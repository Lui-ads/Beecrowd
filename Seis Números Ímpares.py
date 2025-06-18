# Seis Números Ímpares
lista=[]
n=int(input())

if n%2==0:
    lista.append(n+1)
    lista.append(n+3)
    lista.append(n+5)
    lista.append(n+7)
    lista.append(n+9)
    lista.append(n+11)
elif n%2!=0:
    lista.append(n)
    lista.append(n+2)
    lista.append(n+4)
    lista.append(n+6)
    lista.append(n+8)
    lista.append(n+10)
else:
    print("erro")

for numero in lista:
    print(numero)
