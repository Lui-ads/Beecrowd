# Menor e Posição

n = int(input())
valores = list(map(int, input().split()))
menor = min(valores)
posicao = valores.index(menor)
print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")