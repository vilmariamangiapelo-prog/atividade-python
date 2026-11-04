def inverter_palavras(frase):
    palavras = frase.split()

    palavras_invertidas = []

    for palavra in palavras:
        palavras_invertidas.append(palavra[::-1])

    return " ".join(palavras_invertidas)


frase = input("Digite uma frase: ")

resultado = inverter_palavras(frase)

print("Frase com as palavras invertidas:")
print(resultado)
