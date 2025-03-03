from . import (QDialog, QPushButton, QMessageBox, QLineEdit, uic)
from . import (cast)
from modulos.principal import TelaPrincipal 


class login(QDialog):
    
    def __init__(self, *args, **argvs):
        super(login, self).__init__(*args, **argvs)
        uic.loadUi('gui/GUI_Login.ui', self)

        self.loginBtn = cast(QPushButton, self.findChild(QPushButton, "loginButton"))
        self.usernameLnEdt = cast(QLineEdit, self.findChild(QLineEdit, "userLnEdt"))
        self.passwdLnEdt = cast(QLineEdit, self.findChild(QLineEdit, "passLnEdt"))

        self.loginBtn.clicked.connect(self.login) 

    def login(self):
        admin = "admin"
        senha = "admin"
        user = self.usernameLnEdt.text()
        passwd = self.passwdLnEdt.text()
        if user == admin and senha == passwd:
            QMessageBox.information(self, "Login realizado com sucesso", "Entrou como admin")
            self.window = TelaPrincipal()
            self.window.show()
        else:
            QMessageBox.information(self, "Falha no Login", "Credenciais inválidas")