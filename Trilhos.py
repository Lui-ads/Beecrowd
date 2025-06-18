# Trilhos

while True:
    b=0
    v=int(input())
    while b==0:
        vagoes=list(map(int, input().split()))
        vv=len(vagoes)
        if vagoes[0]==1 or vagoes[-1]==1:
            print("YES")
        elif vagoes[0]!=1 or vagoes[-1]!=1:
            print("NO")
        elif vagoes==0:
            b=1