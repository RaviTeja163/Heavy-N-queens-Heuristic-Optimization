# a star search

import time
import math
import numpy as np
import random

def get_Board_Size():
    board_size = int(input("Enter board size: "))
    return board_size

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

def print_board(board, string, print_h_value=False):
	print("\n||||"+string+"||||")

	for i in range(len(board)):
		for j in range(len(board)):
			print(str(board[i][j])+" ", end="")
		print()
	if(print_h_value):
		print("H-value of the board: ", get_H_Value(board))
	print("----------------------------------")

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

def get_Q_Weight(board):
    board_size = len(board)
    queen_weights = []
    for i in range(board_size):
        for j in range(board_size):
            if board[j][i] > 0:
                queen_weights.append(board[j][i])
    return queen_weights

def get_Cost_Matrix(board):
    temp_board = np.copy(board)
    queen_positions = get_Q_Positions(temp_board)
    queen_weights = get_Q_Weight(temp_board)
    board_size = len(temp_board)
    cost_matrix = []
    for i in range(board_size):
        col_cost_values = []
        for j in range(board_size):
            tiles_moved = abs(queen_positions[i] - j)
            moving_cost = queen_weights[i]**2 * tiles_moved
            col_cost_values.append(moving_cost)
        cost_matrix.append(col_cost_values)
    cost_matrix = np.array(cost_matrix).T.tolist()
    # print_board(cost_matrix, "COST MATRIX", False)
    return cost_matrix
    
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
    # print_board(h_matrix, "H MATRIX", False)
    return h_matrix


def get_Total_Cost_Matrix(board):
    h_matrix = get_H_Matrix(board)
    cost_matrix = get_Cost_Matrix(board)
    return np.add(h_matrix,cost_matrix)

def get_Min_TC_Value(total_cost_matrix):
    min_value = math.inf
    min_index = [0,0]

    for i in range(len(total_cost_matrix)):
        for j in range(len(total_cost_matrix)):
            if total_cost_matrix[i][j] < min_value:
                min_value = total_cost_matrix[i][j]
                min_index[0] = i
                min_index[1] = j
    return min_value, min_index

def get_Min_H_Value(h_matrix):
    min_value = math.inf
    min_index = [0,0]

    for i in range(len(h_matrix)):
        for j in range(len(h_matrix)):
            if h_matrix[i][j] < min_value:
                min_value = h_matrix[i][j]
                min_index[0] = i
                min_index[1] = j
    return min_value, min_index

def get_Cost(initial_board, final_board):
    q_init_pos = get_Q_Positions(initial_board)
    q_final_pos = get_Q_Positions(final_board)
    sum = 0
    for i in range(len(q_init_pos)):
        tiles_moved = abs(q_init_pos[i] - q_final_pos[i])
        sum += tiles_moved * (initial_board[q_init_pos[i]][i] ** 2)
    return sum
tic = time.time()
n = get_Board_Size()
stop = False
while not stop:
    board = get_Random_Board(n)
    open_list = []
    open_list = [board]
    final_board = []
    neighbours = []
    neighbours_min_tc_value = []
    neighbours_min_tc_index = []
    num_iterations = []
    i = 0
    while len(open_list) > 0 and not stop and i < 100:
        current_board = open_list.pop(0)
        current_board_tc_matrix = get_Total_Cost_Matrix(current_board)
        current_board_min_tc_value = get_Min_TC_Value(current_board_tc_matrix)[0]
        current_board_min_tc_index = get_Min_TC_Value(current_board_tc_matrix)[1]
        queen_positions = get_Q_Positions(current_board)
        for i in range(len(current_board)):
            for j in range(len(current_board)):
                temp_board = np.copy(current_board)
                temp_board[queen_positions[i]][i] = 0
                if not j == i:  
                    temp_board[j][i] = current_board[queen_positions[i]][i]
                    temp_board_tc_matrix = get_Total_Cost_Matrix(temp_board)
                    temp_board_min_tc_value_index = get_Min_TC_Value(temp_board_tc_matrix)
                    neighbours_min_tc_value.append(temp_board_min_tc_value_index[0])
                    neighbours_min_tc_index.append(temp_board_min_tc_value_index[1])
                    neighbours.append(temp_board)
        min_tc_value = min(neighbours_min_tc_value)
        for i in range(len(neighbours)):
            if neighbours_min_tc_value[i] == min_tc_value:
                open_list.append(neighbours[i])

        current_board_h_value = get_H_Value(current_board)

        if current_board_h_value == 0:
            print_board(current_board, "FINAL STATE", True)
            final_board = current_board
            stop = True
            break
        else:
            print_board(current_board, "INTERMEDIATE STATE", True)
        i += 1
        print(i)
        num_iterations.append(i)
    
toc = time.time()
j = len(num_iterations)-1
# print(f"{j*200 + num_iterations[j]} are the number of iterations required to find the solution")
# print(f"{i-1} number of random restarts")
time_taken = int(toc - tic)
print(f"{time_taken} secs is the time taken for a board of {n} size")