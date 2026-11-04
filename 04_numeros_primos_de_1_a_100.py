def eh_primo(numero):
    if numero < 2:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True


for numero in range(1, 101):
    if eh_primo(numero):
        print(numero)
