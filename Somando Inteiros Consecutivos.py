# Somando Inteiros Consecutivos

e = list(map(int, input().split()))
a = e[0]
n = 0

for valor in e[1:]:
    if valor > 0:
        n = valor
        break

soma = 0
for i in range(n):
    soma += a + i

print(soma)