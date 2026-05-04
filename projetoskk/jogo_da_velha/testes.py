import sys #@ Biblioteca para encerrar o sistema
import os #@ Biblioteca para limpar o terminal
import random as rm #@ Biblioteca para randomizar as jogadas do bot
import time as tm #@ Biblioteca para dar tempo nas respostas do bot e não responder instantaneamente 
#* Variáveis que formam o placar 
pnts_X = 0
pnts_O = 0
velhas = 0
#* Função que guarda a lógica do jogo
def jogo(modo):
    #* Põe as variáveis do placar como globais dentro da função
    global pnts_O, pnts_X, velhas
    #* Posições da matriz do jogo
    matriz = [
            [1,2,3],
            [4,5,6],
            [7,8,9]]
                
    #* Jogador inicial, X e O 
    xis = '✖'
    ball = '⚉'
    jogador_atual = xis
    #* Printa a tabela inicialmente antes da primeira jogada 
    print('[+]Jogo da Velha')
    print(f'\nJogador 1(J1): {xis}\nJogador 2(J2): {ball}')
    print(f"\n {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} \n---+---+---\n {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} \n---+---+---\n {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} \n")
    #! Laço que faz os turnos funcionarem
    while True:
        #* Lista de combinações para verificar possível vitória
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
        #* Verificação para ver se a casa escolhida está disponível, se venceu e se empatou 
        casa_encontrada = False
        venceu = False
        empate = True

        #? Condição para evitar erros e quebra do código
        try:
            #? Condição que faz o modo do bot funcionar
            if modo == 2 and jogador_atual == ball:
                animacao()
                possivel_jogada = False
                for comb in combinacoes:
                    bolas = 0
                    jogada = None
                    casa_vazia = False
                    for (i, j) in comb:
                        valor = matriz[i][j]
                        if valor == ball:
                            bolas += 1
                        if isinstance(valor, int):
                            jogada = valor
                            casa_vazia = True
                    if casa_vazia and bolas == 2:
                        posicao = jogada
                        possivel_jogada = True
                        break
                if not possivel_jogada:
                    for comb in combinacoes:
                        ñ_bolas = 0
                        jogada = None
                        casa_vazia = False
                        for (i, j) in comb:
                            valor = matriz[i][j]
                            if valor == xis:
                                ñ_bolas += 1
                            if isinstance(valor, int):
                                jogada = valor
                                casa_vazia = True
                        if casa_vazia and ñ_bolas == 2:
                            posicao = jogada
                            possivel_jogada = True
                            break
                    if not possivel_jogada:
                        possiveis_forks = []
                        for i, coordenadas in enumerate(matriz):
                            for j, valores in enumerate(coordenadas):
                                if isinstance(valores, int):
                                    val = valores
                                    matriz[i][j] = ball
                                    pfork = 0
                                    for combos in combinacoes:
                                        qnt_balls = 0
                                        csvazia = 0
                                        for (l, c) in combos:
                                            if matriz[l][c] == ball:
                                                qnt_balls += 1
                                            if isinstance(matriz[l][c], int):
                                                csvazia += 1
                                        if qnt_balls == 2 and csvazia == 1:
                                            pfork += 1
                                    if pfork >= 2:
                                        possiveis_forks.append(val)
                                        matriz[i][j] = val
                                    else:
                                        matriz[i][j] = val
                        if possiveis_forks:
                            posicao = rm.choice(possiveis_forks)
                            possivel_jogada = True
                        if not possivel_jogada:
                            opcoes = []
                            if matriz[0][0] == 1:
                                opcoes.append(1)
                            if matriz[1][1] == 5:
                                opcoes.append(5)
                            if matriz[0][2] == 3:
                                opcoes.append(3)
                            if matriz[2][0] == 7:
                                opcoes.append(7)
                            if matriz[2][2] == 9:
                                opcoes.append(9)
                            if opcoes:
                                posicao = rm.choice(opcoes)
                            else:
                                csvzs = []
                                for linhas in matriz:
                                    for valores in linhas:
                                        if isinstance(valores, int):
                                            csvzs.append(valores)
                                posicao = rm.choice(csvzs)
            else:
                #@ Entrada que pede a posição para jogar na matriz
                posicao = int(input(f"{jogador_atual} - Posição: "))
                #? Condição para evitar posições que não existem na matriz
            if posicao < 1 or posicao > 9:
                print("Entrada Inválida!")
            else:
                #! Laço que percorre a lista matriz
                for i, tuplas in enumerate(matriz):
                    #! Laço que percorre a sublista de matriz, tuplas
                    for j, itens in enumerate(tuplas):
                        #? Condição para verificar se a casa é ainda jogável
                        if isinstance(itens, int):
                            #? Condição para verificar se o item de tupla é igual a posição escolhida
                            if itens == posicao:
                                #* Armazena a posição da linha e da coluna
                                linha = i
                                coluna = j
                                #* Responde se a casa foi encontrada
                                casa_encontrada = True
                                break
                    #? Condição que sai do segundo laço
                    if casa_encontrada:
                        break
                #? Condição que verifica se a casa encontrada é verdadeira e troca o valor numérico por X ou O
                if casa_encontrada:
                    #* troca o valor numérico pelo atual jogador
                    matriz[linha][coluna] = jogador_atual
                    #* limpa o terminal
                    os.system("clear")
                    
                    #! Laço que entra na lista de combinações
                    for comb in combinacoes:
                        #? Condição que verifica vitória
                        if all(matriz[i][j] == jogador_atual for i ,j in comb):
                            venceu = True
                            break
                    #? Condição que pontua em caso de vitória
                    if venceu:
                        print(f"\n {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} \n---+---+---\n {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} \n---+---+---\n {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} \n")
                        print(f"O {jogador_atual} Venceu!")
                        if jogador_atual == xis:
                            pnts_X+=1
                            break
                        else:
                            pnts_O+=1
                            break
                    else:
                        #! Laço que entra na lista matriz
                        for linhas in matriz:
                            #! Laço que entra nas linhas da matriz
                            for valores in linhas:
                                #? Condição que verifica se ainda contém algum valor inteiro na matriz
                                if isinstance(valores, int):
                                    empate = False
                                    break
                        #? Condição que contabiliza o empate
                        if empate:
                            print("Deu velha")
                            velhas+=1
                            break
                        print(f"\n {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} \n---+---+---\n {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} \n---+---+---\n {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} \n")
                    #? Condição que verifica quem está jogando e faz a troca na troca de turnos
                    if jogador_atual == xis:
                        jogador_atual = ball
                    else:
                        jogador_atual = xis
                #* Resposta para caso a casa escolhida esteja já ocupada
                else:
                    print("Casa Ocupada!\nTente Outra Posição!")
            #* Resposta para o tratamento do erro que quebraria o código
        except ValueError:
            print("Entrada Inválida!\nA Posição deve ser dada apenas em números inteiros!!")

