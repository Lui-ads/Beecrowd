# Maior e Posição
lista=[0]
for i in range(100):
    n=int(input())
    lista.append(n)
m=max(lista)
n=lista.index(m)
print(m)
print(n)