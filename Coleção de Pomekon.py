# Coleção de Pomekon
nomes=set()
n=int(input())
for i in range(n):
# set(), tem a função de ajudar a não repetir nomes/números
    pokemon=input().strip()
    nomes.add(pokemon)
final=151-len(nomes)
print("Falta(m)", "%d"%final, "pomekon(s).")

