# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 298)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(-20, 60, 111, 16))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("image: url(:/img/icons/user.png);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(-20, 110, 111, 16))
        self.label_3.setStyleSheet("image: url(:/img/icons/key.png);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 170, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 170, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 121, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 131, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 130, 131, 22))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cool auth system</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "login"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:8pt; text-decoration: underline; color:#1a9cff;\">forgot your password?</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "example@example.com"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "password"))
import template.img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
