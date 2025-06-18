# Crescente e Decrescente
while True:
    a, b = map(int, input().split())
    if a == b:
            break
    elif a < b:
        print("Crescente")
    else:
        print("Decrescente")