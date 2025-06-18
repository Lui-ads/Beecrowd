# Preenchimento de Vetor IV

# Fiz com ajuda

inpar = []
par = []
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
        if len(par) == 5:
            for j in range(5):
                print(f"par[{j}] = {par[j]}")
            par = []
    else:
        inpar.append(n)
        if len(inpar) == 5:
            for j in range(5):
                print(f"impar[{j}] = {inpar[j]}")
            inpar = []

for j in range(len(inpar)):
    print(f"impar[{j}] = {inpar[j]}")
for j in range(len(par)):
    print(f"par[{j}] = {par[j]}")
