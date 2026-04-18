def terceira_lista():
    lista1 = []
    lista2 = []
    lista3 = []
    print("--------------------------------------------------------------------")

    print("DIgite os elementos da 1° Lista (Separe com espaço):")
    primeira_lista = input("1° Lista: ").split()

    print("--------------------------------------------------------------------")
    print("Digite os elementos da 2° Lista (Separe com espaço):")
    segunda_lista =input("2° Lista: ").split()

    lista1 = primeira_lista
    lista2 = segunda_lista
    lista3 = lista1 + lista2

    print("--------------------------------------------------------------------")
    print(f"A primeira lista foi: {lista1}")
    print(f"\nA segunda lista foi: {lista2}")
    print(f"\nA junção das 2 listas é: \n{lista3}")
    print("--------------------------------------------------------------------")
terceira_lista()