def animacao(mensagem="O BOT está pensando", ciclos=2, intervalo=0.3):
    for _ in range(ciclos):
        for i in range(1, 4):
            print(f'\r{mensagem}{"." * i:<3}', end='', flush = True)
            tm.sleep(intervalo)
        for i in range(3, 0, -1):
            print(f'\r{mensagem}{"." * i:<3}', end='', flush=True)
            tm.sleep(intervalo)
    print()

#! Laço que permite o jogo rodar novamente caso desejado
print('''
[>]Modo de Jogo
    [+] 1 -> PvP
    [+] 2 -> BOT
''')
while True:
    modo = int(input("Escolha o Modo de Jogo: "))
    if modo not in [1,2]:
        print("Escolha apenas entre\n1 - PvP\n2 - BOT")
    else:
        break
while True:
    jogo(modo)
    print(f"""
  {'_'*8}
  |PLACAR|
{'-'*12}
|J1(✖) -> {pnts_X}|
|J2(⚉) -> {pnts_O}|
|==(#) -> {velhas}|
{'-'*12}
""")
    #! Laço que pergunta sempre após uma vitória ou empate se deseja jogar novamente
    while True:
        #@ entrada para escolha de jogar novamente ou não
        jogar_novamente = input("Deseja Jogar Novamente? s/n: ").lower()
        #? Condição que reinicia o jogo caso a escolha seja sim
        if jogar_novamente == 's':
            os.system("clear")
            break
        #? Condição que encerra o sistema caso a escolha seja não
        elif jogar_novamente == 'n':
            os.system("clear")
            sys.exit()
        #* Resposta para entradas que não sejam "s" ou "n"
        else:
            os.system("clear")
            print("Responda apenas com\nS - para sim\nN - para não")
        