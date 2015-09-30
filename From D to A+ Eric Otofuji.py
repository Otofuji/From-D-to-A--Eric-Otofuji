# -*- coding: utf-8 -*-
"""
Insper Instituto de Ensino e Pesquisa
Faculdade de Engenharia
Eric Fernando Otofuji Abrantes
Projeto parte da recuperação de Design de Software
Instruído pelo curso de Python do CodeCademy
"""

board = []

for i in range(5):
    board.append(["O"]*5)
    
def print_board(board):
    for i in board:
		print(" ".join(i))

from random import randint

def random_row(board):
    return randint(0, len(board)-1)

def random_col(board):
    return randint(0, len(board)-1)

guess_row = int(input("Escolha uma linha: "))
guess_col = int(input("Escolha uma coluna: "))

if guess_row == ship_row and guess_col == ship_col:
    print("Parabéns! Você afundou um navio!")
else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print "Você está mirando no oceano errado! Volte para o oceano certo! Coordenadas de 0 a 4"
    elif(board[guess_row][guess_col] == "X"):
        print "Você gosta de enfeitar o oceano. não? E no mesmo lugar..."
    else:
        print "Sua munição certamente enfeitará mais o oceano, pois acertar navio que é bom nada..."
        board[guess_row][guess_col] = "X"
    print_board(board)
