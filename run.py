import sys
from PyQt5.QtWidgets import QDialog, QApplication
from modulos.login import login

app = QApplication(sys.argv)
window = login()
window.show()
sys.exit(app.exec_())