#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
#from PyQt5.QtCore import Qt
#from PyQt5.QtCore import pyqtSlot
#from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QIcon, QPixmap
#from PyQt5.QtPrintSupport import *
#import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import * 
import os, sys

from template.GUI_Loin import Ui_Login
from template.GUI_Tela import Ui_MainWindow
from template.GUI_RegistLigeiro import Ui_RegistLigeiro


class Veiculo:
    def __init__(self, id_veiculo, velocidade_maxima, cor, matricula):
        self.id_veiculo = id_veiculo
        self.velocidade_maxima = velocidade_maxima
        self.cor = cor
        self.matricula = matricula
        self.categoria = None  

    def __str__(self):
       return (f"Veículo [ID: {self.id_veiculo}, Categoria: {self.categoria}, "
                f"Cor: {self.cor}, Matrícula: {self.matricula}, "
                f"Velocidade Máxima: {self.velocidade_maxima} km/h]")


class Ligeiros(Veiculo):
    def __init__(self, id_veiculo: int, velocidade_maxima: float, cor: str, matricula: str):
        super().__init__(id_veiculo, velocidade_maxima, cor, matricula)
        self.categoria = 'Ligeiros'
    @classmethod


    def manualInsert(cls):
        while True:
            try:
                id_veiculo = int(input("Digite o ID do veículo: "))
                break
            except ValueError:
                print("Valor inválido para o ID. Por favor, insira um número inteiro.")

        while True:
            try:
                velocidade_maxima = float(input("Digite a velocidade máxima do veículo (km/h): "))
                break
            except ValueError:
                print("Valor invalido para a velocidade. Por favor, insira um número.")

       
        cor = input("Digite a cor do veiculo: ")
        matricula = input("Digite a matricula do veiculo: ")
        print("criado com sucesso!!")
        return cls(id_veiculo, velocidade_maxima, cor, matricula)
class telaregistoli(QDialog):
    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui= Ui_RegistLigeiro()
        self.ui.setupUi(self)

class telaprincipal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaprincipal, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionAdd.triggered.connect(self.addLigeiro)

    def addLigeiro(self):
        addLigeiro= telaregistoli() 
        addLigeiro.exec_()


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
            QMessageBox.information(QMessageBox(),"Login realizado com sucesso","Entrou como admin")
            self.window=telaprincipal()
            self.window.show()
        else:
            QMessageBox.information(QMessageBox(),"falha no Login","Credenciais invalidas")


app = QApplication(sys.argv)
if QDialog.Accepted:  
    window = login()
    window.show()
sys.exit(app.exec_())