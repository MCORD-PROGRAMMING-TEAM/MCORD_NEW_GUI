import time

from PySide6.QtCore import QThread, Signal
import socket
import json
from datetime import datetime
import csv
import numpy as np
import sqlite3


class LanController:
    LIMIT_BIT_CURRENT = 16
    INITIAL_VOLTAGE = 48.5
    FINAL_VOLTAGE = 63.0
    EPSILON = 0.0000001
    VOLTAGE_STEP = 2.0
    SLEEP_TIME = 10

    def __init__(self, view, model) -> None:
        self._view = view
        self._model = model
        self.LAN = None
        self.db = DB()

    def allowed_only_lan(self):
        text = self._view.ui.connection_edit.text()
        result = self._model.valid_ipaddress(text)
        if result:
            self._model.ip = text
        self._view.change_if_ip_reponse(result)

    def set_current_device(self):
        self._model.active_source = 'LAN'

    def create_lan_client(self):
        self.LAN = LanClient()
        try:
            res = self.LAN.connect((self._model.ip, 5555)).decode()
            self._view.update_console(res)
            self._model.connected_lan = True
        except:
            self._model.valid_ip = False
            self._model.connection_error()

    def close_lan_client(self):
        if self._model.connected_lan:
            self.LAN.close_connection()

    def json_parser(self, obj):
        res = f'{obj[0]} : {obj[1:]}'
        self._view.update_console(res)

    def detect_error(self):
        self._model.board_error = True

    def lan_send_start(self, status):
        if status:
            self.lan_worker = LanThread(self.LAN, 'start', int(self._model.board_comlist[-1]))
            self.lan_worker.start()
            self.lan_worker.start_response.connect(self.json_parser)
            self.lan_worker.error_response.connect(self._model.error_board_number)
            self.lan_worker.error_response.connect(self._view.error_board_detected)
            self.lan_worker.finished.connect(self.lan_worker.quit)
            self.lan_worker.finished.connect(self._view.ui.voltage_graph.create_series(self._model.board_comlist[-1]))
            self.lan_worker.finished.connect(
                self._view.ui.temperature_graph.create_series(self._model.board_comlist[-1]))
        else:
            self.lan_worker = LanThread(self.LAN, 'stop', self._model.current_board_number)
            self.lan_worker.start()
            self.lan_worker.start_response.connect(self.json_parser)
            self.lan_worker.finished.connect(self.lan_worker.quit)
            self.lan_worker.finished.connect(
                self._view.ui.voltage_graph.remove_series(self._model.current_board_number))
            self.lan_worker.finished.connect(
                self._view.ui.temperature_graph.remove_series(self._model.current_board_number))

    def lan_send_voltage(self):
        mv, sv = self._model.simp_work_params[self._model.active_board][0], \
                 self._model.simp_work_params[self._model.active_board][1]
        params = [self._model.active_board, mv, sv]
        self.lan_worker = LanThread(self.LAN, 'set', params)
        self.lan_worker.start()
        self.lan_worker.start_response.connect(self.json_parser)
        self.lan_worker.finished.connect(self.lan_worker.quit)

    def test(self, params):
        print(params)

    @staticmethod
    def calculate_breakdown_voltage(voltage_current_curve):
        for voltage_current in voltage_current_curve:
            if voltage_current[1] > LanController.LIMIT_BIT_CURRENT:
                return voltage_current[0]
        return -1

    def get_voltage_current_curve(self, bar_id):
        voltage = LanController.INITIAL_VOLTAGE
        end_voltage = LanController.FINAL_VOLTAGE
        self.LAN.do_cmd(['init', bar_id])
        self.LAN.do_cmd(['hvon', bar_id])
        curve_master = []
        curve_slave = []
        while voltage < end_voltage + LanController.EPSILON:
            self.LAN.do_cmd(['setdac', bar_id, voltage, voltage])
            time.sleep(LanController.SLEEP_TIME)
            current_master = self.LAN.do_cmd(['adc', bar_id, 5])
            current_slave = self.LAN.do_cmd(['adc', bar_id, 6])
            curve_master.append((voltage, current_master[1]))
            curve_slave.append((voltage, current_slave[1]))
            voltage += LanController.VOLTAGE_STEP
        return curve_master, curve_slave

    def start_calibration_hub_detectors(self):
        ip_address = self._view.ui.connection_edit.text()
        bar_and_sipm_ids_list = self.db.get_bar_and_sipm_ids_to_calibration(ip_address)
        for bar_and_sipm_ids in bar_and_sipm_ids_list:
            bar_id = int(bar_and_sipm_ids[0])

            initial_temp_master, initial_temp_slave = self.LAN.do_cmd(['gettemp', bar_id])[1] #zgaduje ze indeks 0 wskazuje na temperature z afe master, a 1 ze slave

            beginning_date = datetime.now().timestamp() * 1000

            voltage_current_curves = self.get_voltage_current_curve(bar_id)

            final_temp_master, final_temp_slave = self.LAN.do_cmd(['gettemp', bar_id])[1]
            end_date = datetime.now().timestamp() * 1000

            breakdown_voltage_master = LanController.calculate_breakdown_voltage(voltage_current_curves[0])
            breakdown_voltage_slave = LanController.calculate_breakdown_voltage(voltage_current_curves[1])

            parameters_master = {'breakdownVoltage': breakdown_voltage_master,
                                 'initialTemperature': initial_temp_master,
                                 'beginningDate': beginning_date,
                                 'finalTemperature': final_temp_master,
                                 'endDate': end_date,
                                 'isRecent': 1,
                                 'sipmId': bar_and_sipm_ids[1],
                                 'sipmDateFrom': bar_and_sipm_ids[2]
                                 }

            parameters_slave = {'breakdownVoltage': breakdown_voltage_slave,
                                'initialTemperature': initial_temp_slave,
                                'beginningDate': beginning_date,
                                'finalTemperature': final_temp_slave,
                                'endDate': end_date,
                                'isRecent': 1,
                                'sipmId': bar_and_sipm_ids[3],
                                'sipmDateFrom': bar_and_sipm_ids[4]
                                }

            calibration_parameter_master_id = self.db.create_calibration_parameter_record(parameters_master)
            calibration_parameter_slave_id = self.db.create_calibration_parameter_record(parameters_slave)

            for point in voltage_current_curves[0]:
                self.db.create_calibration_curve_record(point[0], point[1], calibration_parameter_master_id)

            self.db.update_is_recent(bar_and_sipm_ids[1], bar_and_sipm_ids[2], calibration_parameter_master_id)

            for point in voltage_current_curves[1]:
                self.db.create_calibration_curve_record(point[0], point[1], calibration_parameter_slave_id)

            self.db.update_is_recent(bar_and_sipm_ids[3], bar_and_sipm_ids[4], calibration_parameter_slave_id)

        self.db.conn.commit()

    def start_calibration_bars_detectors(self):
        ip_bars = self._model.board_comlist
        bar_and_sipm_ids_list = self.db.get_bar_and_sipm_ids_to_calibration(ip_bars)
        for bar_and_sipm_ids in bar_and_sipm_ids_list:
            bar_id = int(bar_and_sipm_ids[0])

            initial_temp_master, initial_temp_slave = self.LAN.do_cmd(['gettemp', bar_id])[1]

            beginning_date = datetime.now().timestamp() * 1000

            voltage_current_curves = self.get_voltage_current_curve(bar_id)

            final_temp_master, final_temp_slave = self.LAN.do_cmd(['gettemp', bar_id])[1]
            end_date = datetime.now().timestamp() * 1000

            breakdown_voltage_master = LanController.calculate_breakdown_voltage(voltage_current_curves[0])
            breakdown_voltage_slave = LanController.calculate_breakdown_voltage(voltage_current_curves[1])

            parameters_master = {'breakdownVoltage': breakdown_voltage_master,
                                 'initialTemperature': initial_temp_master,
                                 'beginningDate': beginning_date,
                                 'finalTemperature': final_temp_master,
                                 'endDate': end_date,
                                 'isRecent': 1,
                                 'sipmId': bar_and_sipm_ids[1],
                                 'sipmDateFrom': bar_and_sipm_ids[2]
                                 }

            parameters_slave = {'breakdownVoltage': breakdown_voltage_slave,
                                'initialTemperature': initial_temp_slave,
                                'beginningDate': beginning_date,
                                'finalTemperature': final_temp_slave,
                                'endDate': end_date,
                                'isRecent': 1,
                                'sipmId': bar_and_sipm_ids[3],
                                'sipmDateFrom': bar_and_sipm_ids[4]
                                }

            calibration_parameter_master_id = self.db.create_calibration_parameter_record(parameters_master)
            calibration_parameter_slave_id = self.db.create_calibration_parameter_record(parameters_slave)

            for point in voltage_current_curves[0]:
                self.db.create_calibration_curve_record(point[0], point[1], calibration_parameter_master_id)

            self.db.update_is_recent(bar_and_sipm_ids[1], bar_and_sipm_ids[2], calibration_parameter_master_id)

            for point in voltage_current_curves[1]:
                self.db.create_calibration_curve_record(point[0], point[1], calibration_parameter_slave_id)

            self.db.update_is_recent(bar_and_sipm_ids[3], bar_and_sipm_ids[4], calibration_parameter_slave_id)

        self.db.conn.commit()


    def lan_send_update(self):
        if self._model.thread_update_run_status:
            return
        self._model.temp_loop_status = True
        self.lan_worker_update = LanThreadUpdate(self.LAN, self._model)
        self.lan_worker_update.response.connect(self.json_parser)
        self.lan_worker_update.response.connect(self._view.update_params_table)
        self.lan_worker_update.response.connect(self._view.update_graphs)
        # self.lan_worker_update.response.connect(self.insert_database_fetch)
        self.lan_worker_update.thread_start.connect(self._model.get_thead_update_status)
        self.lan_worker_update.start()

    def start_hub_detectors(self):
        ip_address = self._view.ui.connection_edit.text()
        bar_voltage_list = self.db.get_voltage_list_from_db(ip_address)
        for voltage in bar_voltage_list:
            self.LAN.do_cmd(['init', int(voltage[0])])
            self.LAN.do_cmd(['hvon', int(voltage[0])])
            self.LAN.do_cmd(['setdac', int(voltage[0]), voltage[1], voltage[2]])

    def start_bars_detectors(self):
        ip_bars = self._model.board_comlist
        bar_voltage_list = self.db.get_voltage_list_from_db(ip_bars)
        for voltage in bar_voltage_list:
            self.LAN.do_cmd(['init', int(voltage[0])])
            self.LAN.do_cmd(['hvon', int(voltage[0])])
            self.LAN.do_cmd(['setdac', int(voltage[0]), voltage[1], voltage[2]])

    def lan_update_stop(self, status):
        if not status and self._model.temp_loop_status:
            if not self._model.valid_powerbuttons_status():
                self.lan_worker_update.easy_end_thread()


class LanClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, args):
        try:
            self.sock.connect((args))
            return self.sock.recv(1024)
        except:
            return

    def do_cmd(self, obj):
        self.sock.sendall((json.dumps(obj)).encode("utf8"))
        res = self.sock.recv(1024)
        if res:
            res = json.loads(res)
            return res
        else:
            pass

    def close_connection(self):
        self.sock.sendall((json.dumps(['!disconnect']).encode("utf8")))


class LanThread(QThread):
    connection_response = Signal(str)
    start_response = Signal(list)
    error_response = Signal(int)
    progress = Signal(int)
    calib_response = Signal(list)

    def __init__(self, client, func, command) -> None:
        super().__init__()
        self.client = client
        self.command = command
        self.func = func

    def run(self):

        if self.func == 'start':
            res = self.client.do_cmd(['init', int(self.command)])
            if self.check_ERR(res):
                self.error_response.emit(int(self.command))
                return
            self.start_response.emit(res)
            res = self.client.do_cmd(['hvon', int(self.command)])
            self.start_response.emit(res)

        elif self.func == 'set':
            res = self.client.do_cmd(['setdac', int(self.command[0]), int(self.command[1]), int(self.command[2])])
            print(res)
            self.start_response.emit(res)

        elif self.func == 'stop':
            res = self.client.do_cmd(['hvoff', int(self.command)])
            self.start_response.emit(res)

        elif self.func == 'calib':
            volt, curr_m, curr_s = [], [], []
            self.client.do_cmd(['init', int(self.command)])
            self.client.do_cmd(['hvon', int(self.command)])

            for voltage in np.arange(49.0, 63.0, 0.1):
                self.client.do_cmd(['setdac', int(self.command), voltage, voltage])
                res_master = self.client.do_cmd(['adc', int(self.command), 5])
                res_slave = self.client.do_cmd(['adc', int(self.command), 6])
                print([int(self.command), voltage, res_master[1], res_slave[1]])
                volt.append(voltage)
                curr_m.append(res_master[1])
                curr_s.append(res_slave[1])

            self.calib_response.emit([volt, curr_m, curr_s])

    def check_ERR(self, res):
        if res[0] == 'ERR':
            return True


