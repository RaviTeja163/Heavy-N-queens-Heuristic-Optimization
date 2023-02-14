# find all solutions for a board of size n
# generate a random board of size n
# place the queen weights that are present on the random board to the queen positions on all the solutions board
# select the board with minimum cost.
import random
import numpy as np
import time
import pandas as pd
res = []
def solveBoard(board, column):
    n = len(board)
    # if all the queens are placed 
    if (column == n):
        pos = []
        for i in board:
            for j in range(len(i)):
                if i[j] > 0:
                    pos.append(j)
        res.append(pos)
        return True
    
    result = False
    for i in range(n):
        if (checkValidity(board, i, column)):
            board[i][column] = 1
            result = solveBoard(board,column+1) or result
            board[i][column] = 0

    return result

def get_H_Value(board):
    h = 0
    horizontal_attacks = 0
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            # look for a queen
            if board[j][i] > 0:
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
                # k = 1
                # try:
                #     while not (i-k < 0):
                #         if board[i-k][j] > 0:
                #             h += 1
                #         k += 1
                # except:
                #     pass

                # Downward
                # k = 1
                # try:
                #     while not (i+k < 0):
                #         if board[i+k][j] > 0:
                #             h += 1
                #         k += 1
                # except:
                #     pass

                # Left
                k = 1
                try:
                    while not (j-k < 0):
                        if board[i][j-k] > 0:
                            h += 1
                            horizontal_attacks += 1
                        k += 1
                except:
                    pass

                # Right
                k = 1
                try:
                    while not (j+k < 0):
                        if board[i][j+k] > 0:
                            h += 1
                            horizontal_attacks += 1
                        k += 1
                except:
                    pass

    return int(h/2), int(horizontal_attacks/2)

def getAttacksByQueen(q_wt,board):
    attacks_By_Queen = 0
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            # look for a queen
            if board[i][j] == q_wt:
                # we look for the heaviest or the lightest queen
                # Now attack can occur from 8 directions. 
                # Top Left, Top Right, Bottom Left, Bottom Right, Upward, Downward, Left, Right

                # Top Left
                k = 1
                try:
                    while not (i-k < 0 or j-k < 0):
                        if board[i-k][j-k] > 0:
                            attacks_By_Queen += 1
                        k += 1
                except:
                    pass

                # Top Right
                k = 1
                try:
                    while not (i-k < 0 or j+k < 0):
                        if board[i-k][j+k] > 0:
                            attacks_By_Queen += 1
                        k += 1
                except:
                    pass

                # Bottom Left
                k = 1
                try:
                    while not (i+k < 0 or j-k < 0):
                        if board[i+k][j-k] > 0:
                            attacks_By_Queen += 1
                        k += 1
                except:
                    pass

                # Bottom Right
                k = 1
                try:
                    while not (i+k < 0 or j+k < 0):
                        if board[i+k][j+k] > 0:
                            attacks_By_Queen += 1
                        k += 1
                except:
                    pass

                # Upward
                # k = 1
                # try:
                #     while not (i-k < 0):
                #         if board[i-k][j] > 0:
                #             h += 1
                #         k += 1
                # except:
                #     pass

                # Downward
                # k = 1
                # try:
                #     while not (i+k < 0):
                #         if board[i+k][j] > 0:
                #             h += 1
                #         k += 1
                # except:
                #     pass

                # Left
                k = 1
                try:
                    while not (j-k < 0):
                        if board[i][j-k] > 0:
                            attacks_By_Queen += 1
                        k += 1
                except:
                    pass

                # Right
                k = 1
                try:
                    while not (j+k < 0):
                        if board[i][j+k] > 0:
                            attacks_By_Queen += 1
                        k += 1
                except:
                    pass

    return attacks_By_Queen

def checkValidity(board, row, column):
    n = len(board)

    for i in range(column):
        if (board[row][i]):
            return False

    r = row
    c = column
    while r >= 0 and c >= 0:
        if (board[r][c]):
            return False
        r -= 1
        c -= 1

    r = row
    c = column
    while c >= 0 and r < n:
        if (board[r][c]):
            return False
        r += 1
        c -= 1
    return True


