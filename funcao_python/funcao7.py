def dados_pessoais(**kwargs):
   
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="Jennifer", idade=27, cidade="olinda")