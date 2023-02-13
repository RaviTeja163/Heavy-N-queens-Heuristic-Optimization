# greedy search algorithm

import random
import numpy as np
import math

def get_Board_Size():
    board_size = int(input("Enter board size: "))
    return board_size

def print_board(board, string, print_h_value=False):
	print("\n||||"+string+"||||")

	for i in range(len(board)):
		for j in range(len(board)):
			print(str(board[i][j])+" ", end="")
		print()
	if(print_h_value):
		print("H-value of the board: ", get_H_Value(board))
	print("----------------------------------")

def get_Random_Board(n):
    board_size = n
    
    board = [[0 for i in range(board_size)] for i in range(board_size)]
    r = random.sample(range(1,board_size+1),board_size)
    for i in range(board_size):
        row = random.randint(0,board_size-1)
        board[row][i] = r[i]
    
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end = "  ")
        print("\n")

    return board


# Now h value is the pair of queens that are attacking each other
# So we calculate the h value of the board

def get_H_Value(board):
    h = 0
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            # look for a queen
            if board[i][j] > 0:
                # found a queen. Now look for attacking queen pair

                # Now attack can occur from 8 directions. 
                # Top Left, Top Right, Bottom Left, Bottom Right, Upward, Downward, Left, Right

                # Top Left
                k = 1
                try:
                    while not (i-k < 0 or j-k < 0):
                        if board[i-k][j-k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Top Right
                k = 1
                try:
                    while not (i-k < 0 or j+k < 0):
                        if board[i-k][j+k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Bottom Left
                k = 1
                try:
                    while not (i+k < 0 or j-k < 0):
                        if board[i+k][j-k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Bottom Right
                k = 1
                try:
                    while not (i+k < 0 or j+k < 0):
                        if board[i+k][j+k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Upward
                k = 1
                try:
                    while not (i-k < 0):
                        if board[i-k][j] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Downward
                k = 1
                try:
                    while not (i+k < 0):
                        if board[i+k][j] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Left
                k = 1
                try:
                    while not (j-k < 0):
                        if board[i][j-k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Right
                k = 1
                try:
                    while not (j+k < 0):
                        if board[i][j+k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

    return int(h/2)

def get_Q_Positions(board):
    pos = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] > 0:
                pos.append(j)
    return pos

def get_H_Matrix(board):
    queen_positions = get_Q_Positions(board)
    board_size = len(board)
    h_matrix = []
    temp_board = np.copy(board)
    for i in range(board_size):
        col_h_values = []
        temp_board[queen_positions[i]][i] = 0
        for j in range(board_size):
            
            temp_board[j][i] = 1
            temp_h_value = get_H_Value(temp_board)
            col_h_values.append(temp_h_value)
            temp_board[j][i] = 0
        temp_board[queen_positions[i]][i] = 1
        h_matrix.append(col_h_values)
    h_matrix= np.array(h_matrix).T.tolist()
    print_board(h_matrix, "H MATRIX", False)
    return h_matrix

def get_Min_H_Index(h_matrix):
    min_value = math.inf
    min_index = [0,0]

    for i in range(len(h_matrix)):
        for j in range(len(h_matrix)):
            if h_matrix[i][j] < min_value:
                min_value = h_matrix[i][j]
                min_index[0] = i
                min_index[1] = j
    return min_value, min_index

def find_Good_Successor(board):
    temp_board = np.copy(board)
    queen_positions = get_Q_Positions(board)
    h_matrix = get_H_Matrix(temp_board)
    min_h, min_index = get_Min_H_Index(h_matrix)
    temp_board[queen_positions[min_index[1]]][min_index[1]] = 0
    temp_board[min_index[0]][min_index[1]] = board[queen_positions[min_index[1]]][min_index[1]]
    stop = False
    if min_h == 0:
        stop = True
    return temp_board, stop

def get_Cost(initial_board, final_board):
    q_init_pos = get_Q_Positions(initial_board)
    q_final_pos = get_Q_Positions(final_board)
    sum = 0
    for i in range(len(q_init_pos)):
        tiles_moved = abs(q_init_pos[i] - q_final_pos[i])
        sum += tiles_moved * (initial_board[q_init_pos[i]][i] ** 2)
    return sum

stop = False
n = get_Board_Size()
number_iter = []

while not stop:
    board = get_Random_Board(n)
    print_board(board, "INITIAL STATE", True)
    iterations = 0
    new_board, stop = find_Good_Successor(board)
    while not stop and iterations < 100:
        print_board(new_board, "INTERMEDIATE STATE", True)
        new_board, stop = find_Good_Successor(new_board)
        iterations += 1
        number_iter.append(iterations)

print_board(new_board, "FINAL STATE", True)
iteration_count = len(number_iter)-1
print("\n"+str(iteration_count)+" random restarts were required\n")
print(str((iteration_count*200)+number_iter[iteration_count])+" are the number of iterations taken to find solution")