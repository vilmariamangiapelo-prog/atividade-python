idade_dias = int(input("Digite sua idade em dias: "))

anos = idade_dias // 365
resto = idade_dias % 365

meses = resto // 30
dias = resto % 30

print("Idade:", anos, "anos,", meses, "meses e", dias, "dias")
