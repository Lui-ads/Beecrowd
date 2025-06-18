# Máquina de Verificação Automatizada

e1 = list(map(int, input().split()))
e2 = list(map(int, input().split()))

# Mudei a estrutura (como pedido), porém usei a mesma lógica :)

if e1[0]!=e2[0] and e1[1]!=e2[1] and e1[2]!=e2[2] and e1[3]!=e2[3] and e1[4]!=e2[4]:
    final="Y"
else:
    final="N"
print(final)