def findAllSolutions(n):
    res.clear()
    board = [[0 for i in range(n)] for i in range(n)]
    solveBoard(board,0)
    res.sort()
    return res

def get_Random_Board(n):
    board_size = n
    board = np.array([[0 for i in range(board_size)] for i in range(board_size)])
    r = random.sample(range(1,10),board_size)
    for i in range(board_size):
        row = random.randint(0,board_size-1)
        board[row][i] = r[i]
    return board


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

def getCost(q_pos, q_wt, solution):
    sum = 0
    for i in range(len(q_pos)):
        tiles_moved = abs(q_pos[i] - solution[i])
        sum += q_wt[i]**2 * tiles_moved
    return sum

def getQueensOnEdges(board):
    q_on_edges = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] > 0:
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board) - 1:
                    q_on_edges += 1
    return q_on_edges
        

def heaviestQueen(board):
    return max(get_Q_Weight(board))

def lightestQueen(board):
    return min(get_Q_Weight(board))

def pairOfAttackingQueens(board):
    h_value,_ = get_H_Value(board)
    return h_value

def getHorizontalAttacks(board):
    _,horizontal_attacks = get_H_Value(board)
    return horizontal_attacks

def queensOnEdges(board):
    return getQueensOnEdges(board)

def attacksByHeaviestQueen(board):
    q_wt = get_Q_Weight(board)
    max_q_wt = max(q_wt)
    return getAttacksByQueen(max_q_wt, board)

def attacksByLightestQueen(board):
    q_wt = get_Q_Weight(board)
    min_q_wt = min(q_wt)
    return getAttacksByQueen(min_q_wt, board)

def ratioOfQueenWithAllAttacks(board):
    h = pairOfAttackingQueens(board)
    atByHQ = attacksByHeaviestQueen(board)
    atByLQ = attacksByLightestQueen(board)
    if h == 0:
        return 0,0
    else:
        return atByHQ/h, atByLQ/h

def ratioOfQueenWithTotalWt(wt, board):
    sum_of_all_queens = np.sum(get_Q_Weight(board))
    return wt/sum_of_all_queens


