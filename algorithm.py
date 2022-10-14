import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import qrc_resources

class MyWidget(QMainWindow):
    
    """launching an application,
        initializing a window,
        working with widgets functions"""
    
    def __init__(self):
        super().__init__()
        uic.loadUi('gui_qt_designer.ui', self)  # Загружаем дизайн
        # -------------------
        self._click_counter = 0
        self.buttons()
        
    def buttons(self):
        self.git_hub.clicked.connect(lambda: os.system("start \"\" https://github.com/D1R1R/HEAVENcode"))
        # при нажатии на кнопку открыть сайт.
        self.settings_btn.clicked.connect(self.open_settings_menu)
        self.prog_btn.clicked.connect(self.open_programm_menu)
        self.code_btn.clicked.connect(self.open_code_menu)

    def close_all_fr(self):
        self.code_set_fr.setMaximumWidth(0)
        self.Always_on_fr.setMaximumWidth(0)
        self.programm_fr.setMaximumWidth(0)
        self.settings_fr.setMaximumWidth(0)

    def open_settings_menu(self):
        self.close_all_fr()
        if self._click_counter != 1:
            self.settings_fr.setMaximumWidth(16777215)
            self._click_counter = 1
        else:
            self.Always_on_fr.setMaximumWidth(16777215)
            self._click_counter = 0
            
    def open_programm_menu(self):
        self.close_all_fr()
        if self._click_counter != 2:
            self.programm_fr.setMaximumWidth(16777215)
            self._click_counter = 2
        else:
            self.Always_on_fr.setMaximumWidth(16777215)
            self._click_counter = 0

    def open_code_menu(self):
        self.close_all_fr()
        if self._click_counter != 3:
            self.code_set_fr.setMaximumWidth(16777215)
            self._click_counter = 3
        else:
            self.Always_on_fr.setMaximumWidth(16777215)
            self._click_counter = 0
        

class CodeHighlighting():
    
    """text highlighting,
        variable search"""
    
    def variable_search(self):
        pass
    
    def text_highlighting(self):
        pass
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #  app.setStyleSheet(Stylesheet) 
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
