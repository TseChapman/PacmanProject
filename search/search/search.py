# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    # stack stores tuple(x,y) and the current path
    stack = Stack()
    visited = []
    currentPath = []

    # Need to make sure that startState != GoalState
    if problem.isGoalState(problem.getStartState()):
        return currentPath

    stack.push((problem.getStartState(), currentPath))

    # Keep looping until a path to goal state is searched or stack is empty
    while(True):
        # This means that no solution is found
        if stack.isEmpty():
            return []

        # current State info
        coord,currentPath = stack.pop()
        visited.append(coord)

        if problem.isGoalState(coord):
            return currentPath

        # Successors of the current state
        successors = problem.getSuccessors(coord)

        # If successors not None
        if successors:
            for neighbor in successors:
                # If the neighbor's coordinate is not in visited list then
                # calculate updated path
                if neighbor[0] not in visited:
                    updatedPath = currentPath + [neighbor[1]] # Add the next direction to the path
                    stack.push((neighbor[0], updatedPath)) # Add the update path and neighbor into the stack for later loops


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue

    # queue stores tuple(x,y) and the current path
    queue = Queue()
    visited = [] # list of visited coordinates
    currentPath = [] # used in loop, path result

    # Check if start state is goal state
    if problem.isGoalState(problem.getStartState()):
        return currentPath # return empty path

    # Initialize queue with the start state and empty path
    queue.push((problem.getStartState(), []))

    while(True):
        if queue.isEmpty(): # If queue is empty, it means there aren't any goal state in the graph
            return []

        # Get coordinate and current path from the queue
        coord, currentPath = queue.pop()
        visited.append(coord) # add the coordinate as visited

        # If the coordinate is the goal state, return the current path as result path
        if problem.isGoalState(coord):
            return currentPath

        # If the coordinate is not the goal state, get prepare for next loop.
        # get successors/(neighbors coordinate, direction) from the popped coordinate
        successors = problem.getSuccessors(coord)

        if successors: # if there is a successor
            for neighbor in successors: # loop through the neighbor(s) in the successor(s) 
                neighborCoord = neighbor[0] # Get the coordinate of the neighbor
                # Makesure neighbor's coordinate is not visited and neighbor's coordinate is not in future state in the queue
                if neighborCoord not in visited and neighborCoord not in (node[0] for node in queue.list):
                    updatedPath = currentPath + [neighbor[1]] # update path = current path + neighbor's direction
                    queue.push((neighbor[0], updatedPath)) # add to the queue for later loops

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    # Priority queue for uniform cost search
    # prioritize on the cost of the action
    queue = PriorityQueue()

    visited = [] # list of visited coordinate
    currentPath = [] # used in loop. result path

    # check if start state is goal state
    if problem.isGoalState(problem.getStartState()):
        return currentPath

    # Initialize 0 cost, and empty path
    queue.push((problem.getStartState(), []), 0) # cheapest priority

    while(True):
        if queue.isEmpty(): # If queue is empty, it means there aren't any goal state in the graph
            return []

        # get the coordinate from the lowest cost from the queue
        coord, currentPath = queue.pop()
        visited.append(coord) # set the coordinate as visited

        # Check if the coordinate is goal state
        if problem.isGoalState(coord):
            return currentPath

        # if not the goal state, prepare for later loops
        # get successors from the coordinate
        successors = problem.getSuccessors(coord)

        if successors: # if there are any successor, loop through the neighbor(s) in successor
            for neighbor in successors:
                # If the neighbor's coordinate is not visited and the coordinate is not in the queue.
                if neighbor[0] not in visited and (neighbor[0] not in (node[2][0] for node in queue.heap)):
                    # Update the path and get the cost to take the update path.
                    updatedPath = currentPath +[neighbor[1]]
                    priority = problem.getCostOfActions(updatedPath)
                    # add the neighbor's coordinate, update path, and it's cost to the queue
                    queue.push((neighbor[0], updatedPath), priority) 
                # If the neighbor's coordinate is not visited but the coordinate in the queue.
                elif neighbor[0] not in visited and (neighbor[0] in (node[2][0] for node in queue.heap)):
                    # Traverse again to get the previousPriority
                    for node in queue.heap:
                        if node[2][0] == neighbor[0]:
                            previousPriority = problem.getCostOfActions(node[2][1])
                    
                    updatedPriority = problem.getCostOfActions(currentPath + [neighbor[1]])
                    # Check if the update path's priority is less than previous priority
                    if previousPriority > updatedPriority:
                        # if less than, then update the path for the neighbor and add the updated priority
                        updatedPath = currentPath + [neighbor[1]]
                        queue.update((neighbor[0], updatedPath), updatedPriority)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# f(n) function
def f(problem, node, heuristic):
    # f(n) = g(n) + h(n)
    "*** YOUR CODE HERE ***"
    # g(n) = cost of taking action to the 'next state'
    # h(n) = heuristic of taking to the 'next state'
    return problem.getCostOfActions(node[1]) + heuristic(node[0], problem)

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    # Use Priority Queue
    queue = PriorityQueue() # stores ((coordinate, path), f(n)); f(n) is priority

    visited = [] # list of visited coordinates
    currentPath = []

    # Check if start state is goal state
    if problem.isGoalState(problem.getStartState()):
        return currentPath

    # Queue takes f(n) = g(n) + h(n) as priority cost
    startNode = problem.getStartState()
    # initialize queue: ((start coordinate, empty path), f((start coordinate, empty path), heuristic))
    queue.push((startNode,[]), f(problem, (startNode,[]), heuristic))

    while(True):
        if queue.isEmpty(): # If queue is empty, it means no goal state is found in the graph
            return []

        # get the coordinate and current path to that coordinate
        coord, currentPath = queue.pop()

        # Only activate this if statement when coord is visited and
        # a lower cost path has been found
        if coord in visited:
            continue

        visited.append(coord) # set the coordinate as visited

        # Check if the coordinate is goal state
        if problem.isGoalState(coord):
            return currentPath

        # If it is not a goal state, get the successors of the coordinate
        successors = problem.getSuccessors(coord)

        if successors:
            for neighbor in successors: # traverse the neighbor if there is any successor
                if neighbor[0] not in visited: # Check if coord is visited
                    # update the path and enqueue with the new priority of f((neighbor's coordinate, update path), heuristic)
                    updatedPath = currentPath + [neighbor[1]]
                    queue.push((neighbor[0], updatedPath), f(problem, (neighbor[0], updatedPath), heuristic))

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
