#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
#from PyQt5.QtCore import Qt
#from PyQt5.QtCore import pyqtSlot
#from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QIcon, QPixmap
#from PyQt5.QtPrintSupport import *
#import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from GUI_Loin import Ui_Login
from GUI_Tela import Ui_MainWindow

class telaprincipal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaprincipal, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class login(QDialog):
    def __init__(self, *args, **argvs):
        super(login, self).__init__(*args, **argvs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)   

    def login(self):
        admin= "admin"
        senha="admin"
        user=""
        passwd=""
        user=self.ui.lineEdit.text()
        passwd=self.ui.lineEdit_2.text()
        if user == admin and senha==passwd:
            self.window=telaprincipal()
            self.window.show()
        else:
            pass

app = QApplication(sys.argv)
if QDialog.Accepted:  
    window = login()
    window.show()
sys.exit(app.exec_())