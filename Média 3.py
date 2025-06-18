# Média 3

n1, n2, n3, n4 = map(float, input().split())

n1=n1*2
n2=n2*3
n3=n3*4
n4=n4*1

n5=(n1+n2+n3+n4)/10

print(f"Media: {n5:.1f}")
if n5>=7.0:
    print("Aluno aprovado.")
elif n5<5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    e=float(input())
    print(f"Nota do exame: {e:.1f}")
    en=(n5+e)/2
    if en>=5.0:
        print("Aluno aprovado.")
        print(f"Media final: {en:.1f}")
    elif en<=4.9:
        print("Aluno reprovado.")
        print(f"Media final: {en:.1f}")