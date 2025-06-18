# Sequência Lógica 2

x, y = map(int, input().split())

for i in range(1, y + 1):
    if i % x == 0 or i == y:
        print(i)
    else:
        print(i, end=' ')