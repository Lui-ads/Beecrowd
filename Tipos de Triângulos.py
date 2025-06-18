# Tipos de Triângulos

n1, n2, n3=sorted(map(float, input().split()), reverse=True)

if n1>=n2+n3:
    print("NAO FORMA TRIANGULO")
else:

    if n1**2==n2**2 + n3**2:
        print("TRIANGULO RETANGULO")
    elif n1**2>n2**2+n3**2:

        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
    
    if n1==n2==n3:
        print("TRIANGULO EQUILATERO")
    elif n1==n2 or n2==n3 or n1==n3:
        print("TRIANGULO ISOSCELES")
