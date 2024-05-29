# Define a função contaDigito para contar o número de dígitos em um número inteiro
def contaDigito(n):
    return len(str(n))  # Converte o número para uma string e retorna o comprimento da string

# Define a função exibe para solicitar um número inteiro ao usuário e exibir o número de dígitos
def exibe():
    n = int(input('Forneça um inteiro: '))  # Solicita um número inteiro ao usuário
    print(contaDigito(n), 'dígitos')         # Chama a função contaDigito para contar os dígitos do número fornecido

# Chama a função exibe para solicitar um número ao usuário e exibir o número de dígitos
exibe()

