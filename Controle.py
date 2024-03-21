import sqlite3
import os
from tabulate import tabulate
import msvcrt
from prettytable import PrettyTable
import time
from datetime import datetime
import sys
class MyProgram:
    def __init__(self):
        pass

    def getch():
        return msvcrt.getch().decode('utf-8')
    
    
    
    def criar_tabela_dia_data(self):
        conn = sqlite3.connect('vendas.db')
        cursor = conn.cursor()

        try:
            # Obtém a data atual
            data_atual = datetime.now().strftime("%d_%m_%Y")

            # Nome da tabela baseado na data atual
            nome_tabela = f"dia_{data_atual.replace('-', '_')}"

            # Verifica se a tabela já existe
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))
            tabela_existe = cursor.fetchone()

            if not tabela_existe:
                # Cria a tabela se ela não existir
                cursor.execute(f'''CREATE TABLE {nome_tabela} (
                                    id codigo INTEGER,
                                    produto INTEGER,
                                    quantidade INTEGER,
                                    valor Real,
                                    Total REAL
                                )''')
                print(f"Tabela '{nome_tabela}' criada com sucesso!")
            else:
                print(f"A tabela '{nome_tabela}' já existe.")
        except sqlite3.Error as e:
            print("Erro ao criar tabela:", e)
        finally:
            conn.close()
    
    def menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')

       
       
        menu = """ ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗ ██╗     ███████╗
██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║     ██╔════╝
██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     █████╗  
██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║     ██╔══╝  
╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗███████╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
  Cliente: H%T                                        Contato: chasealdorobert@gmail.com   (21)96455-8805 
    
    
    
    Selecione A opção:
    1-Cadastrar Produtos
    2-Ver Produtos
    3-Deletar Produtos
    4-Vender Produto
    5-Total Vendas
    6-Sair

    Escolha: """
        print(menu)

        print('Selecione sua Opção: ', end='', flush=True)
        op = int(msvcrt.getch().decode('utf-8')) # Converter para inteiro

        if op == 1:
            self.cadastro()
        elif op== 2:
            self.lista()
        elif op == 3:
            self.deletar()
        elif op == 4:
            self.vender()
        elif op == 5:
            self.total()
        elif op == 6:
            self.sair()

    def cadastro(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        
        menu1 = """  ██████╗ █████╗ ██████╗  █████╗ ███████╗████████╗██████╗  ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗
██║     ███████║██║  ██║███████║███████╗   ██║   ██████╔╝██║   ██║
██║     ██╔══██║██║  ██║██╔══██║╚════██║   ██║   ██╔══██╗██║   ██║
╚██████╗██║  ██║██████╔╝██║  ██║███████║   ██║   ██║  ██║╚██████╔╝
 ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 
 """
        
        
        
        print(menu1)
        cod = input('Codigo do Produto: ')
        print(cod)
        desc = input('Descrição: ')
        print(desc)
        valor = input('Valor? ')
        print(valor)
        total = input('Quantidade: ')
        print(total)
        os.system('cls' if os.name == 'nt' else 'clear')


        print(menu1)
        print(f'esta correto? \nCodigo: {cod}\nProduto: {desc}\nValor: {valor}\nQuantidade:{total} ')
        print('S ou N?', end='', flush=True)
        c = (msvcrt.getch().decode('utf-8'))  # Converter para maiúsculas
        if c.lower() == 's':
            connection = sqlite3.connect('vendas.db')
            cursor = connection.cursor()

            # Selecionar todos os dados da tabela Produtos
            cursor.execute("SELECT * FROM Produtos")
            dados = cursor.fetchall()
            cursor.execute("INSERT INTO Produtos (codigo, produto, quantidade, valor) VALUES (?, ?, ?, ?)",
               (cod, desc, total, valor))

            # Salvar (commit) as mudanças
            connection.commit()
            # Fechar a conexão
            dados = cursor.fetchall()


                # Exiba os dados (apenas para verificação)
            print('Cadastrado com Sucesso!')
            time.sleep(3)
            self.listaa()
                
                
                
            self.menu()
        else:
            self.cadastro()
         
    
    def deletar(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        menu2 = """
██████╗ ███████╗██╗     ███████╗████████╗ █████╗ ██████╗ 
██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
██║  ██║█████╗  ██║     █████╗     ██║   ███████║██████╔╝
██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══██║██╔══██╗
██████╔╝███████╗███████╗███████╗   ██║   ██║  ██║██║  ██║
╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
                                                         
                                                                    
 """
        
        print(menu2)
        connection = sqlite3.connect('vendas.db')
        cursor = connection.cursor()

        # Selecionar todos os dados da tabela Produtos
        cursor.execute("SELECT * FROM Produtos")
        dados = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["ID", "Nome", "Preço", "Quantidade"]

# Adicionar linhas à tabela com os dados recuperados
        for row in dados:
            table.add_row(row)

        # Exibir a tabela no terminal
        print(table)
        delet=input('Insira ID para deletar ou Sair para sair: ')


        if delet.lower() == 'sair':
            os.system('cls' if os.name == 'nt' else 'clear')
            self.menu()
        else:
            #delet= int(delet)
            connection = sqlite3.connect('vendas.db')
            cursor = connection.cursor()

            # Selecionar todos os dados da tabela Produtos
            cursor.execute("SELECT * FROM Produtos")
            dados = cursor.fetchall()
            cursor.execute("DELETE FROM Produtos WHERE codigo = ?", (delet,))
               

            # Salvar (commit) as mudanças
            connection.commit()
            # Fechar a conexão
            connection.close()
            

                # Exiba os dados (apenas para verificação)
            print('Deletado')
            self.listaa()

        
        
        pass  # Coloque a lógica para vender produtos aqui

    def vender(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.criar_tabela_dia_data()
        menu2 = """██╗   ██╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██║   ██║██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║   ██║█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
 ╚████╔╝ ███████╗██║ ╚████║██████╔╝███████╗██║  ██║
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝ 
 """
        
        print(menu2)
        

        self.vends()
        print(f'Total: {self.a_total()}')
        produto=input('Selecione codigo do produto: ')
        # Conecta-se ao banco de dados SQLite
        conn = sqlite3.connect('vendas.db')
        cursor = conn.cursor()

        # Seleciona a linha da TabelaOrigem com o código especificado
        cursor.execute("SELECT * FROM produtos WHERE codigo = ?", (produto,))
        linha_origem = cursor.fetchone()

        # Verifica se a linha foi encontrada
        if linha_origem:
            # Insere a linha da tabela 'produtos' na tabela 'vendas'
            cursor.execute("INSERT INTO vendas (codigo, produto, quantidade, valor) VALUES (?, ?, ?, ?)", (linha_origem[0], linha_origem[1], 1, linha_origem[3]))

            # Deleta a linha da tabela 'produtos' se desejado
            # cursor.execute("DELETE FROM produtos WHERE codigo = ?", (linha_origem[0],))

            # Commit das alterações
            conn.commit()
        else:
            print("A linha não foi encontrada.")


            # Fecha a conexão com o banco de dados
            conn.close()


        # Seleciona todos os dados da tabela produtos
        
        conn = sqlite3.connect('vendas.db')
        cursor = conn.cursor()

        # Seleciona a linha da TabelaOrigem com o código especificado
        cursor.execute("SELECT * FROM vendas")
        alinha_origem = cursor.fetchall()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(menu2)

        print('Produtos no carrinho:')
        table = PrettyTable()
        table.field_names = ["ID", "Nome", "Quantidade", "Preço"]

# Adicionar linhas à tabela com os dados recuperados
        for row in alinha_origem:
            table.add_row(row)

        # Exibir a tabela no terminal
        print(table)
        cursor.execute("SELECT * FROM produtos")
        linha_origem = cursor.fetchone()


        # Recupera e imprime os resultados em linhas separadas

        #print(linha_origem)

        cursor.execute("SELECT valor FROM vendas")

        # Inicializa a variável de soma

        soma= 0
        # Itera sobre os resultados e calcula a soma
        for linha in cursor.fetchall():
            soma += linha[0]  # Adiciona o valor da quarta coluna à soma

        # Converte a soma para uma string
        soma_string = str(soma)

        # Imprime a soma como uma string
        print("\033[1;34mTotal:\033[0m", soma_string)  # O código 34 define a cor da fonte como azul
        self.adicionar_total(soma_string)
            # Fecha a conexão
        conn.close()
        print('1-Adicionar mais produtos \n2-Finalizar Venda \n3-Limpar Lista \n4-Cancelar: ', end='', flush=True)
        c = (msvcrt.getch().decode('utf-8'))  # Converter para maiúsculas
        if c == '1':
            self.vender()
        
        if c=='2':
            data_atual = datetime.now().strftime("%d_%m_%Y")
            ssoma = 0
            # Nome da tabela baseado na data atual
            nome_tabela = f"dia_{data_atual.replace('-', '_')}"

            conn = sqlite3.connect('vendas.db')
            cursor = conn.cursor()

            # Seleciona todos os dados da tabela produtos
            cursor.execute("SELECT * FROM produtos")
            linhas_origem = cursor.fetchall()  # Obtém todas as linhas da tabela

            # Insere todas as linhas na tabela baseada na data atual
            for linha in linhas_origem:
                cursor.execute(f"INSERT INTO {nome_tabela} (id, produto, quantidade, valor) VALUES (?, ?, ?, ?)", linha)
                conn.commit()

            # Seleciona a coluna 'valor' da tabela baseada na data atual
            cursor.execute(f"SELECT valor FROM vendas")

            # Itera sobre os resultados e calcula a soma
            for linha in cursor.fetchall():
                print("Valor recuperado:", linha[0])
                if linha[0] is not None:  # Verifica se o valor não é None
                    ssoma += int(linha[0])  # Adiciona o valor da quarta coluna à soma
                else:
                    print("Valor nulo encontrado, pulando esta linha.")

            # Converte a soma para uma string
            ssoma_string = str(ssoma)

            # Atualiza a coluna 'Total' para NULL
            #cursor.execute(f"UPDATE {nome_tabela} SET Total = NULL")

            # Insere o valor da soma na coluna 'Total'
            cursor.execute(f"UPDATE {nome_tabela} SET Total = Total + ? WHERE rowid = 1", (ssoma_string,))
            conn.commit()

            # Fecha a conexão
            conn.close()
            self.adicionar_total(0)
            conn = sqlite3.connect('vendas.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM vendas")
            conn.commit()
            conn.close()
            self.menu()            




            

        if c =='3':
            self.adicionar_total(0)
            conn = sqlite3.connect('vendas.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM vendas")
            conn.commit()
            conn.close()
            self.vender()


        if c=='4':
            self.adicionar_total(0)
            conn = sqlite3.connect('vendas.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM vendas")
            conn.commit()
            conn.close()
            self.menu()
    def total(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        menu2 = """
████████╗ ██████╗ ████████╗ █████╗ ██╗     
╚══██╔══╝██╔═══██╗╚══██╔══╝██╔══██╗██║     
   ██║   ██║   ██║   ██║   ███████║██║     
   ██║   ██║   ██║   ██║   ██╔══██║██║     
   ██║   ╚██████╔╝   ██║   ██║  ██║███████╗
   ╚═╝    ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝
                                           
                                                         
                                                                    
 """
        
        print(menu2)
        # Conecta-se ao banco de dados
        conn = sqlite3.connect('vendas.db')

        # Cria um cursor para executar comandos SQL
        cursor = conn.cursor()

        try:
            # Obtém os nomes de todas as tabelas do banco de dados
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tabelas = cursor.fetchall()

            # Percorre os nomes das tabelas e mostra os que começam com "dia"
            #print("Tabelas que começam com 'dia':")
            for tabela in tabelas:
                nome_tabela = tabela[0]
                if nome_tabela.startswith("dia"):
                    print(nome_tabela)
        finally:
            # Fecha a conexão com o banco de dados
            #conn.close()
            pass

        table=input('Digite a data para visualizar (ex: 08_04_2004)')
        try:
            # Obtém os nomes de todas as tabelas do banco de dados que contêm a string especificada
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE ?", ('%' + table + '%',))
            tabelas = cursor.fetchall()

            # Percorre os nomes das tabelas que contêm a string especificada
            for tabela in tabelas:
                nome_tabela = tabela[0]
                
                # Carrega a tabela
                cursor.execute(f"SELECT * FROM {nome_tabela}")
                linhas = cursor.fetchall()
                table = PrettyTable()
                table.field_names = ["ID", "Nome", "Quantidade", "Preço", "Total Vendido"]

        # Adicionar linhas à tabela com os dados recuperados
                for row in linhas:
                    table.add_row(row)
                print(table)
        finally:
            # Fecha a conexão com o banco de dados
            conn.close()

        print('1-Escolher novamente \n2-Retornar ao menu: ', end='', flush=True)
        c = (msvcrt.getch().decode('utf-8'))  # Converter para maiúsculas
        if c == '1':
            self.total()
        
        if c=='2':
            self.menu()
                

    def lista(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        menu2 = """██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗████████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║   ██║   ██║   ██║███████╗
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║   ██║   ██║   ██║╚════██║
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝   ██║   ╚██████╔╝███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝
                                                                    
 """
        
        print(menu2)
        connection = sqlite3.connect('vendas.db')
        cursor = connection.cursor()

        # Selecionar todos os dados da tabela Produtos
        cursor.execute("SELECT * FROM Produtos")
        dados = cursor.fetchall()

        # Fechar a conexão
        connection.close()

        table = PrettyTable()
        table.field_names = ["ID", "Nome", "Quantidade", "Preço"]

# Adicionar linhas à tabela com os dados recuperados
        for row in dados:
            table.add_row(row)

        # Exibir a tabela no terminal
        print(table)
        a=input('repetir? S ou N?')
        if a.lower() == 's' or a.lower() == 'sim':
            os.system('cls' if os.name == 'nt' else 'clear')
            self.lista()
        elif a.lower() == 'n' or a.lower() == 'nao':
            self.menu()


    def adicionar_total(self, soma_string):
    
        conn = sqlite3.connect('vendas.db')
        cursor = conn.cursor()

        # Atualiza o valor da coluna 'total' na tabela 'vendas'
        try:
        # Atualiza o valor da coluna 'total' na tabela 'total'
                cursor.execute("DELETE FROM total")

                cursor.execute("INSERT INTO total (total) VALUES (?)", (soma_string,))
            # Commit das alterações e fecha a conexão
                conn.commit()
                print("Total atualizado com sucesso!")
        except sqlite3.Error as e:
            print("Erro ao atualizar total:", e)
        finally:
            conn.close()


    def a_total(self):
        conn = sqlite3.connect('vendas.db')
        cursor = conn.cursor()
        cursor.execute("SELECT total FROM total")
        linha_origem = cursor.fetchone()
        conn.close()
        if linha_origem:
            return linha_origem[0]
        else:
            return 0  # Se não houver nenhum valor na tabela, retorna 0 ou qualqu

    def listaa(self):
        connection = sqlite3.connect('vendas.db')
        cursor = connection.cursor()

        # Selecionar todos os dados da tabela Produtos
        cursor.execute("SELECT * FROM Produtos")
        dados = cursor.fetchall()

        # Fechar a conexão
        connection.close()

        table = PrettyTable()
        table.field_names = ["ID", "Nome", "Quantidade", "Preço"]

# Adicionar linhas à tabela com os dados recuperados
        for row in dados:
            table.add_row(row)

        # Exibir a tabela no terminal
        print(table)
        time.sleep(3)
        self.menu()

    def vends (self):
        connection = sqlite3.connect('vendas.db')
        cursor = connection.cursor()

        # Selecionar todos os dados da tabela Produtos
        cursor.execute("SELECT * FROM Produtos")
        dados = cursor.fetchall()

        # Fechar a conexão
        connection.close()

        table = PrettyTable()
        table.field_names = ["ID", "Nome", "Quantidade", "Preço"]

# Adicionar linhas à tabela com os dados recuperados
        for row in dados:
            table.add_row(row)

        # Exibir a tabela no terminal
        print(table)

    def sair(self):
        sys.exit()

if __name__ == "__main__":
    programa = MyProgram()
    programa.menu()
