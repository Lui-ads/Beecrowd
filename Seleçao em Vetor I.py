# Seleçao em Vetor I

a = []
for i in range(100):
    valor = float(input())
    a.append(valor)

for i in range(100):
    if a[i] <= 10:
        print(f"A[{i}] = {a[i]:.1f}")