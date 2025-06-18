# Baú Danificado

a = list(map(int, input().split()))
x, y, z = a[0], a[1], a[2]

if x*x == y*y + z*z:
    area = (y + 3 * z / 4) * z / 2
    print(f"AREA = {int(area)}")
else:
    print("Nao eh retangulo!")
