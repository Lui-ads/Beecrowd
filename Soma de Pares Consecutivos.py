# Soma de Pares Consecutivos

while True:
    v1 = int(input())
    if v1 == 0:
        break
    
    if v1 % 2 != 0:
        v1 += 1
   
    soma = 0

    for i in range(5):
        soma += v1
        v1 += 2
    
    print(soma)