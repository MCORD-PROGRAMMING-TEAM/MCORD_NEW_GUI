from PySide6.QtCore import QThread, Signal
import socket
import json
from datetime import datetime
import csv
import numpy as np
import sqlite3


class LanController:
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

    def lan_calibration(self):
        self.lan_worker = LanThread(self.LAN, 'calib', int(self._view.ui.diagnostic_combo.currentText()))
        self.lan_worker.start()
        self.lan_worker.calib_response.connect(self.test)
        self.lan_worker.error_response.connect(self._model.error_board_number)
        self.lan_worker.error_response.connect(self._view.error_board_detected)
        self.lan_worker.finished.connect(self.lan_worker.quit)

    def test(self, params):
        print(params)

    def lan_calibration_handle(self, params):
        print("Start calibration curve")
        volt, curr_m, curr_s = params
        volt_master = self._model.valid_breakdown_voltage(volt, curr_m)
        volt_slave = self._model.valid_breakdown_voltage(volt, curr_s)
        self.update_database_calib(int(self._view.ui.diagnostic_combo.currentText()), volt_master, volt_slave,
                                   volt_master + 2, volt_slave + 2)
        ready_params = [int(self._view.ui.diagnostic_combo.currentText()), volt_master + 2, volt_slave + 2]
        self.lan_worker = LanThread(self.LAN, 'set', ready_params)
        self.lan_worker.start()
        self.lan_worker.start_response.connect(self.json_parser)
        self.lan_worker.finished.connect(self.lan_worker.quit)

    def lan_send_update(self):
        if self._model.thread_update_run_status:
            return
        self._model.temp_loop_status = True
        self.lan_worker_update = LanThreadUpdate(self.LAN, self._model)
        self.lan_worker_update.response.connect(self.json_parser)
        self.lan_worker_update.response.connect(self._view.update_params_table)
        self.lan_worker_update.response.connect(self._view.update_graphs)
        self.lan_worker_update.response.connect(self.insert_database_fetch)
        self.lan_worker_update.thread_start.connect(self._model.get_thead_update_status)
        self.lan_worker_update.start()

    def insert_database_fetch(self, params):
        board_id = int(params[-1])
        master_v, slave_v = params[1][0], params[1][1]
        master_temp, slave_temp = params[2][0], params[2][1]
        print(f"Fetched data: {[board_id, master_v, slave_v, master_temp, slave_temp]}")
        self.db.insert_values_from_fetch(None, board_id, master_v, slave_v, master_temp, slave_temp)

    def update_database_calib(self, id, mbr, sbr, mv, sv):
        self.db.update_value_calibration(id, mbr, sbr, mv, sv)
        print("Database updated !!!")

    def lan_autorun(self):
        board_id = int(self._view.ui.diagnostic_combo.currentText())
        master_v, slave_v = self.db.get_voltage_from_db(board_id)
        ready_params = [board_id, float(master_v), float(slave_v)]
        self.lan_worker = LanThread(self.LAN, 'set', ready_params)
        self.lan_worker.start()
        self.lan_worker.finished.connect(self.lan_worker.quit)

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

            for voltage in np.arange(52.0, 66.0, 0.1):
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

    def get_voltage_from_db(self, id):
        self.cursor.execute(f"SELECT master_voltage, slave_voltage FROM breakdown_voltage_view WHERE bar_id = {id}")
        result = self.cursor.fetchall()
        print(f'Got results:{result[0][0]} {result[0][1]} ')
        return result[0][0], result[0][1]

    def update_value_calibration(self, id, master_br, slave_br, master_v, slave_v):
        self.cursor.execute(
            f"UPDATE Calibration_Parameters SET master_v_br = {master_br}, slace_v_br = {slave_br}, master_work_v = {master_v}, slave_work_v = {slave_v} WHERE board_id = {id}  ")
        self.conn.commit()
        print("Values edited")

    def insert_values_from_fetch(self, *params):
        self.cursor.execute(f"INSERT INTO fetcheddata VALUES ({','.join(['?' for _ in params])})", params)
        self.conn.commit()
        print(f"Values added: {params}")