import hashlib

class SistemaControleUsuarios:
    def __init__(self):
        # Inicializa a estrutura de dados para armazenar os usuários.
        self.usuarios = {}

    def cadastrar_usuario(self, nome, senha, role='usuario'):
        """
        Cadastra um novo usuário no sistema.

        Args:
            nome (str): Nome do usuário.
            senha (str): Senha do usuário.
            role (str): Nível de atribuição do usuário (padrão: 'usuario').

        Returns:
            bool: True se o usuário foi cadastrado com sucesso, False se o nome de usuário já existe.
        """
        # Verifica se o nome de usuário já está em uso.
        if nome in self.usuarios:
            print(f"Erro: O nome de usuário '{nome}' já está em uso.")
            return False

        # Hash da senha para armazenamento seguro.
        hashed_senha = self._hash_senha(senha)

        # Armazena as informações do usuário.
        self.usuarios[nome] = {'senha': hashed_senha, 'role': role}

        print(f"Usuário '{nome}' cadastrado com sucesso.")
        return True

    def verificar_senha(self, nome, senha):
        """
        Verifica se a senha fornecida corresponde à senha cadastrada para o usuário.

        Args:
            nome (str): Nome do usuário.
            senha (str): Senha a ser verificada.

        Returns:
            bool: True se a senha estiver correta, False caso contrário.
        """
        # Verifica se o usuário existe no sistema.
        if nome not in self.usuarios:
            print(f"Erro: Usuário '{nome}' não encontrado.")
            return False

        # Hash da senha fornecida para comparar com a senha armazenada.
        hashed_senha = self._hash_senha(senha)

        # Retorna True se as senhas correspondem, False caso contrário.
        return hashed_senha == self.usuarios[nome]['senha']

    def verificar_atribuicao(self, nome, role):
        """
        Verifica se o usuário possui a atribuição (role) especificada.

        Args:
            nome (str): Nome do usuário.
            role (str): Nível de atribuição a ser verificado.

        Returns:
            bool: True se o usuário possui a atribuição, False caso contrário.
        """
        # Verifica se o usuário existe no sistema.
        if nome not in self.usuarios:
            print(f"Erro: Usuário '{nome}' não encontrado.")
            return False

        # Retorna True se a atribuição do usuário é igual à atribuição fornecida.
        return self.usuarios[nome]['role'] == role

    def _hash_senha(self, senha):
        """
        Função interna para criar o hash da senha.

        Args:
            senha (str): Senha a ser hasheada.

        Returns:
            str: Hash da senha.
        """
        # Utiliza SHA-256 para criar o hash da senha.
        return hashlib.sha256(senha.encode()).hexdigest()

# Exemplo de uso da classe
if __name__ == "__main__":
    sistema = SistemaControleUsuarios()

    # Cadastrando usuários
    sistema.cadastrar_usuario('admin', 'admin@123', role='administrador')
    sistema.cadastrar_usuario('user1', 'user@123')

    # Verificando senhas
    print("Verificando senhas:")
    print(sistema.verificar_senha('admin', 'admin@123'))  # True
    print(sistema.verificar_senha('user1', 'wrong_password'))  # False

    # Verificando atribuições (roles)
    print("\nVerificando atribuições:")
    print(sistema.verificar_atribuicao('admin', 'administrador'))  # True
    print(sistema.verificar_atribuicao('user1', 'administrador'))  # False