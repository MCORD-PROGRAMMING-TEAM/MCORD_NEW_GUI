
from PySide6.QtWidgets import QWidget, QPushButton
from view.view import View


class Model:
    def __init__(self) -> None:
        self.all_menu_buttons = []
        

    def get_all_menu_buttons(self, obj):
        for button in obj.findChildren(QPushButton):
            self.all_menu_buttons.append(button)

    def check_which_slide(self, obj):
        slides_and_pages = {
            'btn_hub': 1,
            'btn_statistic': 2,
            'btn_plot': 3
        }
        slidename = obj.objectName()
        return slides_and_pages[slidename]



    #value of pressbuttonstyle
    pressedbuttonstyle = """
    border-left: 18px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 #ff9ff3, stop:0.5 rgba(85, 170, 255, 0));
    background-color: #2f3542;
    """
