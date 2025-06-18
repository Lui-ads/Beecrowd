# Soma de Impares Consecutivos I

v1=int(input())
v2=int(input())

inicio=min(v1, v2)
fim=max(v1,v2)

soma=0

for i in range(inicio +1, fim):
    if i%2!=0:
        soma+=i

print(soma)