# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        foods = currentGameState.getFood()
        positions = list(successorGameState.getPacmanPosition())
        distance = -999999999999999 # Initialize as negative infinity

        foodList = foods.asList()

        # If the next action is to stop return negative infinity
        if action == 'Stop':
            return distance

        # If any ghost is super close to pacman, return negative infinity
        for ghostState in newGhostStates:
            if ghostState.getPosition() == tuple(positions) and (ghostState.scaredTimer == 0):
                return distance

        # Find the closest food
        for food in foodList:
            currentDistance = -1 * manhattanDistance(positions, food)
            if (currentDistance > distance):
                distance = currentDistance
        # Return the distance from the closest food
        return distance

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        def minMaxSearch(gameState, agentIndex, depth):
            result = []

            # If no legal action return the evalualtion function with the action 0
            if not gameState.getLegalActions(agentIndex):
                return self.evaluationFunction(gameState),0

            # If the depth reaches inputed depth without finding result action, return the evalualtion function with the action 0
            if depth == self.depth:
                return self.evaluationFunction(gameState),0

            # All ghosts have finished a round:
            # 1. increase the depth
            # 2. nextAgent = pacman index #
            if agentIndex == gameState.getNumAgents() - 1:
                depth += 1
                nextAgent = self.index
            else:
                nextAgent = agentIndex + 1

            # Check through actions and recursively determine next action and value
            for action in gameState.getLegalActions(agentIndex):
                if not result:
                    nextValue = minMaxSearch(gameState.generateSuccessor(agentIndex,action), nextAgent, depth)

                    result.append(nextValue[0])
                    result.append(action)
                else:
                    # Check the previous value and change the result if:
                    # 1. Current agent index equals self.index, then if next value/result is bigger than previous value/result
                    #    update the result to next value.
                    # 2. Current agent index is not equals self.index, 
                    #    then if next value/result is less than previous value/result,
                    #    update the result to next value
                    previousValue = result[0]
                    nextValue = minMaxSearch(gameState.generateSuccessor(agentIndex, action), nextAgent, depth)

                    if agentIndex == self.index:
                        if nextValue[0] > previousValue:
                            result[0] = nextValue[0]
                            result[1] = action
                    else:
                        if nextValue[0] < previousValue:
                            result[0] = nextValue[0]
                            result[1] = action
            return result

        # Return the action from all those recursive call of miniMax search
        return minMaxSearch(gameState, self.index,0)[1]

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        # a for alpha, b for beta

        # Find the min value for the agent
        def minVal(state, agentIndex, depth, a, b):
            if agentIndex == state.getNumAgents():
                # Find max value from agentIndex = 0 and increase one level in depth
                return maxVal(state, 0, depth + 1, a, b)

            # Initialize value = None
            value = None

            # Travers through the actions from current agent index
            for action in state.getLegalActions(agentIndex):
                # traversing the successor from different action
                successor = minVal(state.generateSuccessor(agentIndex, action), agentIndex + 1, depth, a, b)
                # First traversal, value is None
                if value is None:
                    value = successor
                else: # After first traversal, value is the min between current successor and current value
                    value = min(value, successor)

                # If alpha is not None and value is less than alpha, return the min value
                if a is not None and value < a:
                    return value
                # If beta is None, update the beta equal to value
                if b is None: 
                    b = value
                else: # else, beta is not None, find update beta equal to the min between current beta and value
                    b = min(b, value)

            # Check after traversal, value is not None, return the value (We found the min)
            if value is not None:
                return value
            else: # Else return the evaluation function of the input state
                return self.evaluationFunction(state)

        # Find the max value for the agent
        def maxVal(state, agentIndex, depth, a, b):
            # Make sure that depth does not exceed inputed depth
            if depth > self.depth:
                return self.evaluationFunction(state)

            # Initialize value equal None
            value = None

            # Travers through the actions from current agent index
            for action in state.getLegalActions(agentIndex):
                # After finding the min value from the agent and actions
                successor = minVal(state.generateSuccessor(agentIndex, action), agentIndex + 1, depth, a, b)
                # Determine the max value between curent value and successor
                value = max(value, successor)

                # If beta is not None and value is greater than beta, return the found max value
                if b is not None and value > b:
                    return value

                # Update alpha equal the max between current alpha and value
                a = max(a, value)

            # After traversing, if value is still None, return the max value
            if value is not None:
                return value
            else: # else return the evaluation funtion of the state
                return self.evaluationFunction(state)

        # Start of the alpha beta search
        def alphaBeta(state):
            # Initialize all value equal to None
            value = optimalAction = None
            a = b = None

            # Find actions from agentIndex, which is 0 from start
            for action in state.getLegalActions(0):
                # Assume root is max agent, find the value with the max value from 
                # all those min agent from min value found from the successors of agentIndex = 0
                value = max(value, minVal(state.generateSuccessor(0, action), 1, 1, a, b))

                # makesure that if alpha is still none, then alpha = value, and optimalAction = action
                if a is None:
                    a = value
                    optimalAction = action
                else: # if alpha is not none, alpha = max between current alpha and value. And optimalAction = action if value is greater than alpha
                    a, optimalAction = max(value, a), action if value > a else optimalAction
            return optimalAction
        
        # Return the optimalAction from alphaBeta function
        return alphaBeta(gameState)

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        # Max agent = Pacman's index, Min agent = Ghost
        def expectiMax(gameState, agentIndex, depth):
            result = []

            # If no legal action is available and depth is equal inputed depth, 
            # then return return a tuple of evaluationFunction with action 0
            if not gameState.getLegalActions(agentIndex) or depth == self.depth:
                return self.evaluationFunction(gameState),0

            # Determine depth and nextAgent
            if agentIndex == gameState.getNumAgents() - 1:
                depth += 1
                nextAgent = self.index
            else:
                nextAgent = agentIndex + 1

            # Travers the action from current agentIndex
            for action in gameState.getLegalActions(agentIndex):
                # If the result is empty, then recuresively find result from nextAgent
                if not result:
                    nextValue = expectiMax(gameState.generateSuccessor(agentIndex, action), nextAgent, depth)
                    # Determine whether or not agentIndex reaches self.index
                    if agentIndex != self.index:
                        # Calculate average and apend to result
                        result.append(float(1.0/len(gameState.getLegalActions(agentIndex))) * nextValue[0])
                        result.append(action)
                    else:
                        result.append(nextValue[0])
                        result.append(action)
                else:
                    # Check if previous value is differ from next value
                    previousValue = result[0]
                    nextValue = expectiMax(gameState.generateSuccessor(agentIndex, action), nextAgent, depth)

                    if agentIndex == self.index:
                        if nextValue[0] > previousValue:
                            result[0] = nextValue[0]
                            result[1] = action
                    else:
                        result[0] = result[0] + float(1.0/len(gameState.getLegalActions(agentIndex))) * nextValue[0]
                        result[1] = action
            return result

        # Return the final result from all those recursive call in expectiMax function
        return expectiMax(gameState, self.index, 0)[1]

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    # My Thought: 
    # After testing a few scoring methods, 
    # I found take the basic current score plus the maximum in manhattan distance will score the best.
    # maximum in manhattan distance = closest because it is inputed as negative and 
    # manhattan distance function returns in absolute value

    # A position list of the pacman
    pacmanPosition = list(currentGameState.getPacmanPosition())
    # Foodlist
    foodList = currentGameState.getFood().asList()
    foodDis = []

    # Find the manhattanDistance from pacman position to food
    for food in foodList:
        foodDis.append(-1 * manhattanDistance(pacmanPosition, food))

    # If somehow no food in the game, append 0 for placeholder
    # Search fails
    if not foodDis:
        foodDis.append(0)

    # Return the currentState's score plus the max of the manhattanDistance from pacman's position to food
    return currentGameState.getScore() + max(foodDis)

# Abbreviation
better = betterEvaluationFunction

