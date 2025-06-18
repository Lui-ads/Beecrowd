# Binary/Hexadecimal Number Systems

def isPowerOfTwo(n: int) -> bool:

    return (n > 0) and ((n & (n - 1)) == 0)

try:
    num = int(input())
    
    if isPowerOfTwo(num):
        print("true")
    else:
        print("false")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")