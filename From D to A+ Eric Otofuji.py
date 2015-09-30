# -*- coding: utf-8 -*-
"""
Insper Instituto de Ensino e Pesquisa
Faculdade de Engenharia
Eric Fernando Otofuji Abrantes
Projeto parte da recuperação de Design de Software
"""

board = []

for i in range(5):
    board.append(["O"]*5)
    
def print_board(board):
    for i in board:
		print(" ".join(i))
		