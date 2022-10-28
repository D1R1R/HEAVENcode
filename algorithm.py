import sys
import os
import keyword
import builtins
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenu, QAction
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat
from PyQt5.QtCore import Qt, QRegularExpression
import qrc_resources 

class Window(QMainWindow):
    
    """launching an application,
        initializing a window,
        working with widgets functions"""
    
    def __init__(self):
        super().__init__()
        uic.loadUi('gui_qt_designer.ui', self)  # Загружаем дизайн
        # -------------------
        self._click_counter = 0
        # -------------------
        self.buttons()

    def lines(self, line):
        self.label.setText(f"lines: {line[0]}")
        
    def buttons(self):
        # BUTTONS
        self.git_hub.clicked.connect(lambda: os.system("start \"\" https://github.com/D1R1R/HEAVENcode"))
        # при нажатии на кнопку открыть сайт.
        self.settings_btn.clicked.connect(self.open_settings_menu)
        self.prog_btn.clicked.connect(self.open_programm_menu)
        self.code_btn.clicked.connect(self.open_code_menu)
        self.save_path_btn.clicked.connect(settings.save_path)
        self.fast_save_btn.clicked.connect(self.save_f_file)
        self.close_file_win.clicked.connect(self.close_file)
        self.new_file_f.clicked.connect(self.new_file)
        # MENU
        menu = QMenu()
        self.menu_btn.setMenu(menu)
        self.settings_menu(menu)
        # self.code_edit.setHtml('<font color="blue">Синий шрифт</font>')
        self.code_edit.installEventFilter(self)

    def new_file(self):
        with open(settings.path_to_afto_save + '\\' + 'untitled.txt', "w") as file:
            self.code_edit.setHtml("""
                                   <font color=#5c5c73 size=4># Let's create our personal universe together!</font>
                                   <br>
                                   <font color=#5c5c73 size=4># print("Hello world!")</font>
                                   """)
        
        
    def save_f_file(self):
        os.replace(settings.file_source + '\\' + settings.now_file, settings.path_to_afto_save + '\\' + settings.now_file)
        settings.file_source = settings.path_to_afto_save


    def settings_menu(self, menu):
        pass

    def close_file(self):
        pass

    def open_file_inWin(self):
        pass
               
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


class Settings(Window):
    
    def __init__(self):
        self.path_to_afto_save = r'C:\Users\User\Downloads'
        self.now_file = 'greetings.txt'
        self.file_source = r'C:\Users\User\Desktop\для Python\pyQt project'
        self._open = 1
        self.var = []

    def afto_save(self):
        pass

    def save_path(self):
        file_name = QFileDialog.getExistingDirectory(self, 'Select a Directory')
        if len(file_name) != 0:
            self.path.setText(file_name)
            self.path_to_afto_save = file_name
    

class MyHighlighter(QSyntaxHighlighter):
    def __init__(self, parent, qt_colors):
        super().__init__(parent)
        self.keywords_format = dict()
        self.keywords3 = []
        self.colors = qt_colors

        keyw = QTextCharFormat()
        keyw.setForeground(self.colors[0])
        keywords = keyword.kwlist
        for word in keywords:
            token = QRegularExpression("\\b" + word + "\\b")
            self.keywords_format[token] = keyw

        keyw2 = QTextCharFormat()
        keyw2.setForeground(self.colors[1])
        keywords2 = builtins

        for word in dir(keywords2):
            token = QRegularExpression("\\b" + word + "\\b")
            self.keywords_format[token] = keyw2
            
    def highlightBlock(self, text):
        line = text.split('\n')[-1]
        if " = " in line:
            keyw3 = QTextCharFormat()
            keyw3.setForeground(self.colors[2])
            token = QRegularExpression("\\b" + line[:line.index("=")].strip() + "\\b")
            self.keywords_format[token] = keyw3
            
        for tokens, ch_format in self.keywords_format.items():
            expression = QRegularExpression(tokens)
            it = expression.globalMatch(text)
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), ch_format)


                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    settings = Settings()
    ex = Window()
    highlighter = MyHighlighter(ex.code_edit.document(), [Qt.blue, Qt.red, Qt.green])
    ex.show()
    sys.exit(app.exec_())
