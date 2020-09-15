Project 3: Reinforcement Learning README.txt
Author: Cheuk-Hang Tse

Question 1(6 points): Value Iteration
Part 1: __init__ code 
	In part 1, I initialize the self.values dictionary for every iteration in self.iterations.
	- First, I have two for loops. the first one is for each iteration; the second one is for each state in that iteration.
	- For each iteration, I will initialize a values dictionary from util.Counter() for computing Q value of the state.
	- Then, start the for loop for each state in mdp.getState(). In each state, I need to check if the state is a terminal state.
	- If the state is not a terminal state, then calculate the qvalue(later implemented in theproject)
	  for the state and input it into the values dictionary.
	- After looping the states, update self.values = values
Part 2: computeQValueFromValues code
	In part 2, I implement the calculation for the Q value formula.
	- First, I initialize the return qValue = 0 and get the transition state and probability from 
	  mdp getTransitionStatesAndProbs function of the inputted state and action
	- Then travers the states and probabilities. For each state and probs, qValue keep adding up
	- Formula: qValue += prob * (R(s,a,s') + discount * V(s')); R(s,a,s') = self.mdp.getReward(state,action,nextState); V(s) = self.values[nextState]
Part 3: computeActionFromValues code
	In part 3, I implement the best action from calculating qValue.
	- First, I need to check if the inputted state is terminal state. If it is terminal state, return None
	- Then, I initialize three value: possibleAct and bestAct and bestQValue
		+ possibleAct is a set of possible action of the state from the self.mdp.getPossibleActions(state)
		+ bestAct: (the return value) best action
		+ bestQValue: Use the determine whether or not to update the bestAct
	- Traverse through the possible action and calculate the qValue for that action in inputted state
	- If the bestQValue is None or is less than the result from calculating the qValue for that action in inputted state
	  Then update bestQValue = qValue and bestAct = action
	- After traversing possible action, return the bestAct (Best Action)
===================================================================================================================================================================
Question 2(1 point): Bridge Crossing Analysis
In this question, I can only change one element so that the optimal policy causes the agent to attempt to cross the bridge.
In my thinking process, I believe that by reducing noise will allow the agent realizing by going foward will reach the terminal state
Therefore, I reduce the noise to 0.01, which successfully pass the question.
===================================================================================================================================================================
Question 3(5 points): Policies
Part 3a: Prefer the close exit(+1), risking the cliff(-10)
	- To get to the closest exit, the discount show be low and living reward should be negative
	- To risk taking cliff, the noise should be 0
Part 3b: Prefer the close exit(+1), but aviod risking the cliff(-10)
	- To get to the closest exit, the discount show be low and living reward should be negative
	- Avoid to risk taking cliff, the noise should be little above 0
Part 3c: Prefer the distant exit (+10), risking the cliff (-10)
	- To get to the distant exit, the discount should be high and living reward should be 0
	- To risk taking cliff, the noise should be 0
Part 3d: Prefer the distant exit (+10), avoiding the cliff (-10)
	- To get to the distant exit, the discount should be high and living reward should be 0
	- Avoid to risk taking cliff, the noise should be little above 0
Part 3e: Avoid both exits and the cliff (so an episode should never terminate)
	- The best way is to not move
	- Largest discount: 1
	- Living reward = 100 (large positive reward)
===================================================================================================================================================================
Question 4(5 points): Q-Learning
In this question, I will implement the q learning class just like the value iteration class
Part 1: __init__ code
	In this part, I only initialize the Q Value dictionary
	- self.qvalue = util.Counter()
Part 2: getQValue code
	In this part, I just need to return the Q value at inputted state and action
Part 3: computeValueFromQValues code
	In this part, I need to return the calculated q value for the state
	- First, I will get legal actions from problem: legalActions = self.getLegalActions(state)
	- If there is no legal action return 0 for q value
	- Initialize the return q value = 0
	- Traverse the action and find the max between current q value and the q value return from getQValue(state,action) function
	- return the max q value (After traversing actions)
Part 4: computeActionFromQValues code
	In this part, I will traverse through the action and find the best action based on q value
	- First get legal action from state and initialize bestAct = bestValue = None
	- Then, traverse through the action in legal actions and get the q value for that state and action.
	- If the bestValue is None or bestValue is less than the found q value, then update bestValue to q value and bestAct equal the action
	- After traversing, return the bestAct because this action in this state have the best q value.
Part 5: update code
	In this part, I implement the update of the dictionary self.qValue.
	- To do this, I update the qValue for the tuple of (state,action) to the following formula:
		> (1 - self.alpha) * self.getQValue(state,action) + self.alpha * (reward + self.discount * self.getValue(nextState))
		> (1 - a) * Q(s,a) + a * (R + discount * V(s'))
===================================================================================================================================================================
Question 5(3 points): Epsilon Greedy
	In this question, I will return a random action determine by flipping a coin on probability on self.epsilon
	- First, check if there is any legal action, if no legal action available, return None
	- Then do a flip coin based on self.epsilon. If true, update the action equal to a random choice of the legal action
	- Else, action will be the policy of the state
	- After determining action, return the action.
===================================================================================================================================================================
Question 6(1 point): Bridge Crossing Revisited
	- Not possible.
	It is impossible to have an epsilon and a learning rate that the optimal policy will be learned after 50 iteration.
	I have try multiple variation of combination for the epsilon and learning rate. It is not possible. And it turns out, I am correct when I do autograder.
===================================================================================================================================================================
Question 7(1 point): Q-Learning and Pacman
	My implementation for Q-Learning class successfully pass the autograder test
===================================================================================================================================================================
Question 8(3 points): Approximate Q-Learning
In this question I will implement the ApproximateQAgent class
Part 1: getQValue code
	In this part, I initialize a temporary qValue that will return after the calculate of Q Value
	- Initialize qValue = 0
	- Traverse through the features and values from self.featExtrator.getFeatures(state, action).items()
	- For each traversal, Q = Q + (weight of the feature) * V
		> qValue += self.weights[feature] * value
	- After traversing, return the qValue
Part 2: update code
	In this part, I update the weight of the feature
	- First, I calculate the difference between (R + discount * V(s')) and Q(s,a)
		> difference = reward + self.discount * self.getValue(nextState) - self.getQValue(state, action)
	- Then, start the traversal per feature and value from self.featExtractor.getFeatures(state,action).items()
	- For each traversal, update the weight for that feature to sum of current weight for the feature + alpha * difference * value
		> self.weight[feature] += self.alpha * difference * value
===================================================================================================================================================================