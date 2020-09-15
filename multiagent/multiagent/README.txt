Project 2 - MultiAgent Solution
Author: Cheuk-Hang Tse

Question 1 Reflex Agent:
I first intialize 3 values:
	1. food: a list of food positions, later will transform into array
	2. positions: Pacman's position illustrate in the form of a list
	3. distance: initialized as negative infinity, or -999999999999999
Second, I will determine if the state reach some situation:
	1. If the next action is to stop, then return as negative infinity
	2. If any ghost is super close to pacman and ghost is not scare, then return negative infinity
At last, find the closest food in the food list. The distance will be negative manhattan distance from current position and food
Then, return the max distance
===================================================================================================================================
Question 2 MinimaxAgent:
First, I implement a minimax search function:
	1. Initialize a empty result array
	2. If the state accomplish following situation, return a tuple of (evalualtion of the current state, and action 0):
		- If no legal action is available
		- If the depth reach the inputed depth without finding result action
	3. Now calculate the depth and agentIndex after finishing a round:
		- If agentIndex reach the number of agent, depth + 1 and nextAgent = self.index
		- else, nextAgent = agentIndex + 1
	4. Next, is to check through available actions of the agent that correspond to agentIndex. 
	   Then, makesure the following situation is done:
		- If the result array is empty, recursively call the miniMax search function of the nextAgent
		  Then append the next value and action to result
		- Else, Check the previous value and change the result if:
			1) Current agent index equal to self.index, then if the nextValue/result is greater than previous
			   value/result, then update the result equal to next value
			2) Current agent index is not equal to self.index, then if the nextValue/result is less than the previous
			   value/result, update the result equal to next value
At last, I return the result's action after all those recursive call of miniMax search function
===================================================================================================================================
Question 3 AlphaBeta Agent:
I implemented 3 functions:
	1. minVal: Find the min value for the agent
	2. maxVal: Find the max value for the agent
	3. alphaBeta: The initial function for starting the alpha beta search

minVal:
	1. If the agentIndex reaches the number of agent, then return the maxVal function of
	   agent 0 and depth + 1
	2. Initialize value = None
	3. Travers through the legal action from current agent index. For each legal action, do the following step:
		1) find the successor, which is the minVal function of agentIndex + 1 and current depth
		2) If value is None (first Traversal), value = successor. Else, value = min(value, successor)
		3) Determine the situation of alpha and beta:
			- If alpha is not None and value is less than alpha, return the value (It is the min value)
			- If beta is None, update the beta equal to value. Else, the beta is not None, therefore
			  update beta equals to the minimum between current beta and value
	4. After traversal, is value is not None, return the value (we found the min). Else, return the evaluation of the state

maxVal:
	1. Makesure that the depth does not exceed inputed depth. If exceeded, return the evaluation of the state
	2. Initialize value = None
	3. Travers through the legal action from current agent index. For each legal action, do the following step: 
		1) find the successor, which is the minVal function of agentIndex + 1 and current depth
		2) The value is equal to the maximum between successor and value
		3) If beta is not None and value is greater than beta, return the found max value
		4) update alpha equal to the maximum between current alpha and value
	4. After traversing, if value is still None, return the max value. Else, return the evaluation of the current state

alphaBeta:
	1. Initialize values = None: value = optimalAction = a (for alpha) = b (for beta) = None
	2. Travers through legal actions of agent that the agent index = 0. For each action, do the following step:
		1) root/value = max(value, minVal (function) of agentIndex = 0 and depth of 1)
		2) If alpha is still none, then alpha = value, and optimalAction = action. Else, 
		   alpha = max between current alpha and value. And optimalAction = action if value is greater than alpha
	3. return the optimalAction after all those action traversal
At last, I return the optimalAction from calling alphaBeta function
===================================================================================================================================
Question 4 ExpectiMax Agent:
I implemented a expectiMax function that return the result action (The expectiMax's optimal action)

expectiMax:
	1. Initialize empty result array
	2. If no legal action is available and depth is equal inputed depth, 
	   then return return a tuple of (evaluationFunction of the current state, action = 0)
	3. Determine the depth and nextAgent:
		- If the agentIndex reaches the number of agent, reset the nextAgent = self.index and depth + 1
		- Else, nextAgent = agentIndex + 1
	4. Travers through the legal action of the agentIndex. For each action, do the following step:
		1) If the result is empty, then recuresively find result from nextAgent
			- nextValue = recursive result of expectiMax by the nextAgent
			- Determine whether or not agentIndex reaches self.index. 
			  If not reaches, calculate average of the nextValue and apend to result. 
			  Else, just append the nextValue and action to result
		2) Else: Check if the previous value is differ from next value
			- nextValue = recursive call of expextiMax by the nextAgent
			- If agentIndex equals to self.index and nextValue is greater than previous value, result = nextValue and action
			- Else, result = [previous value + average of the nextValue, action]
	5. return the result
At last, return the action from the initial call of expectiMax by self.index and 0 depth
===================================================================================================================================
Question 5 betterEvaluationFunction:
In this part, I want to use the most straightforward way to quickly finish the game by eating all the food.
	1. Initialize values:
		- pacmanPosition = list of pacman position
		- foodList = current game state's food as a list
		- foodDis = empty, stores the manhattan distance from pacman's position to food
	2. for each food in food list, appent the negative manhattan distance from pacman's position to food
	3. If somehow foodDis is still empty (Somehow no food in the game), append 0 to foodDis for placeholder
	4. return the score of current game state + the maximum in foodDis
===================================================================================================================================
