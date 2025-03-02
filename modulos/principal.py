from PyQt5.QtWidgets import QMainWindow, QDialog, QTableWidgetItem
from PyQt5 import uic
from modulos.addligeiros import telaregistoli

class telaprincipal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaprincipal, self).__init__(*args, **argvs)
        uic.loadUi('gui/GUI_Tela.ui', self)
        self.actionAdd.triggered.connect(self.addLigeiro)
        self.ligeiros_list = []
        print("Main window initialized")

    def addLigeiro(self):
        print("addLigeiro called")
        addLigeiroDialog = telaregistoli(self)
        if addLigeiroDialog.exec_() == QDialog.Accepted:
            print("Dialog accepted")
            ligeiro = addLigeiroDialog.getLigeiro()
            self.ligeiros_list.append(ligeiro)
            self.updateTable()

    def updateTable(self):
        print("updateTable called")
        self.tableWidget.setRowCount(len(self.ligeiros_list))
        for row, ligeiro in enumerate(self.ligeiros_list):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(ligeiro.id_veiculo)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(ligeiro.matricula))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(ligeiro.cor))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(ligeiro.velocidade_maxima)))
    #def loadUi(uifile, baseinstance=None, package='', resource_suffix='_rc'):
    #    """loadUi(uifile, baseinstance=None, package='') -> widget
    #   
    #    Load a Qt Designer .ui file and return an instance of the user interface.
    #   
    #    uifile is a file name or file-like object containing the .ui file.
    #    baseinstance is an optional instance of the Qt base class.  If specified
    #    then the user interface is created in it.  Otherwise a new instance of the
    #    base class is automatically created.
    #    package is the optional package which is used as the base for any relative
    #    imports of custom widgets.
    #    resource_suffix is the suffix appended to the basename of any resource file
    #    specified in the .ui file to create the name of the Python module generated
    #    from the resource file by pyrcc4.  The default is '_rc', i.e. if the .ui
    #    file specified a resource file called foo.qrc then the corresponding Python
    #    module is foo_rc.
    #    """
    #   
    #from .Loader.loader import DynamicUILoader
 #
    #return DynamicUILoader(package).loadUi(uifile, baseinstance, resource_suffix)