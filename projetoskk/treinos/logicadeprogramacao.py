def q1():
    print('=============================\n','[+] Maior e Menor que ')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    soma = a + b
    if soma < c:
        print(f'\n[>] A soma de A com B ({soma}) < {c}')
    else:
        print(f'\n[>] A soma de A com B ({soma}) > {c}')
def q2():
    print('[+] Par ou Ímpar | Positivo ou Negativo')
    num = int(input('num: '))
    par_impar = num % 2
    if par_impar == 0:
        print(f'\n[>] {num} é um numero par')
    else:
        print(f'\n[>] {num} é um numero ímpar')
    
    if num < 0: 
        print(f'\n[>] {num} também é um número negativo')
    elif num > 0: 
        print(f'\n[>] {num} também é um número positivo')
    else: 
        print(f'\n[>] {num} é um número nulo')
def q3():
    a = int(input('a: '))
    b = int(input('b: '))

    if a == b:
        soma = a + b
        print(f'\n[>] {soma} é a soma de {a} com {b}, quando A e B são iguais.')
    else:
        c = a * b
        print(f'\n[>] {c} é a multiplicação de {a} com {b}, quando A e B são diferentes.')
def q4():
    print('[+] Mostrar o Sucessor e antessor')
    num = int(input('número: '))

    antecessor = num - 1
    sucessor = num + 1

    print(f'\n=> Antecessor: {antecessor}\n=> Número Atual: {num}\n=> Sucessor: {sucessor}')
def q5():
    print('[+] Comparação Salários')
    salario_minimo = 1293.20
    salario_usuario = float(input('Seu Salário: '))

    qnt_salarios = 0

    if salario_usuario < salario_minimo:
        print('\n[>] Você recebe menos que 1 salário minimo')
        print(f'[>] Seu salário: {salario_usuario:.2f}; \n[>] Salário Mínimo: {salario_minimo:.2f}.')
    else:
        qnt_salarios = int(salario_usuario // salario_minimo)
        print(f'\n[>] Você recebe {qnt_salarios} salários mínimos! (~APROXIMADAMENTE~)')
        print(f'[>] Seu salário: {salario_usuario:.2f}; \n[>] Salário Mínimo: {salario_minimo:.2f}')
def q6():
    print('[+] Reajuste de 5%')
    valor = float(input('Valor: '))
    juros = 5/100
    reajuste = valor + (valor*juros)
    print(f'\n[>] O valor original: {valor:.2f}\n[>] O valor pós reajuste: {reajuste:.2f}')
def q7():
    meu_nome = 'João Lucas'
    minha_idade = 17

    print('_________________________' \
    '\n[>] Adivinhar o criador')
    nome = input('Nome de quem fez os códigos: ')
    idade = int(input('Idade dele: '))

    if nome == meu_nome:
        print(f'\n[+] Acertou! {meu_nome} é o nome do criador dos códigos')
    elif idade == minha_idade:
        print(f'[+] Acertou! {minha_idade} é a idade do criador dos códigos')
    else:
        if nome != meu_nome:
            print(f'\n[-] Errou! {nome} não é o nome do criador dos códigos')
        if idade != minha_idade:
            print(f'[-] Errou! {idade} não é a idade do criador dos códigos \n Tente Novamente...')
        return q7()
def q8():
    pass
def q9():
    pass
def q10():
    pass




while True:
    print('=============================')
    escolha = int(input('1/2/3/4...: '))
    if escolha == 1:
        q1()
    if escolha == 2:
        q2()
    if escolha == 3:
        q3()
    if escolha == 4:
        q4()
    if escolha == 5:
        q5()
    if escolha == 6:
        q6()
    if escolha == 7:
        q7()
    if escolha == 8:
        q8()
    if escolha == 9:
        q9()
    if escolha == 10:
        q10()