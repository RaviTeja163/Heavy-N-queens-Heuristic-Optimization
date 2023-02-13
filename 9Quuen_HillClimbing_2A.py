# Greedy search algorithm

import random
import numpy as np
import math
import time


def print_board(board, string, print_h_value=False):
    print("\n||||" + string + "||||")

    for i in range(len(board)):
        for j in range(len(board)):
            print(str(board[i][j]) + " ", end="")
        print()
    if (print_h_value):
        print("H-value of the board: ", get_H_Value(board))
    print("----------------------------------")


def get_Random_Board(n):
    board_size = n

    board = [[0 for i in range(board_size)] for i in range(board_size)]
    r = random.sample(range(1, board_size + 1), board_size)
    for i in range(board_size):
        row = random.randint(0, board_size - 1)
        board[row][i] = r[i]

    # inserting the 9th queen
    value = random.randint(1, board_size + 1)
    index_row = random.randint(0, board_size - 1)
    index_col = random.randint(0, board_size - 1)
    inserted = False
    while not inserted:
        if board[index_row][index_col] > 0:
            index_row = random.randint(0, board_size - 1)
            index_col = random.randint(0, board_size - 1)
        else:
            board[index_row][index_col] = value
            inserted = True
            break

    # print the board
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end="  ")
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
                    while not (i - k < 0 or j - k < 0):
                        if board[i - k][j - k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Top Right
                k = 1
                try:
                    while not (i - k < 0 or j + k < 0):
                        if board[i - k][j + k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Bottom Left
                k = 1
                try:
                    while not (i + k < 0 or j - k < 0):
                        if board[i + k][j - k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Bottom Right
                k = 1
                try:
                    while not (i + k < 0 or j + k < 0):
                        if board[i + k][j + k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Upward
                k = 1
                try:
                    while not (i - k < 0):
                        if board[i - k][j] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Downward
                k = 1
                try:
                    while not (i + k < 0):
                        if board[i + k][j] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Left
                k = 1
                try:
                    while not (j - k < 0):
                        if board[i][j - k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

                # Right
                k = 1
                try:
                    while not (j + k < 0):
                        if board[i][j + k] > 0:
                            h += 1
                        k += 1
                except:
                    pass

    return int(h / 2)


def get_Q_Positions(board):
    pos = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] > 0:
                pos.append(j)
                break
    return pos


def get_Cost(initial_board, final_board):
    attacking_pairs = get_H_Value(final_board)
    q_init_pos = get_Q_Positions(initial_board)
    q_final_pos = get_Q_Positions(final_board)
    sum = 0
    for i in range(len(q_init_pos)):
        tiles_moved = abs(q_init_pos[i] - q_final_pos[i])
        sum += tiles_moved * (initial_board[q_init_pos[i]][i] ** 2)
    final_cost = sum + (100 * attacking_pairs) # defined cost for problem 2
    return final_cost


def get_neighbors(node):
    queen_positions = get_Q_Positions(node)
    node_neighbors = []
    for i in range(len(node)):
        for j in range(len(node[0])):
            temp_board = np.copy(node)
            temp_board[queen_positions[i]][i] = 0
            if not j == queen_positions[i] and temp_board[j][i] == 0:
                temp_board[j][i] = node[queen_positions[i]][i]
                neighbor_node = np.copy(temp_board)
                node_neighbors.append(neighbor_node)
                temp_board[j][i] = 0
    return node_neighbors


# Main
board = get_Random_Board(8)
print_board(board, "INITIAL STATE", True)

current_board = np.copy(board)
current_cost = get_Cost(board, current_board)
time_limit = 10
t = time.time()
td = 0
restarts = 0
while td < time_limit:
    td = time.time() - t
    neighbors = get_neighbors(current_board)
    min_cost = 999999
    for neighbor in neighbors:
        neighbor_cost_value = get_Cost(board, neighbor)
        if neighbor_cost_value < min_cost:
            min_cost = neighbor_cost_value
            min_cost_board = np.copy(neighbor)

    if min_cost < current_cost:
        current_board = np.copy(min_cost_board)
        current_cost = min_cost
    else:  # perform a random restart
        current_board = get_Random_Board(8)
        restarts += 1
    print_board(current_board, "INTERMEDIATE STATE", True)

print_board(current_board, "FINAL STATE", True)
print("\n" + str(restarts) + " random restarts done in the process\n")
print(f"TIME LIMIT({time_limit} secs) EXCEEDED")
