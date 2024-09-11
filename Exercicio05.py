def inverter_string(palavra):
    n = len(palavra)
    while n > 0:
        print(palavra[n-1], end="")
        n-=1



palavra = str(input("Digite uma palavra: "))
inverter_string(palavra)
