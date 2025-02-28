# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as db


class Ui_TelaPedidos(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 500)
        MainWindow.setMinimumSize(QtCore.QSize(790, 500))
        MainWindow.setMaximumSize(QtCore.QSize(790, 500))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(80, 20, 626, 58))
        self.label_titulo.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);")
        self.label_titulo.setObjectName("label_titulo")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setGeometry(QtCore.QRect(140, 185, 111, 31))
        self.label_nome.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_nome.setObjectName("label_nome")
        self.lineEdit_cliente = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cliente.setGeometry(QtCore.QRect(260, 190, 141, 20))
        self.lineEdit_cliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cliente.setObjectName("lineEdit_cliente")
        self.label_produto = QtWidgets.QLabel(self.centralwidget)
        self.label_produto.setGeometry(QtCore.QRect(140, 225, 111, 31))
        self.label_produto.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_produto.setObjectName("label_produto")
        self.comboBox_pedido = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pedido.setGeometry(QtCore.QRect(260, 230, 141, 20))
        self.comboBox_pedido.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_pedido.setObjectName("comboBox_pedido")
        self.comboBox_pedido.addItem("")
        self.label_pedidos = QtWidgets.QLabel(self.centralwidget)
        self.label_pedidos.setGeometry(QtCore.QRect(170, 275, 231, 31))
        self.label_pedidos.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_pedidos.setObjectName("label_pedidos")
        self.textEdit_listaPedidos = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_listaPedidos.setGeometry(QtCore.QRect(130, 315, 301, 105))
        self.textEdit_listaPedidos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_listaPedidos.setObjectName("textEdit_listaPedidos")
        self.pushButton_addCarrinho = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addCarrinho.setGeometry(QtCore.QRect(470, 315, 201, 31))
        self.pushButton_addCarrinho.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"")
        self.pushButton_addCarrinho.setObjectName("pushButton_addCarrinho")
        self.pushButton_finalizarPedido = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_finalizarPedido.setGeometry(QtCore.QRect(470, 355, 201, 31))
        self.pushButton_finalizarPedido.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"")
        self.pushButton_finalizarPedido.setObjectName("pushButton_finalizarPedido")
        self.pushButton_limparCarrinho = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_limparCarrinho.setGeometry(QtCore.QRect(470, 395, 201, 31))
        self.pushButton_limparCarrinho.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"")
        self.pushButton_limparCarrinho.setObjectName("pushButton_limparCarrinho")
        self.spinBox_quantidade = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_quantidade.setGeometry(QtCore.QRect(580, 230, 133, 20))
        self.spinBox_quantidade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_quantidade.setObjectName("spinBox_quantidade")
        self.label_quantidade = QtWidgets.QLabel(self.centralwidget)
        self.label_quantidade.setGeometry(QtCore.QRect(430, 225, 141, 31))
        self.label_quantidade.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_quantidade.setObjectName("label_quantidade")
        self.label_telefone = QtWidgets.QLabel(self.centralwidget)
        self.label_telefone.setGeometry(QtCore.QRect(450, 185, 101, 31))
        self.label_telefone.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_telefone.setObjectName("label_telefone")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(580, 190, 133, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_wallpaper = QtWidgets.QLabel(self.centralwidget)
        self.label_wallpaper.setGeometry(QtCore.QRect(20, 40, 721, 471))
        self.label_wallpaper.setObjectName("label_wallpaper")
        self.pushButton_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(10, 460, 71, 31))
        self.pushButton_voltar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.label_wallpaper.raise_()
        self.label_titulo.raise_()
        self.label_nome.raise_()
        self.lineEdit_cliente.raise_()
        self.label_produto.raise_()
        self.comboBox_pedido.raise_()
        self.label_pedidos.raise_()
        self.textEdit_listaPedidos.raise_()
        self.pushButton_addCarrinho.raise_()
        self.pushButton_finalizarPedido.raise_()
        self.pushButton_limparCarrinho.raise_()
        self.spinBox_quantidade.raise_()
        self.label_quantidade.raise_()
        self.label_telefone.raise_()
        self.lineEdit.raise_()
        self.pushButton_voltar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FOGO DE RIBA - PEDIDOS"))
        self.label_titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Restaurante Fogo de Riba</span></p></body></html>"))
        self.label_nome.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nome:</span></p></body></html>"))
        self.label_produto.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Produto:</span></p></body></html>"))
        self.comboBox_pedido.setItemText(0, _translate("MainWindow", "Nenhum"))
        self.label_pedidos.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Pedidos adicionados:</span></p></body></html>"))
        self.textEdit_listaPedidos.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_addCarrinho.setText(_translate("MainWindow", "Adicionar ao carrinho"))
        self.pushButton_finalizarPedido.setText(_translate("MainWindow", "Finalizar pedido"))
        self.pushButton_limparCarrinho.setText(_translate("MainWindow", "Limpar carrinho"))
        self.label_quantidade.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Quantidade:</span></p></body></html>"))
        self.label_telefone.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Telefone:</span></p></body></html>"))
        self.label_wallpaper.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"Telas/Imagens/fundoPedidos.jpg\"/></p></body></html>"))
        self.pushButton_voltar.setText(_translate("MainWindow", "voltar"))

    #def criardb(): #Para criar a tabela no banco de dados
        #con = db.connect("cardapio.db")
        #cursor = con.cursor()
        #cursor.execute('''
        #CREATE TABLE IF NOT EXISTS pedidos (
        #id INTEGER PRIMARY KEY AUTOINCREMENT,
        #cliente TEXT NOT NULL,
        #telefone TEXT NOT NULL,
        #produtos TEXT NOT NULL,
        #valor INTEGER
        #)
        #''')

    def funcionamentoPedidos(self):
        #con = db.connect("cardapio.db")
        #cursor = con.cursor()
        nome = self.lineEdit_cliente.text().strip().lower()
        telefone = self.lineEdit.text().strip().lower()
        produto = self.comboBox_pedido.currentText()
        quantidade = self.spinBox_quantidade.value()

        Pedido = [produto, quantidade]
        PedidosList = []
        ValorFinal = 0
        Produtos = []

        if self.pushButton_addCarrinho.clicked.connect():
            PedidosList.append(Pedido)

            for pedido in PedidosList:
                Produtos.extend[pedido[0]]
                if pedido[0] == "nome1":
                    ValorUnitario = 1
                elif pedido[0] == "nome2":
                    ValorUnitario = 2
                elif pedido[0] == "nome3":
                    ValorUnitario = 3
                ValorUnitario = ValorUnitario * pedido[1]
                ValorFinal += ValorUnitario

        elif self.pushButton_finalizarPedido.clicked.connect():
            con = db.connect("cardapio.db")
            cursor = con.cursor()
            cursor.execute("INSERT INTO pedidos VALUES (null, %s, %s, %s, %s)",(nome, telefone, Produtos, ValorFinal))

        elif self.pushButton_limparCarrinho.clicked.connect():
            ValorFinal = 0
            PedidosList = []
            Produtos = []

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPedidos = QtWidgets.QMainWindow()
    ui = Ui_TelaPedidos()
    ui.setupUi(TelaPedidos)
    TelaPedidos.show()
    sys.exit(app.exec_())
