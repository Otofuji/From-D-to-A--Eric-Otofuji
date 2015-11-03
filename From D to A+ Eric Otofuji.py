# -*- coding: utf-8 -*-
"""
Insper Instituto de Ensino e Pesquisa
Faculdade de Engenharia
Departamento de Computação
Eric Fernando Otofuji Abrantes
Projeto parte da recuperação de Design de Software
Instruído pelo curso de Python do CodeCademy
"""

from random import randint

board = []

for x in range(5):
    board.append(["O"]*5)

ships = []
fleet = (open("fleet.txt",encoding="utf-8",mode="r")).readlines()

for i in fleet:
    x = i.strip()
    if fleet != "":
        ships.append(int(x))

def shippos(ship):
    axis = randint(0,1)
    col = 0
    row = 0
    a = 0
    b = 0
    c = 0
    if axis == 0:
        col = randint(0,len(board[0])-1)
        row = randint(0,len(board[0])-1)
        a = (row,col)
        if ship > 1:
            b = (row+1,col)
        if ship > 2:
            c = (row+2,col)
    else:
        col = randint(0,len(board[0])-1)
        row = randint(0,len(board[0])-1)
        a = (row,col)
        if ship > 1:
            b = (row,col+1)
        if ship > 2:
            c = (row,col+2)
    return(a,b,c)

print(shippos(ships[1]))
ocean_com_bug = [(shippos(ships[0])),(shippos(ships[1])),(shippos(ships[2]))]
ocean = [(3,1),(4,0),(4,1),(1,2),(3,2),(2,2)]
ocean_row,ocean_col = zip(*ocean)

print(ocean_com_bug)
print(ocean)
print(ocean_row)
print(ocean_col)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("\n\n\n\nHORA DE JOGAR BATALHA NAVAL!!!\n\nCada embarcação destruída te dará um total de três pontos\nConsiga nove pontos para ganhar\nVocê tem dez tiros\n\n")
print_board(board)

score = 0
for turn in range(10):
    guess_row = int(input("\nEscolha uma linha: "))
    guess_col = int(input("\nEscolha uma coluna: "))
 
    elif(board[guess_row][guess_col] == "W"):
        print ("\n\n\nAhhhh, malandro! Acha que atirando onde já atirou e já acertou vai fazer ganhar o jogo?\nNananinanão! Tente de novo!\nVocê foi penalizado perdendo uma rodada que poderia estar usando de forma mais útil.")
    elif guess_row == ocean_row[0] and guess_col == ocean_col[0]:
        board[guess_row][guess_col] = "W"
        print("\n\n\nParabéns! Você destruiu o submarino! Três pontos!")
        score+=3
        if score >=9:
            break
    elif guess_row == ocean_row[1] and guess_col == ocean_col[1]:
        board[guess_row][guess_col] = "W"
        print("\n\n\nParabéns! Você atingiu o navio nuclear, que tem duas partes! Dois pontos por este tiro!")
        score+=2
        if score >=9:
            break
    elif guess_row == ocean_row[2] and guess_col == ocean_col[2]:
        board[guess_row][guess_col] = "W"
        print("\n\n\nParabéns! Você atingiu o navio nuclear, que tem duas partes! Um ponto por este tiro!")
        score+=1
        if score >=9:
            break
    elif guess_row == ocean_row[3] and guess_col == ocean_col[3] or guess_row == ocean_row[4] and guess_col == ocean_col[4] or guess_row == ocean_row[5] and guess_col == ocean_col[5]:
        board[guess_row][guess_col] = "W"
        print("\n\n\nParabéns! Você atingiu o porta-aviões, que tem três partes! Um ponto por este tiro!")
        score+=1
        if score >=9:
            break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("\n\n\nParabéns! Você não só errou o meu encouraçado como também errou o oceano! Você certamente é um gênio da mira...")
        
        elif(board[guess_row][guess_col] == "X"):
            print ("\n\n\nVocê já atirou aqui e já errou. Por que insistir no mesmo erro? Parabéns!")
        
        else:
            print ("\nP\n\narabéns! Você fez umas águas saírem voando. Encouraçado que é bom, nada... Você errou o tiro!")
            board[guess_row][guess_col] = "X"
        
    print ("\nRodada " + str(turn+1) + " de 10.\n")
    print ("\nPontuação: " + str(score) + ".\n")
    print_board(board)

if turn >= 9:
    print ("\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER")
else:
    print("\nPARABÉNS! VOCÊ GANHOU!\nPARABÉNS! VOCÊ GANHOU!\nPARABÉNS! VOCÊ GANHOU!\nPARABÉNS! VOCÊ GANHOU!\nPARABÉNS! VOCÊ GANHOU!\nPARABÉNS! VOCÊ GANHOU!\nPARABÉNS! VOCÊ GANHOU!\nPARABÉNS! VOCÊ GANHOU!\nPARABÉNS! VOCÊ GANHOU!\nPARABÉNS! VOCÊ GANHOU!")