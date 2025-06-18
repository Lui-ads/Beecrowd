# Duas Notas

okay = [2, 5, 10, 20, 50, 100]

while True:
    n1, n2 = map(int, input().split())
    if n1 == 0 and n2 == 0:
        break
    if n1 < n2 and n2 <= 10000:
        t = n2 - n1
        possible = False
        for i in range(len(okay)):
            for j in range(len(okay)):
                if okay[i] + okay[j] == t:
                    possible = True
                    break
            if possible:
                break
        print("possible" if possible else "impossible")
    else:
        print("impossible")