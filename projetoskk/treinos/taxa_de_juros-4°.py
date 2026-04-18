def juros():
    while True:
        print("--------------------------------------------------------------------")
        print("POUPANÇA DE 24 MESES")
        deposito = float(input("Digite aqui o valor depositado inicialmente: "))
        if deposito <= 0:
            print("Valor do Depósito não pode ser nulo ou negativo!")
            continue
        taxa_de_juros = float(input("Digite aqui a porcentagem da taxa de juros('%'): "))
        if taxa_de_juros <= 0:
            print("Valor da Taxa de Juros não pode ser nulo ou negativo!")
            continue
        print("--------------------------------------------------------------------")

        montante = 0
        ganho_juros = 0
        i = 1
        while i <= 24:
            montante = deposito*(1+(taxa_de_juros/100))**i
            print(f"Saldo do {i}° mês: {montante:.2f}")
            i+=1
        ganho_juros=montante-deposito
        print("--------------------------------------------------------------------")
        print(f"O Montante Final foi de: R$ {montante:.2f}")
        print(f"\nO Total de Juros foi de: R$ {ganho_juros:.2f}")
        print("--------------------------------------------------------------------")
        break
juros()