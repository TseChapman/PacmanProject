Questions Solution Author: Cheuk-Hang Tse
Course: CSS 382 Introduction to AI
Professor: Pisan

Question 1 Work:
I implement Depth First Search (DFS) using stack.
First, I have 3 list:
1. visited, a list that store visited states.
2. currentPath, a list that store path that are taken from each loop.
3. stack, a list that use to query the neighbors in state's successors.
stack initialize with start state

Second, implement the DFS loop algorithm:
pop from the stack and check goal state, if the state in goal state, return the currentPath
else, get successors from state and add to stack if the neighbor from successors is not visited.

Keep looping until state is in goal state.

Question 2 Work:
I implement Breadth First Search (BFS) using queue.
First, I have 3 list:
1. visited, a list that store visited states.
2. currentPath, a list that store path that are taken from each loop.
3. queue, a list that use to query the neighbors in state's successors.
queue initialize with start state

Second, implement the BFS loop algorithm:
pop from the queue, which should be the closes state, and check goal state, 
if the state in goal state, return the currentPath.
else, get successors from state and add to queue if the neighbor from successors is not visited.

Keep looping until the popped state is in goal state

Question 3 Work:
I implement Uniform Cost Search using Priority Queue.
First, I have 3 list:
1. visited, a list that store visited states.
2. currentPath, a list that store path that are taken from each loop.
3. queue (priority queue), a list that use to query the neighbors in state's successors.
queue structure = ((coordinate, path), cost)
queue initialize with start state with the cost of 0

Second, implement the Uniform Cost Search loop algorithm:
pop from the queue, which should be the state that have taken the cheapest path, and check goal state, 
if the state in goal state, return the currentPath.
else, get successors from state and 
add to queue if the neighbor from successors is not visited and neighbor is not in queue.heap. 
Also, check the if it is the cheapest path

Keep looping until the popped state is in goal state

Question 4 Work:
I implement A* Search using Priority Queue.
First, I have 3 list:
1. visited, a list that store visited states.
2. currentPath, a list that store path that are taken from each loop.
3. queue (priority queue), a list that use to query the neighbors in state's successors.
queue structure = ((coordinate, path), cost)
queue initialize with start state with the cost of function f: f(n) = g(n) + h(n)
g(n) = problem.getCostOfAction(path)
h(n) = heuristic(coordinate, problem)

Second, implement the Uniform Cost Search loop algorithm:
pop from the queue, which should be the state that have taken the cheapest heuristic path, and check goal state, 
if the state in goal state, return the currentPath.
else, get successors from state and 
add to queue if the neighbor from successors is not visited . 

Keep looping until the popped state is in goal state

Question 5 Work:
I implement Corners Problem.
My state representation is (State's coordinate, a list of unvisited corners)
list of unvisited corners: 0 = not visited, 1 = visited

getStartState: return (startingPosition, the list of unvisited corners)

isGoalState: return False if state[1] <-- a list of unvisited corners has 0 = unvisited

getSuccessors: loop around the Directions, if the coordinate does not hit a wall, append the state to successor array
return the successor array

Question 6 Work:
Constant Heuristic: manhattan distance
implement the cornersHeuristic function:
Basically, calculate the distance from the corners to current state using manhattan Distance
return the highest distance
if the state is in goal state, return 0

Question 7 Work:
implement foodHeuristic function.
state representation: (position, foodGrid)

First, Check if the state is goal state, else continue.

Next, get the following items:
1. a list of food: foodGrid.asList()
2. the number of walls, (Define problem.heuristicInfo['wallCount'] = problem.walls.count())

Create 2 values:
1. count of food
2. distance from food

for food in the food list, ultilize the mazeDistance function and append the maze distance to distance list.
if the count of food is equal to a threshold and the wall count is bigger then break the loop.
return the max of the distance list.

Question 8 Work:
I first implement the isGoalState function from the class, AnyFoodSearchProblem, by getting the food list and
return true if the state is in the food list, else return false.

Then, I implement the findPathToClosestDot simply by using BFS from search.py





