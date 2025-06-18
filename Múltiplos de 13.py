# Múltiplos de 13

x = int(input())
y = int(input())

inicio = min(x, y)
fim = max(x, y)

soma = 0
for num in range(inicio, fim + 1):
    if num % 13 != 0:
        soma += num

print(soma)