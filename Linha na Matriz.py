# Linha na Matriz

# Quase não fiz sozinho

linha = int(input())
operacao = input()
matriz = []
for i in range(12):
    linha_matriz = []
    for j in range(12):
        linha_matriz.append(float(input()))
    matriz.append(linha_matriz)

if operacao == 'S':
    soma = sum(matriz[linha])
    print(f"{soma:.1f}")
elif operacao == 'M':
    media = sum(matriz[linha]) / 12
    print(f"{media:.1f}")