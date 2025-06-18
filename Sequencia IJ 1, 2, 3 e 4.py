# Sequencia IJ 1, 2, 3 e 4

# IJ 1
#i = 1
#j = 60
#while j >= 0:
#    print(f"I={i} J={j}")
#    i += 3
#    j -= 5

# IJ 2
#for i in range(1, 10, 2):
#    for j in range(7, 4, -1):
#        print(f"I={i} J={j}")

# IJ 3
#i = 1
#while i <= 9:
#    j = i + 6
#    for _ in range(3):
#        print(f"I={i} J={j}")
#        j -= 1
#    i += 2

# IJ 4
#i = 0.0
#while i <= 2.0001:
#    for j in range(3):
#       x = i
#        y = 1 + j
#        if abs(x - round(x)) < 1e-9:
#            x = int(round(x))
#       if abs((y + i) - round(y + i)) < 1e-9:
#            print(f'I={x} J={int(round(y + i))}')
#        else:
#            print(f'I={x:.1f} J={y + i:.1f}')
#    i += 0.2