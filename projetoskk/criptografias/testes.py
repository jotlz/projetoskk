import os
import sys
#@ dicionário mapeamento de números (ord)
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

#@ dicionário mapeamento de letras (chr)
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

#@ dicionário mapeamento de código binário
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

#* Função para usar o dicionário de código binário
def binario_cripto(letras):
    letra = letras.upper()
    return mapeamento_binario.get(letra, '*desconhecido*')

#* Função para usar o dicionário de letras
def minha_ord(letras):
    letra_maiuscula = letras.upper()
    return mapeamento_numeros.get(letra_maiuscula, '*desconhecido*')

#* Função para usar o dicionário de números
def minha_chr(numeros):
    return mapeamento_letras.get(numeros, '*desconhecido*')

#! Função trasnformar em código binário
def binario():
    print("[+]Código Binário")

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
def rot13():
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
'''def cifradecezar():
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


#! Função que permite escolher qual
def escolhasTestes():
    while True:
        print(f'''
               {"_"*29}
               |   0 - Encerrar Programa...|
:{"-"*60}:
  | 1 - Código Binário | 4 - Em Breve... | 7 - Em Breve... |
  | 2 - Rot13          | 5 - Em Breve... | 8 - Em Breve... |
  | 3 - Cifra de Cezar | 6 - Em breve... | 9 - Em Breve... |
:{"-"*60}:
''')
        escolha = int(input('Escolha: '))

        match escolha:
            case 0:
                os.system("clear")
                sys.exit()
            case 1:
                os.system("clear")
                binario()
            case 2:
                os.system("clear")
                rot13()
            case 3:
                print('Em manutenção...')
                pass
            #// cifradecezar()
            case _:
                os.system("clear")
                print("Escolha apenas as opções que estejam disponíveis")
escolhasTestes()