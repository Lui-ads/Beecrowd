# Tempo de Jogo

start, end = map(int, input().split())

if start>=end:
    r=(24-start)+end
else:
    r=end-start

print(f"O JOGO DUROU {r} HORA(S)")