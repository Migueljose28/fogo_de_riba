# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QLineEdit, QMessageBox

import sqlite3 as db



class Ui_TelaLoginCadastro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 602)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_cadastro_usuarios = QtWidgets.QWidget(self.centralwidget)
        self.widget_cadastro_usuarios.setGeometry(QtCore.QRect(389, -10, 421, 621))
        self.widget_cadastro_usuarios.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_cadastro_usuarios.setObjectName("widget_cadastro_usuarios")
        self.lineEdit_cadastro_usuario = QtWidgets.QLineEdit(self.widget_cadastro_usuarios)
        self.lineEdit_cadastro_usuario.setGeometry(QtCore.QRect(150, 190, 181, 41))
        self.lineEdit_cadastro_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding: 5px;")
        self.lineEdit_cadastro_usuario.setObjectName("lineEdit_cadastro_usuario")
        self.lineEdit_cadastro_email = QtWidgets.QLineEdit(self.widget_cadastro_usuarios)
        self.lineEdit_cadastro_email.setGeometry(QtCore.QRect(150, 250, 181, 41))
        self.lineEdit_cadastro_email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding: 5px;")
        self.lineEdit_cadastro_email.setObjectName("lineEdit_cadastro_email")
        self.lineEdit_cadastro_telefone = QtWidgets.QLineEdit(self.widget_cadastro_usuarios)
        self.lineEdit_cadastro_telefone.setGeometry(QtCore.QRect(150, 310, 181, 41))
        self.lineEdit_cadastro_telefone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding: 5px;")
        self.lineEdit_cadastro_telefone.setObjectName("lineEdit_cadastro_telefone")
        self.lineEdit_cadastro_senha = QtWidgets.QLineEdit(self.widget_cadastro_usuarios)

        self.lineEdit_cadastro_senha.setEchoMode(QLineEdit.Password)

        self.lineEdit_cadastro_senha.setGeometry(QtCore.QRect(150, 370, 181, 41))
        self.lineEdit_cadastro_senha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding: 5px;")
        self.lineEdit_cadastro_senha.setObjectName("lineEdit_cadastro_senha")
        self.label_cadastro_usuario = QtWidgets.QLabel(self.widget_cadastro_usuarios)
        self.label_cadastro_usuario.setGeometry(QtCore.QRect(60, 190, 81, 31))
        self.label_cadastro_usuario.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Sitka\";\n"
