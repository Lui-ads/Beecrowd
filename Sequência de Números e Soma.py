# Sequência de Números e Soma

while True:
    try:
        entrada = input()
        if not entrada:
            continue
        valores = entrada.strip().split()
        if len(valores) < 2:
            continue
        m, n = map(int, valores)
        if m <= 0 or n <= 0:
            break
        menor = min(m, n)
        maior = max(m, n)
        sequencia = list(range(menor, maior + 1))
        soma = sum(sequencia)
        print(' '.join(map(str, sequencia)), f'Sum={soma}')
    except EOFError:
        break