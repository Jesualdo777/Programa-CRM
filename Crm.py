# Importa a biblioteca mysql.connector para conectar e interagir com um banco de dados MySQL.
import mysql.connector

# Define a classe Cliente com atributos relacionados a um cliente.
class Cliente:
    def __init__(self, nome, email, telefone, endereco, cidade, estado, cep, pais):
        self.nome = nome  # Inicializa o atributo nome.
        self.email = email  # Inicializa o atributo email.
        self.telefone = telefone  # Inicializa o atributo telefone.
        self.endereco = endereco  # Inicializa o atributo endereco.
        self.cidade = cidade  # Inicializa o atributo cidade.
        self.estado = estado  # Inicializa o atributo estado.
        self.cep = cep  # Inicializa o atributo cep.
        self.pais = pais  # Inicializa o atributo pais.

# Define a classe Usuario com atributos relacionados a um usuário do sistema.
class Usuario:
    def __init__(self, nome_usuario, senha, nome, email, papel):
        self.nome_usuario = nome_usuario  # Inicializa o atributo nome_usuario.
        self.senha = senha  # Inicializa o atributo senha.
        self.nome = nome  # Inicializa o atributo nome.
        self.email = email  # Inicializa o atributo email.
        self.papel = papel  # Inicializa o atributo papel.

