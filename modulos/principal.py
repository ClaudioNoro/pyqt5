from . import (QMainWindow, QDialog, QTableWidgetItem, uic, QAction, QTableWidget)
from . import cast
from modulos.addligeiros import TelaRegistoli
from modulos.choicewindow import ChoiceWindow
from modulos.addpesados import TelaRegistope

class TelaPrincipal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(TelaPrincipal, self).__init__(*args, **argvs)
        uic.loadUi('gui/GUI_Tela.ui', self)
        
        self.actionAdd= cast(QAction, self.findChild(QAction, "actionAdd"))
        self.actionAdd.triggered.connect(self.choicewindow)
        
        self.ligeiros_list = []
        self.pesados_list = []

        self.tableLig = cast(QTableWidget, self.findChild(QTableWidget, "tableLigeiros"))
        self.tablePes= cast(QTableWidget, self.findChild(QTableWidget, "tablePesados"))
           
        print("Main window initialized")
    
    def choicewindow(self):
        choiceDialog = ChoiceWindow(self)
        if choiceDialog.exec_() == QDialog.Accepted:
            if choiceDialog.choice == 'Ligeiro':
                self.addLigeiro()
            elif choiceDialog.choice == 'Pesado':
                self.addPesado()

    def addLigeiro(self):
        print("addLigeiro called")
        addLigeiroDialog = TelaRegistoli(self)
        if addLigeiroDialog.exec_() == QDialog.Accepted: # Accepted != accepted (funcoes diferente)
            print("Dialog accepted")
            ligeiro = addLigeiroDialog.getLigeiro()
            self.ligeiros_list.append(ligeiro)
            self.updateTableLig()

    def addPesado(self):
        print("addPesado called")
        addPesadoDialog = TelaRegistope(self)
        if addPesadoDialog.exec_() == QDialog.Accepted:
            print("Dialog accepted")
            pesado = addPesadoDialog.getPesado()
            self.pesados_list.append(pesado)
            self.updateTablePes()

    def updateTablePes(self):
        print("updateTable called")
        self.tablePes.setRowCount(len(self.pesados_list))
        for row, pesado in enumerate(self.pesados_list):
            self.tablePes.setItem(row, 0, QTableWidgetItem(str(pesado.id_veiculo)))
            self.tablePes.setItem(row, 1, QTableWidgetItem(pesado.matricula))
            self.tablePes.setItem(row, 2, QTableWidgetItem(pesado.cor))
            self.tablePes.setItem(row, 3, QTableWidgetItem(str(pesado.velocidade_maxima)))
            self.tablePes.setItem(row, 4, QTableWidgetItem(str(pesado.carga)))

    def updateTableLig(self):
        print("updateTable called")
        self.tableLig.setRowCount(len(self.ligeiros_list))
        for row, ligeiro in enumerate(self.ligeiros_list):
            self.tableLig.setItem(row, 0, QTableWidgetItem(str(ligeiro.id_veiculo)))
            self.tableLig.setItem(row, 1, QTableWidgetItem(ligeiro.matricula))
            self.tableLig.setItem(row, 2, QTableWidgetItem(ligeiro.cor))
            self.tableLig.setItem(row, 3, QTableWidgetItem(str(ligeiro.velocidade_maxima)))
            
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