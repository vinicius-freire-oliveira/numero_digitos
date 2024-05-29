# Número de dígitos
# Define a função 'inteiros' que recebe um parâmetro 'n'
def inteiros(n):
    # Converte 'n' em uma string, conta o número de caracteres na string e retorna o resultado
    return len((str(n)))

# Pede ao usuário para digitar um número ou uma palavra e remove espaços extras
n = str(input('Digite o número ou a palavra: ')).strip()

# Chama a função 'inteiros' com o valor digitado pelo usuário e imprime o resultado
print(f'Há {inteiros(n)} dígitos')
