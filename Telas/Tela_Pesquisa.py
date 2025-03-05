# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app
import sqlite3 as db
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaPesquisa(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 523)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(300, 0, 501, 521))
        self.frame.setObjectName("frame")
        self.pushButton_pesquisar = QtWidgets.QPushButton(self.frame)
        self.pushButton_pesquisar.setGeometry(QtCore.QRect(380, 40, 80, 23))
        #entrar na função para pesquisar
        #self.pushButton_pesquisar.clicked.connect(self.pesquisar_ingrediente)


        self.pushButton_pesquisar.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_pesquisar.setObjectName("pushButton_pesquisar")
        self.pushButton_pesquisar.clicked.connect(self.pesquisar_ingrediente)
        self.comboBox_filtrar = QtWidgets.QComboBox(self.frame)
        self.comboBox_filtrar.setGeometry(QtCore.QRect(220, 40, 149, 23))
        self.comboBox_filtrar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_filtrar.setObjectName("comboBox_filtrar")
        self.comboBox_filtrar.addItem("")
        self.comboBox_filtrar.addItem("")
        self.comboBox_filtrar.addItem("")
        self.comboBox_filtrar.addItem("")
        self.comboBox_filtrar.addItem("")
        self.comboBox_filtrar.addItem("")
        self.comboBox_filtrar.addItem("")
        #Pegando os dados por filtro
        self.comboBox_filtrar.currentIndexChanged.connect(self.filtrar)
       
       
        self.plainTextEdit_exibirCardapio = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_exibirCardapio.setGeometry(QtCore.QRect(10, 70, 451, 401))
        self.plainTextEdit_exibirCardapio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.plainTextEdit_exibirCardapio.setPlainText("")
        self.plainTextEdit_exibirCardapio.setObjectName("plainTextEdit_exibirCardapio")
        

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 201, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_cardapio = QtWidgets.QLabel(self.frame)
        self.label_cardapio.setGeometry(QtCore.QRect(67, 10, 346, 16))
        self.label_cardapio.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 81 8pt \"Rockwell Extra Bold\";\n"
"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Ubuntu\";")
        self.label_cardapio.setObjectName("label_cardapio")
        self.pushButton_fazer_pedido = QtWidgets.QPushButton(self.frame)
        self.pushButton_fazer_pedido.setGeometry(QtCore.QRect(340, 480, 121, 21))
        self.pushButton_fazer_pedido.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_fazer_pedido.setObjectName("pushButton_fazer_pedido")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, -10, 301, 541))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 110, 251, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Telas/Imagens/xilo_fixa.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 171, 41))
        self.label_2.setStyleSheet("font: 700 32pt \"Ubuntu\";\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Ubuntu\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_voltar = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_voltar.setGeometry(QtCore.QRect(10, 480, 61, 21))
        self.pushButton_voltar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 191, 21))
        self.label_3.setStyleSheet("\n"
"font: 81 8pt \"Rockwell Extra Bold\";\n"
"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.pushButton_cardapiocompleto = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cardapiocompleto.setGeometry(QtCore.QRect(70, 340, 161, 23))
        self.pushButton_cardapiocompleto.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_cardapiocompleto.setObjectName("pushButton_cardapiocompleto")
        #entrar na função para mostrar cardapio
        self.pushButton_cardapiocompleto.clicked.connect(self.mostrar_cardapio)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FOGO DE RIBA - PESQUISA"))
        self.pushButton_pesquisar.setText(_translate("MainWindow", "Pesquisar"))
        self.comboBox_filtrar.setItemText(0, _translate("MainWindow", "Filtrar"))
        self.comboBox_filtrar.setItemText(1, _translate("MainWindow", "Pratos principais"))
        self.comboBox_filtrar.setItemText(2, _translate("MainWindow", "Entradas"))
        self.comboBox_filtrar.setItemText(3, _translate("MainWindow", "Sobremesas"))
        self.comboBox_filtrar.setItemText(4, _translate("MainWindow", "Bebidas"))
        self.label_cardapio.setText(_translate("MainWindow", "PESQUISE POR COMIDAS OU INGREDIENTE PREDILETOS"))
        


        self.pushButton_fazer_pedido.setText(_translate("MainWindow", "FAZER PEDIDO"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">_CARDÁPIO_</span></p></body></html>"))
        self.pushButton_voltar.setText(_translate("MainWindow", "VOLTAR"))
        self.label_3.setText(_translate("MainWindow", "RESTAURANTE FOGO DE RIBA"))
        self.pushButton_cardapiocompleto.setText(_translate("MainWindow", "cardápio completo"))



    def criar_banco(self):
        conn = db.connect("cardapio.db")
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pratos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descrição TEXT NOT NULL     
        )
                ''')
        
        # Salvar as alterações e fechar a conexão
        conn.commit()
        conn.close()



    def function_normal(self, cursor):
        dados = cursor.fetchall()
        texto = ""
        row = 0
        lists = ["CATEGORIA: ","NOME: ","DESCRIÇÃO: "]

        for linha in dados:
           i = 1
           for list in lists:
                texto += list + str(linha[i]) + "\n"
                i+=1
           texto += "------------------------------\n"
           row += 1
        #Operador ternario para o plural
        obs = (" resultado encontrado."  if cursor.rowcount == 1 else " resultados encontrados.")
        texto += str(row) + obs
        self.plainTextEdit_exibirCardapio.setPlainText(texto)


    def mostrar_cardapio(self):
        conn = db.connect("cardapio.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM pratos ''').fetchone
        self.function_normal(cursor)
        
                
    def pesquisar_ingrediente(self):
          conn = db.connect("cardapio.db")
          cursor = conn.cursor()
          descrição = self.lineEdit.text()

          cursor.execute('''
          SELECT * FROM pratos WHERE nome LIKE ? or descrição LIKE ?
          ''', ('%' + descrição + '%', '%' + descrição + '%',)).fetchone  # Adicionando '%' no parâmetro
          self.function_normal(cursor)
                
          print(descrição)
          conn.commit()
          conn.close()


    def filtrar(self):
         conn = db.connect("cardapio.db")
         cursor = conn.cursor()
         texto_selecionado = self.comboBox_filtrar.currentText()


         cursor.execute('''
         SELECT * FROM pratos WHERE categoria LIKE ?
         ''', ('%' +  texto_selecionado + '%',)).fetchone  # Adicionando '%' no parâmetro
         self.function_normal(cursor)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TelaPesquisa()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