class LanThreadUpdate(QThread):
    response = Signal(list)
    thread_start = Signal(bool)

    def __init__(self, client, model):
        super().__init__()
        self.client = client
        self.model = model
        self.run_status = True
        self.entire_wait_time = 30
        self.wait_time = 2
        self.csv = False

    def run(self):

        self.thread_start.emit(True)
        while self.run_status:
            # wait loop
            for i in range(self.entire_wait_time):
                if self.run_status:
                    print(i)
                    self.sleep(self.wait_time)
                else:
                    break

            # to faster run thread
            if not self.run_status:
                break

            for board in self.model.board_comlist:
                res = self.client.do_cmd(['getVT', int(board)])
                print(res)
                res.append(board)
                self._csvwriter('outputlog.csv', res)
                self.response.emit(res)

    def easy_end_thread(self):
        self.thread_start.emit(False)
        self.run_status = False

    @staticmethod
    def _getTime():
        now = datetime.now()
        return now.strftime("%d/%m/%Y"), now.strftime("%H:%M:%S")

    def _csvwriter(self, filename, *args):
        if not self.csv:
            labels = ('Data', 'Time', 'Board',
                      'Master_voltage', 'Slave_voltage', 'Master_Temp', 'Slave_Temp')
            self.csv = True
            with open(filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(labels)

        currdata, currtime = self._getTime()
        row = (currdata, currtime, int(args[0][-1]), args[0][1][0], args[0][2][0], args[0][1][1], args[0][2][1])

        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)


