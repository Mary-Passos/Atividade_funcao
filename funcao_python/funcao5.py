def operacoes(a, b):
    
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    return soma, subtracao, multiplicacao

resultado = operacoes(10, 5)
print(f"Soma: {resultado[0]}, Subtração: {resultado[1]}, Multiplicação: {resultado[2]}")


