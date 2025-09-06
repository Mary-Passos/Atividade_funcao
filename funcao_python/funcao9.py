def aplicar_operacao(a, b, operacao):
    return operacao(a, b)


def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

print(aplicar_operacao(5, 3, soma))          
print(aplicar_operacao(5, 3, multiplicacao)) 
print(aplicar_operacao(10, 2, lambda x, y: x - y)) 
