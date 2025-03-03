from . import (QDialog, QPushButton, uic, QLineEdit, Veiculo)
from . import (cast)

class Pesados(Veiculo):
    last_id = 0
    def __init__(self, velocidade_maxima: float, cor: str, matricula: str, carga: float):
        Pesados.last_id += 1  
        super().__init__(Pesados.last_id, velocidade_maxima, cor, matricula)
        self.categoria = 'Pesados'
        self.carga = carga 
   
        


class TelaRegistope(QDialog):
    def __init__(self, parent= None):
        super(TelaRegistope, self).__init__(parent)
        uic.loadUi('gui/GUI_RegistPesados.ui', self)

        self.btnadd = cast(QPushButton, self.findChild(QPushButton, "btnaddP")) ##~cast
        self.btnexit = cast(QPushButton, self.findChild(QPushButton, "btnexit"))

        self.btnadd.clicked.connect(self.accept)
        self.btnexit.clicked.connect(self.reject)

        self.inputmatricula = cast(QLineEdit, self.findChild(QLineEdit, "inputmatriculaP"))
        self.inputcor = cast(QLineEdit, self.findChild(QLineEdit, "inputcorP"))
        self.inputvelocidade = cast(QLineEdit, self.findChild(QLineEdit, "inputvelocidadeP"))
        self.inputcarga = cast(QLineEdit, self.findChild(QLineEdit, "inputcarga"))
        
        print("Dialog initialized")

    def getPesado(self):
        print("getPesado called")
        velocidade_maxima = float(self.inputvelocidade.text())
        cor = self.inputcor.text()
        matricula = self.inputmatricula.text()
        carga = float(self.inputcarga.text())
        return Pesados(velocidade_maxima, cor, matricula, carga)
