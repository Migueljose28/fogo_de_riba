# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 410)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(80, 20, 626, 58))
        self.label_titulo.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);")
        self.label_titulo.setObjectName("label_titulo")
        self.label_cliente = QtWidgets.QLabel(self.centralwidget)
        self.label_cliente.setGeometry(QtCore.QRect(140, 120, 111, 31))
        self.label_cliente.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_cliente.setObjectName("label_cliente")
        self.lineEdit_cliente = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cliente.setGeometry(QtCore.QRect(260, 125, 141, 20))
        self.lineEdit_cliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cliente.setObjectName("lineEdit_cliente")
        self.label_pedido = QtWidgets.QLabel(self.centralwidget)
        self.label_pedido.setGeometry(QtCore.QRect(140, 160, 111, 31))
        self.label_pedido.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_pedido.setObjectName("label_pedido")
        self.comboBox_pedido = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pedido.setGeometry(QtCore.QRect(260, 165, 141, 20))
        self.comboBox_pedido.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_pedido.setObjectName("comboBox_pedido")
        self.comboBox_pedido.addItem("")
        self.label_observacao = QtWidgets.QLabel(self.centralwidget)
        self.label_observacao.setGeometry(QtCore.QRect(150, 210, 231, 31))
        self.label_observacao.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_observacao.setObjectName("label_observacao")
        self.textEdit_observacao = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_observacao.setGeometry(QtCore.QRect(100, 250, 345, 105))
        self.textEdit_observacao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_observacao.setObjectName("textEdit_observacao")
        self.pushButton_concluir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_concluir.setGeometry(QtCore.QRect(490, 256, 201, 31))
        self.pushButton_concluir.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"")
        self.pushButton_concluir.setObjectName("pushButton_concluir")
        self.pushButton_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancelar.setGeometry(QtCore.QRect(490, 293, 201, 31))
        self.pushButton_cancelar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"")
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.pushButton_retornar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_retornar.setGeometry(QtCore.QRect(490, 330, 201, 31))
        self.pushButton_retornar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"")
        self.pushButton_retornar.setObjectName("pushButton_retornar")
        self.spinBox_quantidade = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_quantidade.setGeometry(QtCore.QRect(580, 165, 133, 20))
        self.spinBox_quantidade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_quantidade.setObjectName("spinBox_quantidade")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 160, 141, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 120, 101, 31))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(580, 125, 133, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -30, 801, 471))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 380, 801, 31))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, -10, 801, 31))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 71, 371))
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(730, 20, 71, 361))
        self.label_7.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_3.raise_()
        self.label_titulo.raise_()
        self.label_cliente.raise_()
        self.lineEdit_cliente.raise_()
        self.label_pedido.raise_()
        self.comboBox_pedido.raise_()
        self.label_observacao.raise_()
        self.textEdit_observacao.raise_()
        self.pushButton_concluir.raise_()
        self.pushButton_cancelar.raise_()
        self.pushButton_retornar.raise_()
        self.spinBox_quantidade.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FOGO DED RIBA - PEDIDOS"))
        self.label_titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Restaurante Fogo de Riba</span></p></body></html>"))
        self.label_cliente.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nome:</span></p></body></html>"))
        self.label_pedido.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Produto:</span></p></body></html>"))
        self.comboBox_pedido.setItemText(0, _translate("MainWindow", "Nenhum"))
        self.label_observacao.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Pedidos adicionados:</span></p></body></html>"))
        self.textEdit_observacao.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_concluir.setText(_translate("MainWindow", "Adicionar ao carrinho"))
        self.pushButton_cancelar.setText(_translate("MainWindow", "Finalizar pedido"))
        self.pushButton_retornar.setText(_translate("MainWindow", "Limpar carrinho"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Quantidade:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Telefone:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\"Telas/Imagens/fundoPedidos.jpg\"/></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
