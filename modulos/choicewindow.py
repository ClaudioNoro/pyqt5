from . import (QDialog, QPushButton, uic)
from . import (cast)

class ChoiceWindow(QDialog):
    def __init__(self, parent=None):
        super(ChoiceWindow, self).__init__(parent)
        uic.loadUi('gui/GUI_choice.ui', self)
        
        self.btnLigeiro = cast(QPushButton, self.findChild(QPushButton, "btnLigeiro"))
        self.btnPesado = cast(QPushButton, self.findChild(QPushButton, "btnPesado"))
        
        self.btnLigeiro.clicked.connect(self.acceptLigeiro)
        self.btnPesado.clicked.connect(self.acceptPesado)
        
        self.choice = None

    def acceptLigeiro(self):
        self.choice = 'Ligeiro'
        self.accept()

    def acceptPesado(self):
        self.choice = 'Pesado'
        self.accept()