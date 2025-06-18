# Números Ímpares
valor=int(input())
lista=[]
for i in range (1, valor + 1):
    if i%2!=0 and i not in lista:
        lista.append(i)
for numero in lista:
    print(numero)
    