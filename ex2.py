'''
Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
'''


def verificar_letra_a(string):
    # Converte toda a string para minúsculas
    string_lower = string.lower()
    
    # Conta o número de vezes que 'a' ocorre
    ocorrencias = string_lower.count('a')
    
    # Verifica se a letra 'a' está presente
    if ocorrencias > 0:
        return f"A letra 'a' aparece {ocorrencias} vezes na string."
    else:
        return "A letra 'a' não está presente na string."


texto = input("Digite uma string: ")

# Para previamente definir o texto no código, basta comentar a linha de cima com '#', trocar a variável texto por uma string 'exemplo'
resultado = verificar_letra_a(texto)
print(resultado)
