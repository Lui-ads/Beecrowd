# Dividindo X por Y
a=1
n=int(input())
for i in range(n):
    v1, v2=map(float, input().split())
    try:
        if a==1:
            f=v1/v2
            print
    except:
        print("divisao impossivel")
