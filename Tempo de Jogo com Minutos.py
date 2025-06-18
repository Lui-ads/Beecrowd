# Tempo de Jogo com Minutos

# Mínimo 1 minuto máximo 1h

h1, m1, h2, m2 = map(int, input().split())

# Converter tudo para minutos
inicio = (h1 * 60) + m1
fim = (h2 * 60) + m2

# Calcular a duração em minutos
if fim > inicio:
    duracao = fim - inicio
elif fim < inicio:
    duracao = ((24 * 60) - inicio) + fim
else:  # iguais
    duracao = (24 * 60)

# Converter de volta para horas e minutos
horas = duracao // 60
minutos = duracao % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")