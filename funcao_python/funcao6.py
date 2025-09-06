def media(*numeros):
  
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

resultado3 = media(10, 20, 30)
print(f"Média de 3 valores (10, 20, 30): {resultado3}")

resultado5 = media(5, 10, 15, 20, 25)
print(f"Média de 5 valores (5, 10, 15, 20, 25): {resultado5}")

resultado7 = media(1, 2, 3, 4, 5, 6, 7)
print(f"Média de 7 valores (1, 2, 3, 4, 5, 6, 7): {resultado7}")