def calculadora(operacao, a, b):
    
    def somar(x, y):
        return x + y
    
    def subtrair(x, y):
        return x - y
    
    def multiplicar(x, y):
        return x * y
    
    def dividir(x, y):
        if y == 0:
            return "Erro: Divisão por zero"
        return x / y
    
    operacoes = {
        "somar": somar,
        "subtrair": subtrair,
        "multiplicar": multiplicar,
        "dividir": dividir
    }
    
    if operacao in operacoes:
        return operacoes[operacao](a, b)
    else:
        return "Operação inválida"

print("Soma:", calculadora("somar", 20, 10))      
print("Multiplicação:", calculadora("multiplicar", 6, 7))  