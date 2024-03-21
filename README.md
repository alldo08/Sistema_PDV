# Sistema_PDV Versão b0.9vF
Não comercializar sem devida autorização
Se for utilizar ao menos Pague uma cerveja para esse Dev que vos fala: pix 21964558805 (Aldo Roberto de Lima)



Versão beta: Futuras atualizacoes: Funcionamento de reducao de quantidade de produtos, adicionar opcao para troco, Sistema de impressao de itens vendidos. Limpeza e mais simplificação do codigo.
Requisitos import: sqlite3 (gerenciamento banco de dados)
                    os( interação com o S.O)
                    tabulate( Formatação mais amigavel da tabela para ser apresentada em terminal)
                    msvcrt (Utilizado para um menu um pouco mais intuitivo)
                    prettytable( Formatação mais amigavel da tabela SQL para apresentar em terminal)
                    time(Criação tabelas dias e outras automações referente aá datas)
                    datetime ( Ler a cima)
                    sys(Manipulação de arquivos do sistema)


Pequenas explicações de cada função que acho nescessario explicar:
    
    
Cria a tabela que fará o controle do fluxo do caixa do dia:
    def criar_tabela_dia_data(self):
       
Utilizado um menu simples em ASCII e os.system para limpar console não deixando tao confuso para o cliente e usado msvcrt para ao apertar o botao relacionado a opção carregar automaticamente para poupar certo tempo
  def menu(self):
Cadastro dos itens por : Codigo, descricao, valor e quantidade. Com função para limpar o console para melhor visualizacao dos itens, e menu altomatizado.
   def cadastro(self):

Deleta o Item selecionando pelo codigo alem função para limpar o console para melhor visualizacao dos itens, e menu altomatizado.
  def deletar(self): 

Menu de vendas com loop para adição de itens no carrinho(salvo em uma planilha temporaria)
  def vender(self):

Carrega a planilha que o cliente desejar de algum dia que teve vendas e usa o tabulate para formatação
      def total(self):
Mostra lista de itens em formato planilha com o tabulate
  def lista(self):

      
