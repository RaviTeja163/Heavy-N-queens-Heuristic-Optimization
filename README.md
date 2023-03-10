# Heavy-N-queens-Heuristic-Optimization

## Greedy search for N queens
* Create a board with queens with random weights and place them randomly one in each column.
* Then find the No. of attacks on each queen to find the H value of the board and divide no of attacks by two because H is no of attacking pairs.
*	Create a H Matrix for the board. It will give the H value of board if a Queen is moved to each position in its own column.
*	Then find the good position where the H value is minimum and move the queen to that position.
*	Run this loop until the H value of the board turns out to be 0.

## A* Algorithm for N queens
*	Create a random board with N queens of random weights, one in each column.
*	Define the heuristic H to be the number of pair of queens under attack. To find the H value, for each of the queen, we traverse through all its moving directions and increment a count variable if there is any other queen in its attacking range. After continuing this process for all the queens, finally the count is divided by 2, since we require the pair of queens under attack.
*	Iterate through each column, check the presence of the queen, and store the positions and the weights of the queen in separate lists.
*	A H-matrix is formed, which gives the H value of the board if the queen in each column in moved to all the possible positions.
*	Similarly, a Cost matrix is also formed, whose values helps to determine the cost to move a queen to all positions in its column. The formula for the cost calculation of each queen is, Weight^2 * No. of tiles moved.
*	Calculate the Total cost matrix by adding the Cost and H matrices.
*	From this Total cost matrix, find the least value. And in the column in which this least value is present, move the queen in that column to the position of the least value.
*	Then recalculate the H value to this modified board.
*	Continue this process until none of the queens are in attacking positions, i.e., we get a H value of 0.

## Hill Climbing algorithm for 9/8 heavy queens
*	I choose the random restart method of the hill climbing algorithm.
*	Create a random board of size 8 with 9 queens in it.
*	Set this board as the initial node.
*	Set the time limit for the process.
*	Find all the neighbours of the initial node and calculate the cost for each neighbour, with the formula given, 100*attacking pairs + cost to move each weighted queen.
*	Find the neighbour with the least cost. If this cost in lower than the cost of the initial node, then this neighbour becomes the initial node. If not, we perform a random restart and create a new random board and set it to the initial node.
*	Continue the same process until the time limit is exceeded.
*	The final board which was set as node will be the outcome of the algorithm.

## Supervides Learning
Machine Learning techniques are feeded the data generated for the K x K Heavy Queens problem  to predict a heuristic so as to solve the board.

Features: Total Weights, Mean Weights, Median Weights, Heaviest Queen, Lightest Queens, Range Of Weights, Standard Deviations Of Weights, Heaviest Queen Wt Ratios, Lightest Queen Wt Ratios, Queens On Edges, Horizontal Attacks, Attacks By Heaviest Queen, Attacks By Lightest Queens, Heaviest Queen Attacks Ratio, Lightest Queen Attacks Ratio, Final Costs.

Initially a model is trained with the all features in ???weka??? software with m5 attribute selection method and following is the result:

TotalCost = 5.5609 ??? Total Weights
+28.5654 ??? Mean Weights
+4.2172 ??? Median Weights
+(??? 12.8935) ??? Heaviest Queen
+(??? 5.0241) ??? Lightest Queens
+(???5.1879) ??? Range Of Weights
+7.1239 ??? Standard Deviations Of Weights
+231.1929 ??? Heaviest Queen Wt Ratios
+5.3983 ??? Queens On Edges
+14.7357 ??? Attacks By Heaviest Queen
+(???2.3722) ??? Attacks By Lightest Queens
+19.7673 ??? Heaviest Queen Attacks Ratio
+(???202.6684)

The best features out of them are chosen by plotting a pearson correlation coefficient map. The features witha good correlation with the cost are chosen. Following are the good feature that are found: Total Weights, Heaviest Queen, Lightest Queens, Attacks By Heaviest Queen, Heaviest Queen Attacks Ratio.

This is the model of good features:

TotalCost = 9.6141 ??? Total Weights
+(???7.495) ??? Heaviest Queen
+(???3.5481) ??? Lightest Queens
+10.8857 ??? Attacks By Heaviest Queen
+34.8749 ??? Heaviest Queen Attacks Ratio
+(???111.8746)

A sequential multi-layer neural network model is implemented using the tensorflow module with different datasets.
