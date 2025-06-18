# Bem-vindos e Bem-vindas ao Inverno!

d1, d2, d3 = map(int, input().split())

if d2 < d1:
    if d3 >= d2:
        print(":)")
    else:
        if (d2 - d3) < (d1 - d2):
            print(":)")
        else:
            print(":(")
elif d2 > d1:
    if d3 <= d2:
        print(":(")
    else:
        if (d3 - d2) < (d2 - d1):
            print(":(")
        else:
            print(":)")
else:
    if d3 > d2:
        print(":)")
    else:
        print(":(")