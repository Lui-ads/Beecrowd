# Resto da Divisão

v1=int(input())
v2=int(input())

inicio=min(v1, v2)
fim=max(v1, v2)

for num in range(inicio+1, fim):
    if num % 5 == 2 or num % 5 == 3:
        print(num)
        