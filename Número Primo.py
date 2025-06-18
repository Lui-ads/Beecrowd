# Número Primo

t = int(input())
for _ in range(t):
    n = int(input())
    if n < 2:
        print(f"{n} nao eh primo")
        continue
    primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(f"{n} eh primo")
    else:
        print(f"{n} nao eh primo")