# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3 as db


class Ui_TelaPedidos(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 500)
        
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(80, 0, 626, 58))
        self.label_titulo.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);")
        self.label_titulo.setObjectName("label_titulo")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setGeometry(QtCore.QRect(130, 100, 111, 31))
        self.label_nome.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_nome.setObjectName("label_nome")
        self.lineEdit_cliente = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cliente.setGeometry(QtCore.QRect(260, 110, 141, 20))
        self.lineEdit_cliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cliente.setObjectName("lineEdit_cliente")
        self.label_produto = QtWidgets.QLabel(self.centralwidget)
        self.label_produto.setGeometry(QtCore.QRect(130, 140, 111, 31))
        self.label_produto.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_produto.setObjectName("label_produto")
        self.comboBox_pedido = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pedido.setGeometry(QtCore.QRect(260, 150, 141, 20))
        self.comboBox_pedido.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_pedido.setObjectName("comboBox_pedido")
        
        self.comboBox_pedido.addItem("")
        self.comboBox_pedido.addItem("nome1")
        self.comboBox_pedido.addItem("nome2")
        self.comboBox_pedido.addItem("nome3")

        self.label_pedidos = QtWidgets.QLabel(self.centralwidget)
        self.label_pedidos.setGeometry(QtCore.QRect(300, 200, 231, 31))
        self.label_pedidos.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_pedidos.setObjectName("label_pedidos")
        self.pushButton_atualizarLista = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_atualizarLista.setGeometry(QtCore.QRect(100, 410, 201, 31))
        self.pushButton_atualizarLista.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"")
        self.pushButton_atualizarLista.setObjectName("pushButton_atualizarLista")
        self.pushButton_atualizarLista.clicked.connect(self.carrega_dados) #Para atualizar a tabela do banco


        self.pushButton_realizarPedido = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_realizarPedido.setGeometry(QtCore.QRect(320, 410, 201, 31))
        self.pushButton_realizarPedido.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"")
        self.pushButton_realizarPedido.setObjectName("pushButton_realizarPedido")
        self.pushButton_realizarPedido.clicked.connect(self.realizarPedido)

        
        self.pushButton_limparPedido = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_limparPedido.setGeometry(QtCore.QRect(540, 410, 201, 31))
        self.pushButton_limparPedido.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"")
        self.pushButton_limparPedido.setObjectName("pushButton_limparPedido")
        self.pushButton_limparPedido.clicked.connect(self.limparCampos) #Limpa os campos

        self.spinBox_quantidade = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_quantidade.setGeometry(QtCore.QRect(580, 150, 133, 20))
        self.spinBox_quantidade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_quantidade.setObjectName("spinBox_quantidade")
        self.spinBox_quantidade.setRange(1,10) #Define o range do botão de quantidade

        self.label_quantidade = QtWidgets.QLabel(self.centralwidget)
        self.label_quantidade.setGeometry(QtCore.QRect(430, 140, 141, 31))
        self.label_quantidade.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_quantidade.setObjectName("label_quantidade")
        self.label_telefone = QtWidgets.QLabel(self.centralwidget)
        self.label_telefone.setGeometry(QtCore.QRect(450, 100, 101, 31))
        self.label_telefone.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Ravie\";\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_telefone.setObjectName("label_telefone")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(580, 110, 133, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_wallpaper = QtWidgets.QLabel(self.centralwidget)
        self.label_wallpaper.setGeometry(QtCore.QRect(20, 30, 721, 471))
        self.label_wallpaper.setObjectName("label_wallpaper")
        self.pushButton_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(10, 460, 71, 31))
        self.pushButton_voltar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Ravie\";\n"
