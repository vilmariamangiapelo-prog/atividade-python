import math

a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Os valores devem ser positivos.")

elif a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2

    area = math.sqrt(s * (s-a) * (s-b) * (s-c))

    print("Os valores formam um triangulo.")
    print("Area:", area)

else:
    print("Os valores nao formam um triangulo:")
    print(a, b, c)