# Define a classe SistemaCRM que gerencia a conexão com o banco de dados e as operações CRUD.
class SistemaCRM:
    def __init__(self):
        self.conexao = mysql.connector.connect(  # Estabelece uma conexão com o banco de dados MySQL.
            host='localhost',   # Endereço do servidor de banco de dados.
            user='root',        # Nome de usuário para a conexão.
            password='he182555@', # Senha do usuário.
            database='crm_simples' # Nome do banco de dados a ser utilizado.
        )
        self.cursor = self.conexao.cursor()  # Cria um cursor para executar comandos SQL.

    # Método para adicionar um cliente no banco de dados.
    def adicionar_cliente(self, cliente):
        sql = '''
        INSERT INTO clientes (nome, email, telefone, endereco, cidade, estado, cep, pais)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''  # Define o comando SQL para inserir um novo cliente.
        valores = (cliente.nome, cliente.email, cliente.telefone, cliente.endereco, cliente.cidade, cliente.estado, cliente.cep, cliente.pais)  # Cria uma tupla com os valores a serem inseridos.
        self.cursor.execute(sql, valores)  # Executa o comando SQL com os valores fornecidos.
        self.conexao.commit()  # Confirma a transação no banco de dados.
        print('Cliente adicionado com sucesso.')  # Imprime uma mensagem de sucesso.

    # Método para adicionar um usuário no banco de dados.
    def adicionar_usuario(self, usuario):
        sql = '''
        INSERT INTO usuarios (nome_usuario, senha, nome, email, papel)
        VALUES (%s, %s, %s, %s, %s)
        '''  # Define o comando SQL para inserir um novo usuário.
        valores = (usuario.nome_usuario, usuario.senha, usuario.nome, usuario.email, usuario.papel)  # Cria uma tupla com os valores a serem inseridos.
        self.cursor.execute(sql, valores)  # Executa o comando SQL com os valores fornecidos.
        self.conexao.commit()  # Confirma a transação no banco de dados.
        print('Usuário adicionado com sucesso.')  # Imprime uma mensagem de sucesso.

    # Método para listar todos os clientes do banco de dados.
    def listar_clientes(self):
        self.cursor.execute('SELECT * FROM clientes')  # Executa o comando SQL para selecionar todos os clientes.
        clientes = self.cursor.fetchall()  # Recupera todos os resultados da consulta.
        for cliente in clientes:  # Itera sobre cada cliente recuperado.
            print(f'ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}, Telefone: {cliente[3]}, Endereço: {cliente[4]}, Cidade: {cliente[5]}, Estado: {cliente[6]}, CEP: {cliente[7]}, País: {cliente[8]}')  # Imprime os detalhes de cada cliente.

    # Método para listar todos os usuários do banco de dados.
    def listar_usuarios(self):
        self.cursor.execute('SELECT * FROM usuarios')  # Executa o comando SQL para selecionar todos os usuários.
        usuarios = self.cursor.fetchall()  # Recupera todos os resultados da consulta.
        for usuario in usuarios:  # Itera sobre cada usuário recuperado.
            print(f'ID: {usuario[0]}, Nome de Usuário: {usuario[1]}, Nome: {usuario[3]}, Email: {usuario[4]}, Papel: {usuario[5]}')  # Imprime os detalhes de cada usuário.

    # Método para fechar a conexão com o banco de dados.
    def fechar_conexao(self):
        self.cursor.close()  # Fecha o cursor.
        self.conexao.close()  # Fecha a conexão com o banco de dados.

# Função principal para interação com o usuário.
def main():
    sistema_crm = SistemaCRM()  # Cria uma instância do sistema CRM.

    while True:  # Loop infinito para exibir o menu e lidar com as escolhas do usuário.
        print("1. Adicionar Cliente")  # Exibe a opção para adicionar cliente.
        print("2. Adicionar Usuário")  # Exibe a opção para adicionar usuário.
        print("3. Listar Clientes")  # Exibe a opção para listar clientes.
        print("4. Listar Usuários")  # Exibe a opção para listar usuários.
        print("5. Sair")  # Exibe a opção para sair.
        
        escolha = input("Escolha uma opção: ")  # Lê a escolha do usuário.

        if escolha == '1':  # Se a escolha for adicionar cliente.
            nome = input("Nome do Cliente: ")  # Solicita o nome do cliente.
            email = input("Email do Cliente: ")  # Solicita o email do cliente.
            telefone = input("Telefone do Cliente: ")  # Solicita o telefone do cliente.
            endereco = input("Endereço do Cliente: ")  # Solicita o endereço do cliente.
            cidade = input("Cidade do Cliente: ")  # Solicita a cidade do cliente.
            estado = input("Estado do Cliente: ")  # Solicita o estado do cliente.
            cep = input("CEP do Cliente: ")  # Solicita o CEP do cliente.
            pais = input("País do Cliente: ")  # Solicita o país do cliente.

            cliente = Cliente(nome, email, telefone, endereco, cidade, estado, cep, pais)  # Cria uma instância de Cliente com os dados fornecidos.
            sistema_crm.adicionar_cliente(cliente)  # Adiciona o cliente no banco de dados.

        elif escolha == '2':  # Se a escolha for adicionar usuário.
            nome_usuario = input("Nome de Usuário: ")  # Solicita o nome de usuário.
            senha = input("Senha: ")  # Solicita a senha.
            nome = input("Nome: ")  # Solicita o nome.
            email = input("Email: ")  # Solicita o email.
            papel = input("Papel: ")  # Solicita o papel.

            usuario = Usuario(nome_usuario, senha, nome, email, papel)  # Cria uma instância de Usuario com os dados fornecidos.
            sistema_crm.adicionar_usuario(usuario)  # Adiciona o usuário no banco de dados.

        elif escolha == '3':  # Se a escolha for listar clientes.
            sistema_crm.listar_clientes()  # Lista todos os clientes.

        elif escolha == '4':  # Se a escolha for listar usuários.
            sistema_crm.listar_usuarios()  # Lista todos os usuários.

        elif escolha == '5':  # Se a escolha for sair.
            sistema_crm.fechar_conexao()  # Fecha a conexão com o banco de dados.
            print("Sistema encerrado.")  # Informa que o sistema foi encerrado.
            break  # Encerra o loop.

        else:  # Se a escolha for inválida.
            print("Opção inválida, tente novamente.")  # Informa ao usuário que a opção é inválida.

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente (não importado como módulo).
    main()  # Chama a função principal para iniciar o programa.
