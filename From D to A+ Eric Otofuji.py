# -*- coding: utf-8 -*-
"""
Insper Instituto de Ensino e Pesquisa
Faculdade de Engenharia
Eric Fernando Otofuji Abrantes
Projeto parte da recuperação de Design de Software
Instruído pelo curso de Python do CodeCademy
"""

from random import randint

board = []

for x in range(5):
    board.append(["O"]*5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("\n\n\n\nHORA DE JOGAR BATALHA NAVAL!!!\n\n")
print_board(board)

def random_row(board):
    return randint(0, len(board)-1)

def random_col(board):
    return randint(0, len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(10):
    guess_row = int(input("\nEscolha uma linha: "))
    guess_col = int(input("\nEscolha uma coluna: "))

    if guess_row == ship_row and guess_col == ship_col:
        print ("\nParabéns! Você afundou meu encouraçado...")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("\nParabéns! Você não só errou o meu encouraçado como também errou o oceano! VOcê certamente é um gênio da mira...")
        
        elif(board[guess_row][guess_col] == "X"):
            print ("\nVocê já atirou aqui e já errou. Por que insistir no mesmo erro? Parabéns!")
        
        else:
            print ("\nParabéns! Você fez umas águas saírem voando. Encouraçado que é bom, nada... Você errou o tiro!")
            board[guess_row][guess_col] = "X"
        
        # Print turn and board again here
        print ("\nRodada " + str(turn+1) + " de 10.\n")
        print_board(board)


if turn >= 9:
    print ("\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER\nGAME OVER")