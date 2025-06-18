# Tomadas Elétricas
n_str=input()
n=int(n_str)
cont=0
soma1=0
final=0
okay=0
if n>=1 and n<=20:
    okay=n
# Esse eu já tinha feito antes, foi só copiar e cola 
else:
    print("Erro1")
for i1 in range(okay):
    l_str=input().split()
    ll=[int(x) for x in l_str]
    k=ll[0]
    k1=ll[1:]
    if 1 <= k <= 10:
        for i in range (k):
            if all(2<=numero<=20 for numero in k1):
                soma=sum(k1)
            else:
                print("Erro2")
            cont+=1
            soma1=soma
            if k>0:
                kk=k-1
            else:
                print("Erro3")
            if soma1<kk:
                final=kk-soma1
            else:
                final=soma1-kk
        
    else:
        print("Erro4")
    print(final)