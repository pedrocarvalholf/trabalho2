# Sistema de Controle de Usuários

Este é um simples sistema de controle de usuários em Python que inclui:

- Cadastro de usuários com verificação de nome de usuário único.
- Hash de senhas para segurança.
- Níveis de atribuição (roles) como "administrador" e "usuário".
- Verificação de senha e atribuições.

## Como Usar

1. Instancie a classe `SistemaControleUsuarios`.
2. Utilize o método `cadastrar_usuario` para adicionar novos usuários.
3. Use `verificar_senha` para verificar senhas e `verificar_atribuicao` para verificar atribuições.

Exemplo de uso:

```python
sistema = SistemaControleUsuarios()

# Cadastrando usuários
sistema.cadastrar_usuario('admin', 'admin@123', role='administrador')
sistema.cadastrar_usuario('user1', 'user@123')

# Verificando senhas
print(sistema.verificar_senha('admin', 'admin@123'))  # True
print(sistema.verificar_senha('user1', 'wrong_password'))  # False

# Verificando atribuições
print(sistema.verificar_atribuicao('admin', 'administrador'))  # True
print(sistema.verificar_atribuicao('user1', 'administrador'))  # False
