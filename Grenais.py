# Grenais

def main():
    grenais = 0
    inter_v = 0
    gremio_v = 0
    empates = 0

    while True:
        try:
            inter, gremio = map(int, input().split())
        except EOFError:
            break

        grenais += 1
        if inter > gremio:
            inter_v += 1
        elif gremio > inter:
            gremio_v += 1
        else:
            empates += 1

        print("Novo grenal (1-sim 2-nao)")
        while True:
            try:
                resposta = int(input())
            except EOFError:
                resposta = 2
            if resposta in (1, 2):
                break
        if resposta == 2:
            break

    print(f"{grenais} grenais")
    print(f"Inter:{inter_v}")
    print(f"Gremio:{gremio_v}")
    print(f"Empates:{empates}")
    if inter_v > gremio_v:
        print("Inter venceu mais")
    elif gremio_v > inter_v:
        print("Gremio venceu mais")
    else:
        print("Nao houve vencedor")

if __name__ == "__main__":
    main()