# Sequência de Sequência
case = 0
while True:
    try:
        N = int(input())
        case += 1
        
        total_numbers = 1  
        for i in range(1, N + 1):
            total_numbers += i
        
        sequence = []
        sequence.append(0)
        for i in range(1, N + 1):
            sequence.extend([i] * i)
        
        if total_numbers == 1:
            print(f"Caso {case}: {total_numbers} numero")
        else:
            print(f"Caso {case}: {total_numbers} numeros")
        
        print(' '.join(map(str, sequence)))
        print()  
    except EOFError:
        break