from PyQt5.QtWidgets import  QDialog, QMessageBox
from PyQt5.QtPrintSupport import * 
from PyQt5.QtWidgets import QDialog
from modulos.principal import telaprincipal
from PyQt5 import uic

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





class login(QDialog):
    
    def __init__(self, *args, **argvs):
        super(login, self).__init__(*args, **argvs)
        uic.loadUi('gui/GUI_Login.ui', self)
        self.ui.pushButton.clicked.connect(self.login)   

    def login(self):
        admin = "admin"
        senha = "admin"
        user = self.ui.lineEdit.text()
        passwd = self.ui.lineEdit_2.text()
        if user == admin and senha == passwd:
            QMessageBox.information(self, "Login realizado com sucesso", "Entrou como admin")
            self.window = telaprincipal()
            self.window.show()
        else:
            QMessageBox.information(self, "Falha no Login", "Credenciais inválidas")