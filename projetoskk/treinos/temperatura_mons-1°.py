def mons():
    temperatura = [-10, -8, 0, 1, 2, 5, -2, -4]

    menor = min(temperatura)
    maior = max(temperatura)
    media = sum(temperatura)/len(temperatura)

    print("---------------------------------------")
    print(f"A menor temperatura é: {menor}\n")
    print(f"A maior temperatura é: {maior}\n")
    print(f"A média das temperaturas é: {media}")
    print("---------------------------------------")
mons()