if __name__ == "__main__":
    initial_boards = []
    # final_boards = []
    final_costs = []
    times = []
    heaviest_queens = []
    heaviest_queens_log = []
    lightest_queens = []
    lightest_queens_log = []
    # q_1 = []
    # q_2 = []
    # q_3 = []
    # q_4 = []
    # q_5 = []
    # q_1_pos = []
    # q_2_pos = []
    # q_3_pos = []
    # q_4_pos = []
    # q_5_pos = []
    # q_1_attacks = []
    # q_2_attacks = []
    # q_3_attacks = []
    # q_4_attacks = []
    # q_5_attacks = []
    # q_1_moves = []
    # q_2_moves = []
    # q_3_moves = []
    # q_4_moves = []
    # q_5_moves = []
    h_queen_wt_ratios = []
    l_queen_wt_ratios = []
    total_wts = []
    total_wts_log = []
    # total_wts_25 = []
    # total_wts_50 = []
    # total_wts_75 = []
    standard_deviations_weight = []
    range_of_weights = []
    mean_wts = []
    median_wts = []
    attacks_by_heaviest_queen = []
    attacks_by_heaviest_queen_log = []
    attacks_by_lightest_queen = []
    heaviest_queen_attacks_ratio = []
    heaviest_queen_attacks_ratio_log = []
    lightest_queen_attacks_ratio = []
    queens_on_edges = []    
    horizontal_attacks = []
    # sum_of_attacks_and_weights = []
    # hq_distance_from_t_edge_and_weight = []
    # lq_distance_from_t_edge_and_weight = []
    possible_moves = []
    n = 5
    tic = time.time()
    for i in range(50000):
        initial_board = get_Random_Board(n)
        q_pos = get_Q_Positions(initial_board)
        q_wt = get_Q_Weight(initial_board)
        # q_1.append(q_wt[0])
        # q_2.append(q_wt[1])
        # q_3.append(q_wt[2])
        # q_4.append(q_wt[3])
        # q_5.append(q_wt[4])
        # q_1_pos.append(q_pos[0])
        # q_2_pos.append(q_pos[1])
        # q_3_pos.append(q_pos[2])
        # q_4_pos.append(q_pos[3])
        # q_5_pos.append(q_pos[4])
        if np.log(np.sum(q_wt)) and np.log(np.max(q_wt)) and np.log(np.min(q_wt)) and np.log(attacksByHeaviestQueen(initial_board)) and np.log(ratioOfQueenWithAllAttacks(initial_board)[0]):
            start = time.time()
            print("Iteration = ", i+1)
            cost = []
            # initial_board = np.array([[0, 0, 0, 6, 0],
            #                           [0, 0, 0, 0, 0],
            #                           [1, 0, 0, 0, 9],
            #                           [0, 4, 0, 0, 0],
            #                           [0, 0, 5, 0, 0]])
    
            solutions = findAllSolutions(n)
            # print(solutions)
            for j in range(len(solutions)):
                cost.append(getCost(q_pos, q_wt, solutions[j]))
            final_costs.append(np.min(cost))
            # solution = []
            # for i,j in enumerate(cost):
            #     if j == np.min(cost):
            #         solution = solutions[i]
            # tiles_moved = []
            # for i in range(len(solution)):
            #     tiles_moved.append(np.abs(q_pos[i] - solution[i]))
            # q_1_moves.append(tiles_moved[0])
            # q_2_moves.append(tiles_moved[1])
            # q_3_moves.append(tiles_moved[2])
            # q_4_moves.append(tiles_moved[3])
            # q_5_moves.append(tiles_moved[4])
            cost.clear()
            initial_boards.append(np.array(initial_board))
            stop = time.time()
            times.append(stop - start)
            heaviest_queens.append(heaviestQueen(initial_board))
            lightest_queens.append(lightestQueen(initial_board))
            h_queen_wt_ratios.append(ratioOfQueenWithTotalWt(np.max(q_wt),initial_board))
            l_queen_wt_ratios.append(ratioOfQueenWithTotalWt(np.min(q_wt),initial_board))
            total_wts.append(np.sum(q_wt))
            # total_wts_25.append(0.25 * np.sum(q_wt))
            # total_wts_50.append(0.5 * np.sum(q_wt))
            # total_wts_75.append(0.75 * np.sum(q_wt))
            standard_deviations_weight.append(np.std(q_wt))
            range_of_weights.append(np.max(q_wt) - np.min(q_wt))
            mean_wts.append(np.mean(q_wt))
            median_wts.append(np.median(q_wt))
            attacks_by_heaviest_queen.append(attacksByHeaviestQueen(initial_board))
            attacks_by_lightest_queen.append(attacksByLightestQueen(initial_board))
            heaviest_queen_attacks_ratio.append(ratioOfQueenWithAllAttacks(initial_board)[0])
            lightest_queen_attacks_ratio.append(ratioOfQueenWithAllAttacks(initial_board)[1])
            queens_on_edges.append(getQueensOnEdges(initial_board))
            horizontal_attacks.append(getHorizontalAttacks(initial_board))
            total_wts_log.append(np.log(np.sum(q_wt)))
            heaviest_queens_log.append(np.log(np.max(q_wt)))
            lightest_queens_log.append(np.log(np.min(q_wt)))
            attacks_by_heaviest_queen_log.append(np.log(attacksByHeaviestQueen(initial_board)))
            heaviest_queen_attacks_ratio_log.append(np.log(ratioOfQueenWithAllAttacks(initial_board)[0]))
        else:
            continue
        
        # possible_moves.append(n-1)


        # atcks = []
        # for i in range(len(q_wt)):
        #     atcks.append(getAttacksByQueen(q_wt[i], initial_board))
            # print(atcks)
        # q_1_attacks.append(atcks[0])
        # q_2_attacks.append(atcks[1])
        # q_3_attacks.append(atcks[2])
        # q_4_attacks.append(atcks[3])
        # q_5_attacks.append(atcks[4])
        
        # sum_of_attacks_and_weights.append(np.sum(atcks))
        
        # hq_distance_from_t_edge = 0
        # lq_distance_from_t_edge = 0

        # for i,j in enumerate(q_wt):
        #     if j == np.max(q_wt):
        #         hq_distance_from_t_edge = q_pos[i]
        #     if j == np.min(q_wt):
        #         lq_distance_from_t_edge = q_pos[i]
        
        # hq_distance_from_t_edge_and_weight.append(hq_distance_from_t_edge * np.max(q_wt)**2)
        # lq_distance_from_t_edge_and_weight.append(lq_distance_from_t_edge * np.min(q_wt)**2)
        

    toc = time.time()
    print("The time taken", int(toc - tic), "secs")

    # print(initial_boards)
    # print(final_costs)
    # print(times)
    # print(queens_On_Edges)
    # print(pair_Of_Attacking_Queens)
    # print(attacks_By_Heaviest_Queens)
    # print(attacks_By_Lightest_Queens)
    # print(h_queen_attack_ratios)
    # print(l_queen_attack_ratios)
    # print(horizontal_attacks)
    # print(heaviest_Queens)
    # print(lightest_Queens)
    # print(total_wts)
    # print(h_queen_wt_ratios)
    # print(l_queen_wt_ratios)
    # print(standard_deviations)
    # print(range_of_weights)
    # print(mean_wts)
    # print(median_wts)
    # print(sum_of_attacks_and_weights)

    # print(hq_distance_from_t_edge_and_weight)
    # print(lq_distance_from_t_edge_and_weight)
    # print(q_1_moves)
    # print(q_2_moves)
    # print(q_3_moves)
    # print(q_4_moves)
    # print(q_5_moves)

