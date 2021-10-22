from app  import App
import pytest
from PySide6.QtCore import Qt


class TestApp:
    
    @pytest.fixture
    def pyapp(self,qtbot):
        apli = App()
        qtbot.addWidget(apli)
        return apli
    
    
    def test_maximize_window(self,pyapp,qtbot):
        qtbot.mouseClick(pyapp.view.ui.maximizeButton,Qt.LeftButton)
        assert pyapp.view.isMaximized()
        
    def test_return_from_maximize_window(self,pyapp,qtbot):
        qtbot.mouseClick(pyapp.view.ui.maximizeButton,Qt.LeftButton)
        qtbot.mouseClick(pyapp.view.ui.maximizeButton,Qt.LeftButton)
        assert (pyapp.view.height(), pyapp.view.width()) == (731 , 1065)
        
    def test_toggle_menu(self,pyapp,qtbot):
        qtbot.mouseClick(pyapp.view.ui.ToggleButton,Qt.LeftButton)
        qtbot.wait(550)
        assert pyapp.view.ui.LeftMenuFrame.minimumWidth() == 160
        
    def test_toggle_menu_close(self,pyapp,qtbot):
        qtbot.mouseClick(pyapp.view.ui.ToggleButton,Qt.LeftButton)
        qtbot.wait(510)
        qtbot.mouseClick(pyapp.view.ui.ToggleButton,Qt.LeftButton)
        qtbot.wait(510)
        assert pyapp.view.ui.LeftMenuFrame.minimumWidth() == 60
        
        
    def test_extra_settings_menu(self,pyapp,qtbot):
        qtbot.mouseClick(pyapp.view.ui.SettingsButton,Qt.LeftButton)
        qtbot.wait(550)
        assert pyapp.view.ui.ExtraLeftMenuFrame.minimumWidth() == 160
        
    def test_extra_settings_menu_close(self,pyapp,qtbot):
        qtbot.mouseClick(pyapp.view.ui.SettingsButton,Qt.LeftButton)
        qtbot.wait(510)
        qtbot.mouseClick(pyapp.view.ui.SettingsButton,Qt.LeftButton)
        qtbot.wait(510)
        assert pyapp.view.ui.ExtraLeftMenuFrame.minimumWidth() == 0
        
        
    def test_home_stackedwidget_default(self,pyapp):
        assert pyapp.view.ui.stackedWidget.currentWidget() == pyapp.view.ui.home_page
        
    def test_change_stacked_to_2nd_page(self,pyapp,qtbot):
        qtbot.mouseClick(pyapp.view.ui.btn_widgets,Qt.LeftButton)
        qtbot.wait(600)
        assert pyapp.view.ui.stackedWidget.currentWidget() == pyapp.view.ui.next_page
        
    def test_change_stacked_to_3rd_page(self,pyapp,qtbot):
        qtbot.mouseClick(pyapp.view.ui.btn_new,Qt.LeftButton)
        qtbot.wait(600)
        assert pyapp.view.ui.stackedWidget.currentWidget() == pyapp.view.ui.title_page
        
    def test_change_stacked_return_to_home(self,pyapp,qtbot):
        qtbot.mouseClick(pyapp.view.ui.btn_new,Qt.LeftButton)
        qtbot.wait(600)
        qtbot.mouseClick(pyapp.view.ui.btn_home,Qt.LeftButton)
        qtbot.wait(600)
        assert pyapp.view.ui.stackedWidget.currentWidget() == pyapp.view.ui.home_page
        

        
        