"border-radius: 10px;\n"
"")

        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.tableWidget_listaPedidos = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_listaPedidos.setGeometry(QtCore.QRect(160, 240, 518, 151))
        self.tableWidget_listaPedidos.setObjectName("tableWidget_listaPedidos")
        self.tableWidget_listaPedidos.setColumnCount(5)
        self.tableWidget_listaPedidos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_listaPedidos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_listaPedidos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_listaPedidos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_listaPedidos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_listaPedidos.setHorizontalHeaderItem(4, item)
        self.label_wallpaper.raise_()
        self.label_titulo.raise_()
        self.label_nome.raise_()
        self.lineEdit_cliente.raise_()
        self.label_produto.raise_()
        self.comboBox_pedido.raise_()
        self.label_pedidos.raise_()
        self.pushButton_atualizarLista.raise_()
        self.pushButton_realizarPedido.raise_()
        self.pushButton_limparPedido.raise_()
        self.spinBox_quantidade.raise_()
        self.label_quantidade.raise_()
        self.label_telefone.raise_()
        self.lineEdit.raise_()
        self.pushButton_voltar.raise_()
        self.tableWidget_listaPedidos.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.carrega_dados()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Restaurante Fogo de Riba</span></p></body></html>"))
        self.label_nome.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nome:</span></p></body></html>"))
        self.label_produto.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Produto:</span></p></body></html>"))
        self.comboBox_pedido.setItemText(0, _translate("MainWindow", "Nenhum"))
        self.label_pedidos.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">LISTAS DE PEDIDOS:</span></p></body></html>"))
        self.pushButton_atualizarLista.setText(_translate("MainWindow", "ATUALIZAR LISTA"))
        self.pushButton_realizarPedido.setText(_translate("MainWindow", "REALIZAR PEDIDO"))
        self.pushButton_limparPedido.setText(_translate("MainWindow", "LIMPAR PEDIDO"))
        self.label_quantidade.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Quantidade:</span></p></body></html>"))
        self.label_telefone.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Telefone:</span></p></body></html>"))
        self.label_wallpaper.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"Telas/Imagens/fundoPedidos.jpg\"/></p></body></html>"))
        self.pushButton_voltar.setText(_translate("MainWindow", "voltar"))
        item = self.tableWidget_listaPedidos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_listaPedidos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_listaPedidos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TELEFONE"))
        item = self.tableWidget_listaPedidos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PRODUTO"))
        item = self.tableWidget_listaPedidos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CLIENTE"))

    def realizarPedido(self):
        con = db.connect("cardapio.db")
        cursor = con.cursor()

        nome = self.lineEdit_cliente.text().strip().lower()
        telefone = self.lineEdit.text().strip().lower()
        produto = self.comboBox_pedido.currentText()
        quantidade = self.spinBox_quantidade.value()

        if nome == "" or telefone == "":
            msg = QMessageBox()
            msg.setIcon(msg.Warning)
            msg.setWindowTitle("Aviso")
            msg.setText("INFORME SUAS INFORMAÇÕES PESSOAIS!")
            msg.exec_()

        else:
            valor = 0

            if produto == "Nenhum":
                msg = QMessageBox()
                msg.setIcon(msg.Warning)
                msg.setWindowTitle("Aviso")
                msg.setText("SELECIONE ALGUM PRODUTO!")
                msg.exec_()
            elif produto == "nome1":
                valor = 1 * quantidade
            elif produto == "nome2":
                valor = 2 * quantidade
            elif produto == "nome3":
                valor = 3 * quantidade
            elif produto == "nome4":
                valor = 4 * quantidade
        

            if valor != 0:
                cursor.execute("INSERT INTO pedidos VALUES (null, ?, ?, ?, ?)",(nome, telefone, produto, valor))
                con.commit()
                msg = QMessageBox()
                msg.setIcon(msg.Information)
                msg.setWindowTitle("Aviso")
                msg.setText("PEDIDO REALIZADO COM SUCESSO!")
                msg.exec_()

                self.lineEdit_cliente.setText("")
                self.lineEdit.setText("")
                self.comboBox_pedido.setCurrentIndex(0)
                self.spinBox_quantidade.setValue(1)

    def limparCampos(self):
        self.lineEdit_cliente.setText("")
        self.lineEdit.setText("")
        self.comboBox_pedido.setCurrentIndex(0)
        self.spinBox_quantidade.setValue(1)

    def carrega_dados(self):
        # Conectar ao banco de dados
        con = db.connect("cardapio.db")
        cursor = con.cursor()

        # Buscar os dados da tabela
        cursor.execute("SELECT * FROM pedidos")
        rows = cursor.fetchall()

        # Obter os nomes das colunas
        col_names = [description[0] for description in cursor.description]

        # Configurar o TableWidget
        self.tableWidget_listaPedidos.setRowCount(len(rows))
        self.tableWidget_listaPedidos.setColumnCount(len(col_names))
        self.tableWidget_listaPedidos.setHorizontalHeaderLabels(col_names)

        # Preencher o TableWidget com os dados
        for row_idx, linha_dado in enumerate(rows):
            for coluna, coluna_dado in enumerate(linha_dado):
                self.tableWidget_listaPedidos.setItem(row_idx, coluna, QTableWidgetItem(str(coluna_dado)))

        # Fechar a conexão
        con.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPedidos = QtWidgets.QMainWindow()
    ui = Ui_TelaPedidos()
    ui.setupUi(TelaPedidos)
    TelaPedidos.show()
    sys.exit(app.exec_())