"")
        self.label_cadastro_usuario.setObjectName("label_cadastro_usuario")
        self.label_cadastro_email = QtWidgets.QLabel(self.widget_cadastro_usuarios)
        self.label_cadastro_email.setGeometry(QtCore.QRect(80, 250, 61, 31))
        self.label_cadastro_email.setStyleSheet("background-color: transparent;\n"
"font: 12pt \"Sitka\";\n"
"")
        self.label_cadastro_email.setObjectName("label_cadastro_email")
        self.label_cadastro_telefone = QtWidgets.QLabel(self.widget_cadastro_usuarios)
        self.label_cadastro_telefone.setGeometry(QtCore.QRect(70, 310, 71, 31))
        self.label_cadastro_telefone.setStyleSheet("background-color: transparent;\n"
"font: 12pt \"Sitka\";\n"
"")
        self.label_cadastro_telefone.setObjectName("label_cadastro_telefone")
        self.label_cadastro_senha = QtWidgets.QLabel(self.widget_cadastro_usuarios)
        self.label_cadastro_senha.setGeometry(QtCore.QRect(90, 370, 61, 31))
        self.label_cadastro_senha.setStyleSheet("background-color: transparent;\n"
"font: 12pt \"Sitka\";\n"
"")
        self.label_cadastro_senha.setObjectName("label_cadastro_senha")
        self.label_cadastro_titulo_cad_clientes = QtWidgets.QLabel(self.widget_cadastro_usuarios)
        self.label_cadastro_titulo_cad_clientes.setGeometry(QtCore.QRect(10, 100, 401, 51))
        self.label_cadastro_titulo_cad_clientes.setStyleSheet("font: 75 8pt \"Verdana\";\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.label_cadastro_titulo_cad_clientes.setObjectName("label_cadastro_titulo_cad_clientes")
        self.pushButton_cadastro_cadastrar = QtWidgets.QPushButton(self.widget_cadastro_usuarios)


        self.pushButton_cadastro_cadastrar.clicked.connect(self.cad_usuarios)

        self.pushButton_cadastro_cadastrar.setGeometry(QtCore.QRect(144, 460, 111, 41))
        self.pushButton_cadastro_cadastrar.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.pushButton_cadastro_cadastrar.setObjectName("pushButton_cadastro_cadastrar")
        self.label_cadastro_pergunta = QtWidgets.QLabel(self.widget_cadastro_usuarios)
        self.label_cadastro_pergunta.setGeometry(QtCore.QRect(180, 30, 121, 20))
        self.label_cadastro_pergunta.setStyleSheet("background-color: transparent;")
        self.label_cadastro_pergunta.setObjectName("label_cadastro_pergunta")
        self.pushButton_cadastro_entre = QtWidgets.QPushButton(self.widget_cadastro_usuarios)
        self.pushButton_cadastro_entre.setGeometry(QtCore.QRect(310, 30, 75, 23))
        self.pushButton_cadastro_entre.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_cadastro_entre.setObjectName("pushButton_cadastro_entre")
        self.widget_login = QtWidgets.QWidget(self.widget_cadastro_usuarios)
        self.widget_login.setGeometry(QtCore.QRect(10, 0, 401, 621))
        self.widget_login.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_login.setObjectName("widget_login")
        self.label_login_titulo_clientes = QtWidgets.QLabel(self.widget_login)
        self.label_login_titulo_clientes.setGeometry(QtCore.QRect(0, 100, 401, 51))
        self.label_login_titulo_clientes.setStyleSheet("font: 75 8pt \"Verdana\";\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.label_login_titulo_clientes.setObjectName("label_login_titulo_clientes")
        self.label_login_pergunta = QtWidgets.QLabel(self.widget_login)
        self.label_login_pergunta.setGeometry(QtCore.QRect(170, 30, 131, 20))
        self.label_login_pergunta.setStyleSheet("background-color: transparent;")
        self.label_login_pergunta.setObjectName("label_login_pergunta")
        self.pushButton_login_crie = QtWidgets.QPushButton(self.widget_login)
        self.pushButton_login_crie.setGeometry(QtCore.QRect(310, 30, 75, 23))
        self.pushButton_login_crie.setStyleSheet("border-radius: 5px;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_login_crie.setObjectName("pushButton_login_crie")
        self.label_login_usuario = QtWidgets.QLabel(self.widget_login)
        self.label_login_usuario.setGeometry(QtCore.QRect(60, 200, 81, 31))
        self.label_login_usuario.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Sitka\";\n"
"")
        self.label_login_usuario.setObjectName("label_login_usuario")
        self.lineEdit_login_usuario = QtWidgets.QLineEdit(self.widget_login)
        self.lineEdit_login_usuario.setGeometry(QtCore.QRect(150, 200, 181, 41))
        self.lineEdit_login_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding: 5px;")
        self.lineEdit_login_usuario.setObjectName("lineEdit_login_usuario")
        self.label_login_senha = QtWidgets.QLabel(self.widget_login)
        self.label_login_senha.setGeometry(QtCore.QRect(80, 270, 61, 31))
        self.label_login_senha.setStyleSheet("background-color: transparent;\n"
"font: 12pt \"Sitka\";\n"
"")
        self.label_login_senha.setObjectName("label_login_senha")
        self.lineEdit_login_senha = QtWidgets.QLineEdit(self.widget_login)

        self.lineEdit_login_senha.setEchoMode(QLineEdit.Password)

        self.lineEdit_login_senha.setGeometry(QtCore.QRect(150, 270, 181, 41))
        self.lineEdit_login_senha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding: 5px;")
        self.lineEdit_login_senha.setObjectName("lineEdit_login_senha")
        self.pushButton_login_logar = QtWidgets.QPushButton(self.widget_login)
        self.pushButton_login_logar.setGeometry(QtCore.QRect(150, 360, 111, 41))
        self.pushButton_login_logar.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.pushButton_login_logar.setObjectName("pushButton_login_logar")
        self.label_parte_fixa = QtWidgets.QLabel(self.centralwidget)
        self.label_parte_fixa.setGeometry(QtCore.QRect(-4, -10, 401, 621))
        self.label_parte_fixa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_parte_fixa.setText("")
        self.label_parte_fixa.setScaledContents(False)
        self.label_parte_fixa.setObjectName("label_parte_fixa")
        self.label_titulo_fixo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo_fixo.setGeometry(QtCore.QRect(10, 20, 381, 61))
        self.label_titulo_fixo.setStyleSheet("font: 75 8pt \"Sitka Heading\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_titulo_fixo.setObjectName("label_titulo_fixo")
        self.label_subtitulo_fixo = QtWidgets.QLabel(self.centralwidget)
        self.label_subtitulo_fixo.setGeometry(QtCore.QRect(60, 60, 251, 21))
        self.label_subtitulo_fixo.setStyleSheet("font: 75 8pt \"Sitka Heading\";")
        self.label_subtitulo_fixo.setObjectName("label_subtitulo_fixo")
        self.label_imagem_fixa = QtWidgets.QLabel(self.centralwidget)
        self.label_imagem_fixa.setGeometry(QtCore.QRect(40, 100, 301, 281))
        self.label_imagem_fixa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_imagem_fixa.setText("")
        self.label_imagem_fixa.setPixmap(QtGui.QPixmap("Telas/Imagens/xilo_fixa.jpg"))
        self.label_imagem_fixa.setScaledContents(True)
        self.label_imagem_fixa.setObjectName("label_imagem_fixa")
        self.label_descricao_fixa = QtWidgets.QLabel(self.centralwidget)
        self.label_descricao_fixa.setGeometry(QtCore.QRect(0, 400, 391, 31))
        self.label_descricao_fixa.setStyleSheet("font: 75 11pt \"Nirmala UI\";")
        self.label_descricao_fixa.setObjectName("label_descricao_fixa")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_login_crie.clicked.connect(self.transparencia1)
        self.pushButton_cadastro_entre.clicked.connect(self.transparencia2)
        self.pushButton_login_crie.clicked.connect(self.transparencia3)
        self.pushButton_cadastro_entre.clicked.connect(self.transparencia4)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FOGO DE RIBA - ACESSO"))
        self.label_cadastro_usuario.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Arretado:</span></p></body></html>"))
        self.label_cadastro_email.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">E-mail:</span></p></body></html>"))
        self.label_cadastro_telefone.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Telefone:</span></p></body></html>"))
        self.label_cadastro_senha.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Senha:</span></p></body></html>"))
        self.label_cadastro_titulo_cad_clientes.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">CRIE SUA CONTA</span></p></body></html>"))
        self.pushButton_cadastro_cadastrar.setText(_translate("MainWindow", "CRIAR"))
        self.label_cadastro_pergunta.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; font-style:italic; color:#ffffff;\">Já tem uma conta?</span></p></body></html>"))
        self.pushButton_cadastro_entre.setText(_translate("MainWindow", "ENTRAR"))
        self.label_login_titulo_clientes.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">ACESSE SUA CONTA</span></p></body></html>"))
        self.label_login_pergunta.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; font-style:italic; color:#ffffff;\">Não tem uma conta?</span></p></body></html>"))
        self.pushButton_login_crie.setText(_translate("MainWindow", "CRIAR"))
        self.label_login_usuario.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Arretado:</span></p></body></html>"))
        self.label_login_senha.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Senha:</span></p></body></html>"))
        self.pushButton_login_logar.setText(_translate("MainWindow", "ENTRAR"))
        self.label_titulo_fixo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#000000;\">RESTAURANTE FOGO DE RIBA</span></p></body></html>"))
        self.label_subtitulo_fixo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Fogo de Riba no Fogão, Calor no Coração</span></p></body></html>"))
        self.label_descricao_fixa.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">O Melhor da Comida Regional Você Encontra Aqui!</span></p></body></html>"))

    def transparencia1(self):
        self.widget_login.setVisible(False)

    def transparencia2(self):
        self.widget_login.setVisible(True)

    def transparencia3(self):
        self.widget_cadastro_usuarios.setVisible(True)

    def transparencia4(self):
        self.widget_cadastro_usuarios.setVisible(True)

    def criardb():
        con = db.connect("usuarios.db")
        cursor = con.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        senha TEXT NOT NULL     
       
    )
        ''')

    def cad_usuarios(self):
        con = db.connect("usuarios.db")
        cursor = con.cursor()
        nome = self.lineEdit_cadastro_usuario.text()
        email = self.lineEdit_cadastro_email.text()
        telefone = self.lineEdit_cadastro_telefone.text()
        senha = self.lineEdit_cadastro_senha.text()

        if nome == "" or email == "" or telefone == "" or senha == "":
            msg = QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText("O CADASTRO POSSUI CAMPO(S) VAZIO(S)!")
            msg.exec_()

        else:
            cmd = "INSERT INTO usuarios values (null, ?, ?, ?, ?)"
            cursor.execute(cmd, (nome,email,telefone,senha))
            con.commit()

            msg = QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText("CADASTRADO COM SUCESSO!")
            msg.exec_()

            self.limpar()
            cursor.close()
            con.close()


    def limpar(self):
        self.lineEdit_cadastro_usuario.setText("")
        self.lineEdit_cadastro_email.setText("")
        self.self.lineEdit_cadastro_telefone.setText("")
        self.lineEdit_cadastro_senha.setText("")

    criardb()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TelaLoginCadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
