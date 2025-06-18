# Acima da Diagonal Principal

operacao=input().strip()  

soma=0.0
elementos=0

for k in range(144): 
    valor=float(input())
    i=k//12      
    j=k % 12      
    if j>i:       
        soma+=valor
        elementos+=1

if operacao=='M':
    resultado=soma/elementos
else:
    resultado=soma

print("{0:.1f}".format(resultado))