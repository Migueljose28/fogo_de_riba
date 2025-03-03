import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from Tela_LoginCadastro import Ui_TelaLoginCadastro as login_cadastro
from Tela_Principal import Ui_TelaPrincipal as principal
from Tela_Pesquisa import Ui_TelaPesquisa as pesquisa
from Tela_Pedidos import Ui_TelaPedidos as pedidos
from Tela_Sobre import Ui_TelaSobre as sobre

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_cadastro = login_cadastro()
        self.principal = principal()
        self.pesquisa = pesquisa()
        self.pedidos = pedidos()
        self.sobre = sobre()
        self.login()

    def login(self): 
        self.ui = self.login_cadastro  # Começa na login_cadastro
        self.ui.setupUi(self)
        self.ui.pushButton_login_logar.clicked.connect(self.verificar)

    #Graças a Deus
    def verificar(self):
            teste = self.login_cadastro.logar()
            if teste:
               self.mudar_para_telaprincipal()
       
        
    def mudar_para_telaPedidos(self):
            self.ui = self.pedidos  # Muda para pedidos
            self.ui.setupUi(self)
            self.ui.pushButton_voltar.clicked.connect(self.mudar_para_telaprincipal)

    def mudar_para_telapesquisa(self):
            self.ui = self.pesquisa # Muda para pesquisar
            self.ui.setupUi(self)
            self.ui.pushButton_voltar.clicked.connect(self.mudar_para_telaprincipal)

            self.ui.pushButton_fazer_pedido.clicked.connect(self.mudar_para_telaPedidos)

    def mudar_para_telaprincipal(self):
            self.ui = self.principal # Muda para principal
            self.ui.setupUi(self)
            self.ui.pushButton_cardapio.clicked.connect(self.mudar_para_telapesquisa)
            self.ui.pushButton_pedidos.clicked.connect(self.mudar_para_telaPedidos)
            #logout
            self.ui.pushButton_fechar.clicked.connect(self.login)
            self.ui.pushButton_sobre.clicked.connect(self.mudar_para_telasobre)

    def mudar_para_telasobre(self):
            self.ui = self.sobre # Muda para sobre
            self.ui.setupUi(self)
            self.ui.pushButton_retornar.clicked.connect(self.mudar_para_telaprincipal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
