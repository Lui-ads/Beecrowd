# Pares, Ímpares, Positivos e Negativos

par=0
impar=0
menos_que_zero=0
mais_que_zero=0

for i in range(5):
    n = int(input())

    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    # -- // --
    
    if n > 0:
        mais_que_zero += 1
    elif n < 0:
        menos_que_zero += 1


print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{mais_que_zero} valor(es) positivo(s)")
print(f"{menos_que_zero} valor(es) negativo(s)")



#-5  3
#0   2
#-3  1
#-4  3
#12