# Collect Data

# df = pd.DataFrame.from_dict({"Initial_Boards":initial_boards,"Pair of Attacking Queens":pair_Of_Attacking_Queens, "Total_Weights":total_wts, "Total_Weights_25%":total_wts_25, "Total_Weights_50%":total_wts_50, "Total_Weights_75%":total_wts_75, "Mean_Weights":mean_wts, "Median_Weights": median_wts, "Heaviest_Queen": heaviest_Queens, "Lightest_Queens": lightest_Queens, "Range_Of_Weights": range_of_weights, "Standard_Deviations_Of_Weights":standard_deviations_weight, "Final_Costs":final_costs})
# df.to_csv('data5by5_v4.csv',header = True, index = False)
# df.to_excel('data5by5_v4.xlsx',header = True, index = False)

# df = pd.DataFrame.from_dict({"Initial_Boards":initial_boards,"Total Weights":total_wts, "Total Weights 25":total_wts_25, "Total Weights 50":total_wts_50, "Total Weights 75":total_wts_75, "Heaviest Queens": heaviest_Queens, "Lightest Queens": lightest_Queens, "Attacks By Heaviest Queen":attacks_by_heaviest_queen, "Heaviest_Queen_Attacks_Ratio":heaviest_queen_attacks_ratio,"Sum Of Attacks * Weight":sum_of_attacks_and_weights, "Final Costs":final_costs})
# df.to_csv('Data_5by5_v8.csv',header = True, index = False)

