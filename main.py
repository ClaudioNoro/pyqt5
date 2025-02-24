from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from GUI_Loin import Ui_Login

class login(QDialog):
    def __init__(self, *args,**argvs):
        super(login, self).__init__(*args,**argvs)
        self.ui= Ui_Login()
        self.ui.setupUi(self)

app= QApplication(sys.argv)
if(QDialog.accepted == True):
    window=login()
    window.show()
sys.exit(app.exec_())