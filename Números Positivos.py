# Números Positivos

a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
lista1=[a, b, c, e, f]
lista2=[]
for numero in lista1:
    if numero >=0:
        lista2.append(numero)
final=len(lista2)
print("%d"%final, "valores positivos")