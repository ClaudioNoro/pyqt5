from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from modulos.login import Ligeiros

class telaregistoli(QDialog):
    def __init__(self, parent=None):
        super(telaregistoli, self).__init__(parent)
        uic.loadUi('gui/GUI_ReigistLigeiro.ui', self)
        self.btnadd.clicked.connect(self.accept)
        self.btnexit.clicked.connect(self.reject)
        print("Dialog initialized")

    def getLigeiro(self):
        print("getLigeiro called")
        id_veiculo = int(self.inputmatricula.text())
        velocidade_maxima = float(self.inputvelocidade.text())
        cor = self.inputcor.text()
        matricula = self.inputmatricula.text()
        return Ligeiros(id_veiculo, velocidade_maxima, cor, matricula)