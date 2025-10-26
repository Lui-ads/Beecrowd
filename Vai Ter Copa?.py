# Vai Ter Copa?

while True:
    try:
        n=int(input())
        if 0<=n<=100:
            if n!=0:
                print("vai ter duas!")
            else:
                print("vai ter copa!")    
    except EOFError:
        break