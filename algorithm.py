import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import webbrowser  # для открытия сайта


class MyWidget(QMainWindow):
    
    """launching an application,
        initializing a window,
        working with widgets functions"""
    
    def __init__(self):
        super().__init__()
        uic.loadUi('gui_qt_designer.ui', self)  # Загружаем дизайн
        self.buttons()
        
    def buttons(self):
        self.git_hub.clicked.connect(lambda: webbrowser.open('http://www.google.com'))
        # при нажатии на кнопку открыть сайт.


class CodeHighlighting():
    
    """text highlighting,
        variable search"""
    
    def variable_search(self):
        pass
    
    def text_highlighting(self):
        pass
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
