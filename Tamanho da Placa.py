# Tamanho da Placa

while True:
    try:
        v1, v2, v3 = map(int, input().split())       
        for i in range(v3):
            d1, d2 = map(int, input().split())
            
            if (d1 <= v1 and d2 <= v2) or (d2 <= v1 and d1 <= v2):
                print("Sim")
            else:
                print("Nao")
    except EOFError:
        break