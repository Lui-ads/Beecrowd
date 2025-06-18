# Ultrapassando Z

x = int(input())
while True:
    z = int(input())
    if z > x:
        break

soma = 0
contador = 0
while soma < z:
    soma += x
    x += 1
    contador += 1

print(contador)