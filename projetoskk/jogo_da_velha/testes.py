def jogar_dnv():
    import sys; import os
    rpt = {1 : "s", 2 : "n"}

    repetir = input(f"Deseja jogar novamente? {rpt.get(1)}/{rpt.get(2)}: ").lower()
    if repetir == rpt.get(1):
        os.system('clear')
        jogo_da_velha()
    elif repetir == rpt.get(2):
        os.system('clear')
        sys.exit()
    else:
        print(f"Responda apenas com\n{rpt.get(1)} - para sim\n{rpt.get(2)} - para não")
        return jogar_dnv()

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
    pnts_X = 0
    pnts_O = 0
    empates = 0
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
            print(f"Placar:\n{xis} - {pnts_X}\n{ball} - {pnts_O}")
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
                        if jogador_atual == xis:
                            pnts_X+=1
                        else:
                            pnts_O+=1
                        jogar_dnv()
                    else:
                        for linhas in matriz:
                            for valores in linhas:
                                if isinstance(valores, int):
                                    empate = False
                        if empate:
                            print("Deu velha")
                            empates+=1
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