from . import (QDialog, QPushButton, uic, QLineEdit, Veiculo)
from . import (cast)




class Ligeiros(Veiculo):
    last_id = 0
    def __init__(self, velocidade_maxima: float, cor: str, matricula: str):
        Ligeiros.last_id += 1  
        super().__init__(Ligeiros.last_id, velocidade_maxima, cor, matricula)
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



class TelaRegistoli(QDialog):
    def __init__(self, parent=None):
        super(TelaRegistoli, self).__init__(parent)
        uic.loadUi('gui/GUI_ReigistLigeiro.ui', self)
        
        self.btnadd = cast(QPushButton, self.findChild(QPushButton, "btnadd")) ##~cast
        self.btnexit = cast(QPushButton, self.findChild(QPushButton, "btnexit"))

        self.btnadd.clicked.connect(self.accept)
        self.btnexit.clicked.connect(self.reject)

        self.inputmatricula = cast(QLineEdit, self.findChild(QLineEdit, "inputmatricula"))
        self.inputcor = cast(QLineEdit, self.findChild(QLineEdit, "inputcor"))
        self.inputvelocidade = cast(QLineEdit, self.findChild(QLineEdit, "inputvelocidade"))
        
        print("Dialog initialized")

        self.button1 = QPushButton("Button 1", self)
        self.button1.clicked.connect(self.accept)

    def getLigeiro(self):
        print("getLigeiro called")
        velocidade_maxima = float(self.inputvelocidade.text())
        cor = self.inputcor.text()
        matricula = self.inputmatricula.text()
        return Ligeiros(velocidade_maxima, cor, matricula)