
# *posições do jogo da velha
matriz = [  [1,2,3],
            [4,5,6],
            [7,8,9]]
            
#* X e O do jogo
xis = '✖'
ball = '⚉'

print('[+] Jogo da Velha')
print('\nJogador 1(J1): X\nJogador 2(J2): O')

print(f"\n {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} \n---+---+---\n {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} \n---+---+---\n {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} \n")

#* função que chama o jogo
def jogo():
    #*placar de vitórias
    winsj1 = 0
    winsj2 = 0

    if winsj1 > 0 or winsj2 > 0:
        print(f"\nPlacar: J1=>{winsj1} | J2=>{winsj2}")

    #* laço que faz os turnos do jogo funcionarem
    while True: 
        #* função que permite o j1 jogar e caso repetir uma casa ocupada repete a jogada
        def jogada1():
            while True:
                buscar_casa = False
                j1 = int(input('J1 - Posição: '))
                if j1 not in [1,2,3,4,5,6,7,8,9]:
                    print("Entrada Inválida")
                else:
                    for i, tuplas in enumerate(matriz):
                        for j, posicao in enumerate(tuplas):
                            if isinstance(posicao, int):
                                if posicao == j1:
                                    linha = i
                                    coluna = j
                                    buscar_casa = True
                                    break
                        if buscar_casa == True:
                            break

                    if buscar_casa == True:
                        matriz[linha][coluna] = xis
                        print(f" {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} \n---+---+---\n {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} \n---+---+---\n {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} \n")
                        return False
                    else:
                        print('Casa Ocupada!\nTente novamente...')

            #* função que permite o j2 jogar e caso repetir uma casa ocupada repete a jogada
        def jogada2():
            while True:
                buscar_casa = False
                j2 = int(input('J2 - Posição: '))
                if j2 not in [1,2,3,4,5,6,7,8,9]:
                    print('Entrada Inválida')
                else:
                    for i, tuplas in enumerate(matriz):
                        for j, posicao in enumerate(tuplas):
                            if isinstance(posicao, int):
                                if posicao == j2:
                                    linha = i
                                    coluna = j
                                    buscar_casa = True
                                    break
                        if buscar_casa == True:
                            break
                    if buscar_casa == True:
                        matriz[linha][coluna] = ball
                        print(f" {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} \n---+---+---\n {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} \n---+---+---\n {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} \n")
                        return False
                    else:
                        print('Casa Ocupada!\nTente Novamente...')
        #@ verifica se ganhou ou não
        jogada1(),jogada2()
jogo()