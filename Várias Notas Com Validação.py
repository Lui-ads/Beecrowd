# V´árias Notas Com Validação

def ler_nota_valida():
    while True:
        try:
            nota = float(input())
            if 0.0 <= nota <= 10.0:
                return nota
            else:
                print("nota invalida")
        except EOFError:
            exit()
        except:
            print("nota invalida")

def novo_calculo():
    while True:
        print("novo calculo (1-sim 2-nao)")
        try:
            x = int(input())
            if x == 1 or x == 2:
                return x
        except:
            continue

def main():
    while True:
        nota1 = ler_nota_valida()
        nota2 = ler_nota_valida()
        media = (nota1 + nota2) / 2.0
        print(f"media = {media:.2f}")
        if novo_calculo() == 2:
            break

if __name__ == "__main__":
    main()