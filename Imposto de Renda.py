# Imposto de Renda

r=float(input())
i=0.0

if r<=2000.00:
    print("Isento")
else:
    if r>2000.00:
        faixa1=min(r, 3000.00)-2000.00
        i+=faixa1*0.08
    if r>3000.00:
        faixa2=min(r, 4500.00)-3000.00
        i+=faixa2*0.18
    if r>4500.00:
        faixa3=r-4500.00
        i+=faixa3*0.28
        
    print(f"R$ {i:.2f}")
