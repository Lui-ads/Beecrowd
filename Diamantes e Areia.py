# Diamantes e Areia

n = int(input())
for i in range(n):
    line = input().replace('.', '')
    count = 0
    stack = []
    for char in line:
        if char == '<':
            stack.append(char)
        elif char == '>' and stack and stack[-1] == '<':
            stack.pop()
            count += 1
    print(count)