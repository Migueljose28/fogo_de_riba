# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 490)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 490))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 490))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_nomeRestaurante = QtWidgets.QLabel(self.centralwidget)
        self.label_nomeRestaurante.setGeometry(QtCore.QRect(180, 0, 651, 61))
        self.label_nomeRestaurante.setObjectName("label_nomeRestaurante")
        self.pushButton_sobre = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sobre.setGeometry(QtCore.QRect(10, 440, 101, 41))
        self.pushButton_sobre.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Telas/Imagens/aboutIcon.jfif"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_sobre.setIcon(icon)
        self.pushButton_sobre.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_sobre.setObjectName("pushButton_sobre")
        self.pushButton_cardapio = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cardapio.setGeometry(QtCore.QRect(640, 260, 301, 51))
        self.pushButton_cardapio.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Telas/Imagens/cardapio2Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_cardapio.setIcon(icon1)
        self.pushButton_cardapio.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_cardapio.setObjectName("pushButton_cardapio")
        self.pushButton_fechar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_fechar.setGeometry(QtCore.QRect(890, 440, 101, 41))
        self.pushButton_fechar.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Telas/Imagens/leaveIcon.jfif"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_fechar.setIcon(icon2)
        self.pushButton_fechar.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_fechar.setObjectName("pushButton_fechar")
        self.pushButton_pedidos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pedidos.setGeometry(QtCore.QRect(640, 330, 301, 51))
        self.pushButton_pedidos.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Telas/Imagens/cardapioIcon.jfif"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_pedidos.setIcon(icon3)
        self.pushButton_pedidos.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_pedidos.setObjectName("pushButton_pedidos")
        self.label_fundo1 = QtWidgets.QLabel(self.centralwidget)
        self.label_fundo1.setGeometry(QtCore.QRect(0, 70, 591, 361))
        self.label_fundo1.setObjectName("label_fundo1")
        self.label_fundo2 = QtWidgets.QLabel(self.centralwidget)
        self.label_fundo2.setGeometry(QtCore.QRect(590, 70, 411, 361))
        self.label_fundo2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_fundo2.setObjectName("label_fundo2")
        self.label_fraseWow = QtWidgets.QLabel(self.centralwidget)
        self.label_fraseWow.setGeometry(QtCore.QRect(600, 130, 371, 91))
        self.label_fraseWow.setObjectName("label_fraseWow")
        self.label_nomeRestaurante.raise_()
        self.label_fundo1.raise_()
        self.label_fundo2.raise_()
        self.label_fraseWow.raise_()
        self.pushButton_cardapio.raise_()
        self.pushButton_pedidos.raise_()
        self.pushButton_sobre.raise_()
        self.pushButton_fechar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela Principal"))
        self.label_nomeRestaurante.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#000000;\">Restaurante Fogo de Riba</span></p></body></html>"))
        self.pushButton_sobre.setText(_translate("MainWindow", "SOBRE NÓS"))
        self.pushButton_cardapio.setText(_translate("MainWindow", "  ACESSE NOSSO CARDÁPIO"))
        self.pushButton_fechar.setText(_translate("MainWindow", " SAIR"))
        self.pushButton_pedidos.setText(_translate("MainWindow", "  FAÇA JÁ O SEU PEDIDO!"))
        self.label_fundo1.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"Telas/Imagens/gaviao.jpg\"/></p></body></html>"))
        self.label_fundo2.setText(_translate("MainWindow", "TextLabel"))
        self.label_fraseWow.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Fogo de riba no fogão,<br/>calor no coração!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
