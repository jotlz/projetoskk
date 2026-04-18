def caixa_registradora():
    precos = {
    1 : 0.50,
    2 : 1.00,
    3 : 4.00,
    5 : 7.00,
    9 : 8.00}
    
    total=0.0

    while True:
        print("---------------------------------------------------------------")
        print("Ex:\n1 - Balinha \n2 - Caneta \n3 - Caderneta \n5 - Cola Bastão \n9 - Láspis de Cor \n0 - Encerrar Programa!")
        print("---------------------------------------------------------------")

        codigo_produto = int(input("Digite aqui o código do produto: "))
        if codigo_produto == 0:
            break

        if codigo_produto not in precos:
            print("Código inválido! \nTente Novamente!")
            continue

        quant_produto = int(input("Digite aqui a quantidade do produto: "))
        
        subtotal = precos[codigo_produto]*quant_produto
        total+=subtotal
    print("---------------------------------------------------------------")
    print(f"O total da compra foi de: R$ {total:.2f} ")
caixa_registradora()