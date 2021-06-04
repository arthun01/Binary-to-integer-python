def tudo():

    print("==============================")

    print("     CONVERSOR NÚMEROS/BINÁRIOS")

    print("==============================")
    
    n = int(input("Escreva um número Inteiro: "))
    na = n
    bi = []

    while n > 0:
        bi.append(n%2)
        n = n // 2

    bins = "".join(map(str,bi))
    

    print("O número", na, " em binário é  ", bins[::-1])

    p = str(input("\n Quer repetir? S/N: "))

    if p=="s" or p=="S":
        tudo()
   
tudo()


