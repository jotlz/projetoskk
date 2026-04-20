def jogar_dnv():
    import sys; import os

    repetir = input("Deseja jogar novamente? S/N: ").lower()
    if repetir != 's' or  repetir != 'n':
        print("Apenas responda com\nS - (para sim)\nN - (para não)")
        return jogar_dnv()
    else:
        if repetir == 's':
            os.system('clear')
            jogo_da_velha()
        elif repetir == 'n':
            os.system('clear')
            sys.exit()

def jogo_da_velha():
    # *posições do jogo da velha
    matriz = [
            [1,2,3],
            [4,5,6],
            [7,8,9]]
                
    #* X e O do jogo
    xis = '✖'
    ball = '⚉'

    print('[+] Jogo da Velha')
    print(f'\nJogador 1(J1): {xis}\nJogador 2(J2): {ball}')

    print(f"\n {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} \n---+---+---\n {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} \n---+---+---\n {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} \n")

    #* laço que repete turnos até alguem ganhar ou empatar
    jogador_atual = xis
    while True:
        combinacoes = [
            # @ Linhas
            [(0,0),(0,1),(0,2)],
            [(1,0),(1,1),(1,2)],
            [(2,0),(2,1),(2,2)],
            # @ Colunas
            [(0,0),(1,0),(2,0)],
            [(0,1),(1,1),(2,1)],
            [(0,2),(1,2),(2,2)],
            # @ Diagonais
            [(0,0),(1,1),(2,2)],
            [(0,2),(1,1),(2,0)]
        ]
        venceu = False
        empate = True
        casa_ocupada = False
        try:
            posicao = int(input(f"{jogador_atual} - Posição: "))
            if posicao not in [1,2,3,4,5,6,7,8,9]:
                print("Entrada Inválida!")
            else:
                for i, tuplas in enumerate(matriz):
                    for j, itens in enumerate(tuplas):
                        if isinstance(itens, int):
                            if itens == posicao:
                                linha = i
                                coluna = j
                                casa_ocupada = True
                                break
                    if casa_ocupada:
                        break
                if casa_ocupada:
                    matriz[linha][coluna] = jogador_atual
                    for comb in combinacoes:
                        if all(matriz[i][j] == jogador_atual for i ,j in comb):
                            venceu = True
                            break
                    if venceu:
                        print(f"\n {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} \n---+---+---\n {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} \n---+---+---\n {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} \n")
                        print(f"{jogador_atual} - Venceu")
                        jogar_dnv()
                    elif not venceu:
                        for linhas in matriz:
                            for valores in linhas:
                                if isinstance(valores, int):
                                    empate = False
                                    print(valores)
                        if empate:
                            print("Deu velha")
                            break
                    print(f"\n {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} \n---+---+---\n {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} \n---+---+---\n {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} \n")
                    if jogador_atual == xis:
                        jogador_atual = ball
                    else:
                        jogador_atual = xis
                else:
                    print("Casa Ocupada!\nTente Outra Posição!")
        except ValueError:
            print("Entrada Inválida!\nA Posição deve ser dada apenas em números inteiros!!")
jogo_da_velha()