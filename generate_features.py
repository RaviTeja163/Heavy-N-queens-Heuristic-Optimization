import numpy as np
import random
import pandas as pd

def getRandomBoard(n):
    board_size = n
    board = np.array([[0 for i in range(board_size)] for i in range(board_size)])
    r = random.sample(range(1,9),board_size)
    for i in range(board_size):
        row = random.randint(0,board_size-1)
        board[row][i] = r[i]
    return np.array(board)

def get_Q_Weight(board):
    board_size = len(board)
    queen_weights = []
    for i in range(board_size):
        for j in range(board_size):
            if board[j][i] > 0:
                queen_weights.append(board[j][i])
    return queen_weights


def getQueenAttacks(q_wt,board):
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

def totalAttacks(board):
    h = 0
    d_attacks = 0
    h_attacks = 0
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
                            d_attacks += 1
                        k += 1
                except:
                    pass

                # Top Right
                k = 1
                try:
                    while not (i-k < 0 or j+k < 0):
                        if board[i-k][j+k] > 0:
                            h += 1
                            d_attacks += 1
                        k += 1
                except:
                    pass

                # Bottom Left
                k = 1
                try:
                    while not (i+k < 0 or j-k < 0):
                        if board[i+k][j-k] > 0:
                            h += 1
                            d_attacks += 1
                        k += 1
                except:
                    pass

                # Bottom Right
                k = 1
                try:
                    while not (i+k < 0 or j+k < 0):
                        if board[i+k][j+k] > 0:
                            h += 1
                            d_attacks += 1
                        k += 1
                except:
                    pass


                # Left
                k = 1
                try:
                    while not (j-k < 0):
                        if board[i][j-k] > 0:
                            h += 1
                            h_attacks += 1
                        k += 1
                except:
                    pass

                # Right
                k = 1
                try:
                    while not (j+k < 0):
                        if board[i][j+k] > 0:
                            h += 1
                            h_attacks += 1
                        k += 1
                except:
                    pass

    return int(h/2), int(d_attacks/2), int(h_attacks/2)

    
heaviest_queens = list()
lightest_queens = list()
total_weights = list()
heaviest_lightest_weight_ratios = list()
mean_weights = list()
median_weights = list()
heaviest_queen_attacks = list()
lightest_queen_attacks = list()
horizontal_attacks = list()
diagonal_attacks = list()
pair_of_attacking_queens = list()
heaviest_lightest_attack_ratios = list()
highest_number_of_attacks_by_a_queen = list()

boards = 1000
j = 0
while j < boards:
    n = 5  # size of the board
    init_board = getRandomBoard(n)
    # print("\n\nInitial Board is: ",init_board)
    attacking_queen_pair, h_attacks, d_attacks = totalAttacks(init_board)
    # print("\n\nThe attacking queen pairs are: ", attacking_queen_pair)
    if attacking_queen_pair == 0:
        continue
    else:
        q_weights = get_Q_Weight(init_board)

        # get queen weights and append
        heaviest_queens.append(np.max(q_weights))
        lightest_queens.append(np.min(q_weights))
        total_weights.append(np.sum(q_weights))
        mean_weights.append(np.mean(q_weights))
        median_weights.append(np.median(q_weights))
        heaviest_lightest_weight_ratios.append(np.max(q_weights)/np.min(q_weights))

        # get queen attacks
        atck = list()
        qw = sorted(q_weights)
        for i in qw:
            atck.append(getQueenAttacks(i,init_board))
        heaviest_queen_attacks.append(atck[-1])
        lightest_queen_attacks.append(atck[0])
        attacking_queen_pair, h_attacks, d_attacks = totalAttacks(init_board)
        pair_of_attacking_queens.append(attacking_queen_pair)
        horizontal_attacks.append(h_attacks)
        diagonal_attacks.append(d_attacks)
        if atck[0] == 0:
            heaviest_lightest_attack_ratios.append(0)
        else:
            heaviest_lightest_attack_ratios.append(atck[-1]/atck[0])
        highest_number_of_attacks_by_a_queen.append(np.max(atck))

        j += 1


df1 = pd.DataFrame.from_dict({"Heaviest Queens":heaviest_queens,"Lightest Queens":lightest_queens,"Total Weights":total_weights,"Heaviest Queen Lightest Queen Weight Ratio":heaviest_lightest_weight_ratios,"Mean Weights":mean_weights,"Median Weights":median_weights,"Heaviest Queen Attacks":heaviest_queen_attacks,"Lightest Queen Attacks":lightest_queen_attacks,"Horizontal Attacks":horizontal_attacks,"Diagonal Attacks":diagonal_attacks,"Pair Of Attacking Queens":pair_of_attacking_queens,"Heaviest Queen Lightest Queen Attack Ratio":heaviest_lightest_attack_ratios,"Highest Number Of Attacks By a Queen":highest_number_of_attacks_by_a_queen})
df1.to_csv('Features.csv',header = True, index = False)
