# TDA Racional
from math import gcd

start = int(input())
for i in range(start):
    try:
        n1, n, d1, op, n2, n, d2 = input().split()
        
        n1=int(n1)
        d1=int(d1)
        n2=int(n2)
        d2=int(d2)

        if op == "+":
            r1 = (n1*d2)+(n2*d1)
            r2 = d1*d2

        elif op == "-":
            r1 = (n1*d2)-(n2*d1)
            r2 = d1*d2

        elif op == "*":
            r1 = n1*n2
            r2 = d1*d2

        elif op == "/":
            r1 = n1*d2
            r2 = n2*d1

        else:
            print("Ops")
        
        divisor = gcd(abs(r1), abs(r2))
        r11 = r1 // divisor
        r22 = r2 // divisor
    
    except:
        break

    print(f"{r1}/{r2} = {r11}/{r22}")
