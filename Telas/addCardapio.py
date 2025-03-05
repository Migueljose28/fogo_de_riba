import sqlite3 as db

class AddBanco:

    def __init__(self):
            conn = db.connect("cardapio.db")
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS pratos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    categoria TEXT NOT NULL,
                    nome TEXT NOT NULL,
                    descrição TEXT NOT NULL     
            )
                    ''')
  
            conn = db.connect("cardapio.db")
            cursor = conn.cursor()
            categoria = input("degite a categoria: ")
            nome = input("digite o nome do prato novo: ")
            descrição = input("digite a descrição do prato: ")
            cmd = "INSERT INTO pratos VALUES (null,?,?,?)"
           
            cursor.execute(cmd,(categoria, nome, descrição))

            conn.commit()
           
            print("Deu certo")
            cursor.close()
            conn.close()


    def deletar_tabela(self):
            conn = db.connect("cardapio.db")
            cursor = conn.cursor()
            cursor.execute("DROP TABLE pratos")



            conn.commit()
            cursor.close()
            conn.close()
        
    

if __name__ == "__main__":
    banco = AddBanco()
    #banco.deletar_tabela()
    banco()
