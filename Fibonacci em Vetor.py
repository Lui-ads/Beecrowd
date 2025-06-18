# Fibonacci em Vetor
t=int(input())
for i in range(t):
# Esse código foi doido de fazer haha
    n=int(input())
    fibonacci = [0, 1]
    for i in range(2, n + 1):
        proximo = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(proximo)
    print(f"Fib({n}) = {fibonacci[n]}")

