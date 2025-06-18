# Magic and Sword

# Fiz com ajuda

import math

def magia_dano(magia: str) -> int:
    match magia:
        case "fire":
            return 200
        case "water":
            return 300
        case "earth":
            return 400
        case _:
            return 100

def magia_raio(magia: str, lv: str) -> int:
    match (magia, lv):
        case ("fire", "1"):
            return 20
        case ("fire", "2"):
            return 30
        case ("fire", "3"):
            return 50
        case ("water", "1"):
            return 10
        case ("water", "2"):
            return 25
        case ("water", "3"):
            return 40
        case ("earth", "1"):
            return 25
        case ("earth", "2"):
            return 55
        case ("earth", "3"):
            return 70
        case ("air", "1"):
            return 18
        case ("air", "2"):
            return 38
        case _:
            return 60

def intercessao(cx: int, cy: int, raio: int, 
               rx: int, ry: int, 
               largura: int, altura: int) -> bool:
    cDx = abs(cx - (rx + largura / 2))
    cDy = abs(cy - (ry + altura / 2))

    if (cDx > (largura / 2 + raio)) or (cDy > (altura / 2 + raio)):
        return False
    elif (cDx <= largura / 2) or (cDy <= altura / 2):
        return True
    else:
        return ((cDx - largura/2)**2 + (cDy - altura/2)**2) <= raio**2

t = int(input())
for _ in range(t):
    posicao = list(map(int, input().split()))
    w, h, x0, y0 = posicao[0], posicao[1], posicao[2], posicao[3]
    ataque = input().split()
    magia, lv = ataque[0], ataque[1]
    cx, cy = int(ataque[2]), int(ataque[3])

    if intercessao(cx, cy, magia_raio(magia, lv), x0, y0, w, h):
        print(magia_dano(magia))
    else:
        print(0)