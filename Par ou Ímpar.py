# Par ou Ímpar

v=int(input())

if 0<v<=10000:
    for i in range(v):
        n=int(input())
        if n<0 and n%2==0:
            print("EVEN NEGATIVE")
        elif n<0 and n%2!=0:
            print("ODD NEGATIVE")
        elif n>0 and n%2 ==0:
            print("EVEN POSITIVE")
        elif n>0 and n%2 !=0:
            print("ODD POSITIVE")
        else:
            print("NULL")

else:
    print("Erro")
