from time import time
import numpy as np
import random
import pandas as pd


class Node:
    def __init__(self,board):
        self.board = board
        self.h = getHeuristicCost(self.board)
        self.g = getPathCost(self.board)
        self.f = self.g + self.h
        self.parent = None

def getRandomBoard(n):
    board_size = n
    board = np.array([[0 for i in range(board_size)] for i in range(board_size)])
    r = random.sample(range(1,9),board_size)
    for i in range(board_size):
        row = random.randint(0,board_size-1)
        board[row][i] = r[i]
    return np.array(board)

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

def totalAttacks(board):
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


def getPathCost(board):
    q_init_pos = get_Q_Positions(init_board)
    q_final_pos = get_Q_Positions(board)
    sum = 0
    for i in range(len(q_init_pos)):
        tiles_moved = abs(q_init_pos[i] - q_final_pos[i])
        sum += tiles_moved * (init_board[q_init_pos[i]][i] ** 2)
    return sum


def getHeuristicCost(board):
    return 0

def qSort(q, cost_type):
    if cost_type == "g":
        return sorted(q, key = lambda i:i.g)
    if cost_type == "h":
        return sorted(q, key = lambda i:i.h)
    if cost_type == "f":
        return sorted(q, key = lambda i:i.f)   


def astar(init_board):
    iterations = 0

    initial_board_node = Node(init_board)
    initial_board_node.parent = initial_board_node
    open_list = list()
    closed_list = list()
    open_list.append(initial_board_node)
    while open_list:
        # sort the open list w.r.t. "f" cost
        open_list = qSort(open_list, cost_type="f")

        # pop out the lowest node as current
        current_board_node = open_list.pop(0)
        
        # append number of moves
        iterations += 1
        # print(len(open_list))

        # append the current board to the closed list
        closed_list.append(current_board_node)
        attacking_pairs = totalAttacks(current_board_node.board)

        # if board is solved break out of the loop
        if attacking_pairs == 0:
            configurations = []
            costs = []
            current = current_board_node
            while current is not initial_board_node:
                configurations.append(current.board)
                costs.append(current.g)
                current = current.parent
            return configurations[::-1], costs[::-1], len(closed_list)+len(open_list)

        # look for branching nodes
        branches = []
        q_positions = get_Q_Positions(current_board_node.board)
        for row in range(n):
            for col in range(n):
                temp_board = np.copy(current_board_node.board)
                temp_board[q_positions[row]][row] = 0
                temp_board[col][row] = current_board_node.board[q_positions[row]][row]
                new_board_node = Node(temp_board)
                new_board_node.parent = current_board_node
                branches.append(new_board_node)
        
        for branch in branches:
            # if the created branch board is not in closed list and not in open list append in open list
            if not any(np.array_equal(branch.board, z.board) for z in closed_list):
                if not any(np.array_equal(branch.board, k.board) for k in open_list):
                    open_list.append(branch)


initial_boards = list()
final_boards = list()
times_taken = list()
nodes_time = list()
branching_factors = list()
final_costs = list()

tic = time()
boards = 100
j = 0
total_times = 0
total_branchings = 0
total_costs = 0
total_nodes_per_sec = 0
while j < boards:
    n = 5  # size of the board
    init_board = getRandomBoard(n)
    # print("\n\nInitial Board is: ",init_board)
    attacking_queen_pair = totalAttacks(init_board)
    # print("\n\nThe attacking queen pairs are: ", attacking_queen_pair)
    if attacking_queen_pair == 0:
        continue
    else:
        start = time()
        configurations, costs, expandedStates = astar(init_board)
        stop = time()


        # get initial board and final board
        initial_boards.append(init_board)
        final_boards.append(configurations[-1])

        # get time taken per board
        t = (stop-start)
        times_taken.append(t)
        total_times += t

        # calculate the branching factor
        number_of_expanded_states = expandedStates
        depth_solution = len(configurations)
        branching = number_of_expanded_states ** (1 / (depth_solution + 1))
        branching_factors.append(branching)
        total_branchings += branching

        # calculating nodes/sec
        nodes_per_sec = number_of_expanded_states/t
        nodes_time.append(nodes_per_sec)
        total_nodes_per_sec += nodes_per_sec

        # get the final cost of the board
        final_costs.append(costs[-1])
        total_costs += costs[-1]
        j += 1


toc = time()
print(f"The time taken to run {boards} iterations with admissible heuristic: {int(toc - tic)} secs.")
print(f"The average time to solve the boards: ", total_times/boards)
print(f"The average costs: ", total_costs/boards)
print(f"The average nodes/sec: ", total_nodes_per_sec/boards)
print(f"The average effective branching factor: ", total_branchings/boards)

df1 = pd.DataFrame.from_dict({"Initial_Boards":initial_boards, "Final_Boards":final_boards, "Times Taken":times_taken, "Nodes/sec":nodes_time, "Branching Factor":branching_factors, "Cost":final_costs})
df1.to_csv('admissible_heuristic_data.csv',header = True, index = False)
