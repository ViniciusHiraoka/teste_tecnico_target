'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''


def is_fibonacci(num):
    # Função para gerar a sequência de Fibonacci até um certo número
    def generate_fibonacci_until(n):
        fib_sequence = [0, 1]
        while fib_sequence[-1] < n:
            next_value = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_value)
        return fib_sequence

    # Gera a sequência de Fibonacci até atingir ou ultrapassar o número informado
    fib_sequence = generate_fibonacci_until(num)

    # Verifica se o número informado está na sequência gerada
    if num in fib_sequence:
        return f"{num} pertence à sequência de Fibonacci."
    else:
        return f"{num} não pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))

# Para previamente definir o numero no código, basta comentar a linha de cima com '#', trocar a variável numero por um valor x
resultado = is_fibonacci(numero)
print(resultado)
