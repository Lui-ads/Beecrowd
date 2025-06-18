# Área do Círculo

def area (r):
    r2=r*r
    Pi = 3.14159
    area = r2*Pi
    return area
    
r=input()
r=float(r)
result=area(r)
print("A=%.4f" % result)