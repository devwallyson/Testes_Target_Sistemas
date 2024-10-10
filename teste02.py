#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 
#e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
#escreva um programa na linguagem que desejar onde, infoncia de Fibonacci e retorne uma mensagem avisando se 
#o número informado pertence ou não a sequência.rmado um número,
#ele calcule a sequê

def sequencia_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

n = int(input("Informe um número: "))
if sequencia_fibonacci(n):
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} não pertence à sequência de Fibonacci.")
 