class DB:
    def __init__(self) -> None:
        self.dbname = "MCORD_Server_sqlite_db_test2.sqlite3"
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def get_voltage_list_from_db(self, param):
        if isinstance(param, list):
            bar_ids = ', '.join(param)
            self.cursor.execute(f"SELECT bar_id, master_voltage, slave_voltage "
                                f"FROM optimal_voltage_view "
                                f"WHERE bar_id IN ({bar_ids}) " 
                                f"AND calibration_master_is_recent = 1 AND calibration_slave_is_recent = 1")
        else:
            self.cursor.execute(f"SELECT bar_id, master_voltage, slave_voltage "
                                f"FROM all_optimal_voltage_view "
                                f"WHERE ip_address = \'{param}\' "
                                f"AND calibration_master_is_recent = 1 AND calibration_slave_is_recent = 1")
        return self.cursor.fetchall()

    def get_bar_and_sipm_ids_to_calibration(self, param):
        if isinstance(param, list):
            bar_ids = ', '.join(param)
            self.cursor.execute(
                f"SELECT bar_serial_number, sipm_master_id, sipm_master_date_from, sipm_ext_master_id, sipm_ext_date_from "
                f"FROM bar_and_sipm_id_list_to_calibration_view "
                f"WHERE bar_serial_number IN ({bar_ids})"
            )
        else:
            self.cursor.execute(
                f"SELECT bar_serial_number, sipm_master_id, sipm_master_date_from, sipm_ext_master_id, sipm_ext_date_from "
                f"FROM bar_and_sipm_ids_to_calibration_view "
                f"WHERE ip_address = \'{param}\' "
            )
        return self.cursor.fetchall()

    def create_calibration_parameter_record(self, parameters):
        return self.cursor.execute(f"INSERT INTO calibration_parameters (breakdown_voltage, initial_temperature,"
                                   f" beggining_date, final_temperature, end_date, is_recent, sipm_id, sipm_date_from)"
                                   f"VALUES ( {parameters['breakdownVoltage']}, {parameters['initialTemperature']}, {parameters['beginningDate']}, "
                                   f"{parameters['finalTemperature']}, {parameters['endDate']}, "
                                   f"{parameters['isRecent']}, {parameters['sipmId']}, {parameters['sipmDateFrom']})").lastrowid

    def create_calibration_curve_record(self, voltage, current, calibration_parameters_id):
        self.cursor.execute(f"INSERT INTO calibration_curve(voltage, current, callibration_parameters_id)"
                            f"VALUES({voltage}, {current}, {calibration_parameters_id})")

    def update_is_recent(self, sipm_id, sipm_date_from, recent_id):
        self.cursor.execute(f"UPDATE calibration_parameters "
                            f"SET is_recent = 0 "
                            f"WHERE sipm_id = {sipm_id} AND sipm_date_from = {sipm_date_from} AND id <> {recent_id}")