# df = pd.DataFrame.from_dict({"Initial_Boards":initial_boards,"Total Weights":total_wts, "Total Weights 25":total_wts_25, "Total Weights 50":total_wts_50, "Total Weights 75":total_wts_75, "Heaviest Queens": heaviest_Queens, "Lightest Queens": lightest_Queens, "Attacks By Heaviest Queen":attacks_by_heaviest_queen, "Heaviest_Queen_Attacks_Ratio":heaviest_queen_attacks_ratio,"Sum Of Attacks * Weight":sum_of_attacks_and_weights,"lq_distance_from_t_edge_and_weight":lq_distance_from_t_edge_and_weight, "hq_distance_from_t_edge_and_weight":hq_distance_from_t_edge_and_weight,"Final Costs":final_costs})
# df.to_csv('Data_5by5_v9.csv',header = True, index = False)

# df = pd.DataFrame.from_dict({"Initial_Boards":initial_boards, "Total_Weights":total_wts, "Queens_1":q_1, "Queens_2":q_2, "Queens_3":q_3, "Queens_4":q_4, "Queens_5":q_5, "Queens_1_Moves":q_1_moves, "Queens_2_Moves":q_2_moves, "Queens_3_Moves":q_3_moves, "Queens_4_Moves":q_4_moves, "Queens_5_Moves":q_5_moves, "Mean_Weights":mean_wts, "Attacks_By_Heaviest_Queens":attacks_by_heaviest_queen, "Heavies_Queen_Attacks_Ratios":heaviest_queen_attacks_ratio, "Final_Costs":final_costs})
# df.to_csv('Data_5by5_v11.csv',header = True, index = False)

# df = pd.DataFrame.from_dict({"Initial_Boards":initial_boards, "Total_Weights":total_wts, "Queens_1":q_1, "Queens_2":q_2, "Queens_3":q_3, "Queens_4":q_4, "Queens_5":q_5, "Queens_1_Attacks":q_1_attacks, "Queens_2_Attacks":q_2_attacks, "Queens_3_Attacks":q_3_attacks, "Queens_4_Attacks":q_4_attacks, "Queens_5_Attacks":q_5_attacks, "Queen_1_Positions":q_1_pos, "Queen_2_Positions":q_2_pos, "Queen_3_Positions":q_3_pos, "Queen_4_Positions":q_4_pos, "Queen_5_Positions":q_5_pos,"Final_Costs":final_costs})
# df.to_csv('Data_5by5_v15.csv',header = True, index = False)

# df = pd.DataFrame.from_dict({"Initial Boards": initial_boards, "Total Weights":total_wts, "Mean Weights":mean_wts, "Median Weights":median_wts,"Heaviest Queen":heaviest_queens,"Lightest Queens":lightest_queens, "Range of Weights":range_of_weights, "Weighs Standard Deviation":standard_deviations_weight, "Heaviest Queen Weight Ratis":h_queen_wt_ratios, "Lightest Queen Weight Ratios":l_queen_wt_ratios, "Queens on Edges":queens_on_edges, "Horizontal Attacks": horizontal_attacks, "Attacks By Heaviest Queen": attacks_by_heaviest_queen, "Attacks By Lightest Queens":attacks_by_lightest_queen, "Heaviest Queens Attacks Ratio": heaviest_queen_attacks_ratio, "Lightest Queens Attacks Ratio":lightest_queen_attacks_ratio, "Final Costs": final_costs})
# df.to_csv('Data_5by5_v18.csv',header = True, index = False)

df = pd.DataFrame.from_dict({"Initial Boards": initial_boards, "Total Weights^2":np.square(total_wts), "Heaviest Queen^2":np.square(heaviest_queens),"Lightest Queens^2":np.square(lightest_queens), "Attacks By Heaviest Queen^2": np.square(attacks_by_heaviest_queen), "Heaviest Queens Attacks Ratio^2": np.square(heaviest_queen_attacks_ratio), "Total Weights_log": total_wts_log, "Heaviest Queen_log": heaviest_queens_log,"Lightest Queens_log": lightest_queens_log, "Attacks By Heaviest Queen_log": attacks_by_heaviest_queen_log, "Heaviest Queens Attacks Ratio_log": heaviest_queen_attacks_ratio_log, "Final Costs": final_costs})
df.to_csv('Data_5by5_v21.csv',header = True, index = False)