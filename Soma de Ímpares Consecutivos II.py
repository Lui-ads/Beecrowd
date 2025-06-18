# Soma de Ímpares Consecutivos II

n = int(input())
for i in range(n):
    v1, v2 = map(int, input().split())
    mm = min(v1, v2)
    mx = max(v1, v2)
    soma = 0
    for j in range(mm + 1, mx):
        if j % 2 !=0:
            soma+=j
    print(soma)