#biblioteca mapeamento numeros (ord)
mapeamento_numeros = {
    'A' : 1, 'B' : 2,
    'C' : 3, 'D' : 4,
    'E' : 5, 'F' : 6,
    'G' : 7, 'H' : 8,
    'I' : 9, 'J' : 10,
    'K' : 11, 'L' : 12,
    'M' : 13, 'N' : 14,
    'O' : 15, 'P' : 16,
    'Q' : 17, 'R' : 18,
    'S' : 19, 'T' : 20,
    'U' : 21, 'V' : 22,
    'W' : 23, 'X' : 24,
    'Y' : 25, 'Z' : 26
}

#biblioteca mapeamento letras (chr)
mapeamento_letras = {
    1 : 'A', 2 : 'B',
    3 : 'C', 4 : 'D',
    5 : 'E', 6 : 'F',
    7 : 'G', 8 : 'H',
    9 : 'I', 10 : 'J',
    11 : 'K', 12 : 'L',
    13 : 'M', 14 : 'N',
    15 : 'O', 16 : 'P',
    17 : 'Q', 18 : 'R',
    19 : 'S', 20 : 'T',
    21 : 'U', 22 : 'V',
    23 : 'W', 24 : 'X',
    25 : 'Y', 26 : 'Z'   
}

#biblioteca mapeamento código binário
mapeamento_binario = {
    'A' : '01100001','B' : '01100010','C' : '01100011',
    'D' : '01100100','E' : '01100101','F' : '01100110',
    'G' : '01100111','H' : '01101000','I' : '01101001',
    'J' : '01101010','K' : '01101011','L' : '01101100',
    'M' : '01101101','N' : '01101110','O' : '01101111',
    'P' : '01110000','Q' : '01110001','R' : '01110010',
    'S' : '01110011','T' : '01110100','U' : '01110101',
    'V' : '01110110','W' : '01110111','X' : '01111000',
    'Y' : '01111001','Z' : '01111010','0' : '00110000',
    '1' : '00110001','2' : '00110010','3' : '00110011',
    '4' : '00110100','5' : '00110101','6' : '00110110',
    '7' : '00110111','8' : '00111000','9' : '00111001',
}

#chama a biblioteca de mapeamento binário
def binario_cripto(letras):
    letra = letras.upper()
    return mapeamento_binario.get(letra, '*desconhecido*')

#chama a biblioteca de mapeamento de letras
def minha_ord(letras):
    letra_maiuscula = letras.upper()
    return mapeamento_numeros.get(letra_maiuscula, '*desconhecido*')

#chama a biblioteca de mapeamento de números
def minha_chr(numeros):
    return mapeamento_letras.get(numeros, '*desconhecido*')

#função de traduzir para código binário
def Binario():
    print(":--------------------------------:")
    print("[+] Código Binário")
    print("Texto para criptografar\n")

    texto = input("Criptografar: ").upper()
    textoCriptografado = []

    for letra in texto:

        if letra in mapeamento_binario:

            letra = binario_cripto(letra)
            criptografia = letra
            textoCriptografado.append(criptografia)

        else:
            
            textoCriptografado.append(letra)

    print('\n[>>]',' '.join(textoCriptografado))

#função para transformar em Rot13
def Rot13():
    print(":--------------------------------:")
    print("[+] ROT13")
    print("Texto criptografar\n")

    texto = input("Criptografar: ")
    textoCriptografado = []
    
    for letra in texto:

        if letra.isalpha():

            if minha_ord(letra) < 14:
                unicode = (minha_ord(letra) + 13)
            else:
                unicode = (minha_ord(letra) - 13)
            criptografia = minha_chr(unicode)
            textoCriptografado.append(criptografia)
        else:
            textoCriptografado.append(letra)

    print('\n[>>]',''.join(textoCriptografado))

#função para criptografar em Cifra de Cézar (Manutenção - Refazer)
'''def CifraDeCezar():
    print(":--------------------------------:")
    print("[+] Cifra de Cezar")
    print("Criptografar: ")

    palavra = list(input("Palavra para ser criptografada: ").upper())
    deslocamento = int(input("deslocamento: "))

    palavraCriptografada = []
    for letras in palavra:

        if letras == ' ':
            criptografia = ' '
        elif letras == ',':
            criptografia = ','
        elif letras == '!':
            criptografia = '!'     
        elif letras == '.':
            criptografia = '.'       
        elif letras == '?':
            criptografia = '?'     
        elif letras == '"':
            criptografia = '"'

        else:
            unicode = (ord(letras) + deslocamento)

            if unicode > ord('Z') and unicode < ord('z'):
                unicode = (unicode - 26)

            criptografia = chr(unicode)

        palavraCriptografada.append(criptografia)

    print(''.join(palavraCriptografada))'''


#função que roda o código e pode repetir quantas vezes quiser
def escolhasTestes():

    while True:

        print(":--------------------------------:")
        print("Escolha dos Testes - 1 à 5...")
        escolha = int(input('escolha: '))

        if escolha == 0:
            return False
        if escolha == 1:
            Binario()
        if escolha == 2:
            Rot13()
        if escolha == 3:
            print('Em manutenção...')
            pass
            #CifraDeCezar()
        if escolha == 4:
            pass
        if escolha == 5:
            pass
        if escolha not in [0, 1, 2, 3, 4, 5]:
            print("Só de 0 à 5, num tem mais que isso!")
            return escolhasTestes()
escolhasTestes()
