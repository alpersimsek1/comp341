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
from util import Stack, Queue, PriorityQueue

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
    start = problem.getStartState()
    visited = set()
    s = Stack()
    moves = []
    startPoint = (start, moves, 0)
    s.push(startPoint)
    while(s.isEmpty() == False):
        cs = s.pop()
        moves = cs[1]
        isIn = checkIsIn(cs[0],visited)
        if isIn==False:
            visited.add(cs[0])
            if problem.isGoalState(cs[0]):
                return moves

            successors =successor(problem,cs[0])
            for action in successors:
                isin = checkIsIn(action[0], visited)
                if isin == False:
                    direction = action[1]
                    temp_actions = moves + direction.split()
                    new_element = (action[0], temp_actions, action[2])
                    s.push(new_element)

    return moves

def checkIsIn(a, set):
    someBool = False
    for m in set:
        if m == a:
            someBool = True
    return someBool

def successor(prob,a):
    return prob.getSuccessors(a)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    moves = []
    visited = set()
    q = Queue()
    start_node = (start, moves, 0)
    q.push(start_node)

    while (q.isEmpty()==False):
        cs = q.pop()
        moves = cs[1]
        isIn = checkIsIn(cs[0], visited)
        if isIn == False:
            visited.add(cs[0])
            if problem.isGoalState(cs[0]):
                return moves
            successors =successor(problem,cs[0])
            for action in successors:
                isin = checkIsIn(action[0], visited)
                if isin == False:
                    direction = action[1]

                    temp_actions = moves + direction.split()  # split -- converts str to list

                    new_element = (action[0], temp_actions, action[2])
                    q.push(new_element)

    return moves

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    visited = set()
    pq = PriorityQueue()
    moves = []
    startPoint = (start, moves, 0)
    pq.push(startPoint,0)
    while (pq.isEmpty() == False):
        cs = pq.pop()
        moves = cs[1]
        isIn = checkIsIn(cs[0], visited)
        if isIn == False:
            visited.add(cs[0])
            if problem.isGoalState(cs[0]):
                return moves

            successors = successor(problem, cs[0])
            for action in successors:
                isin = checkIsIn(action[0], visited)
                if isin == False:
                    direction = action[1]
                    temp_actions = moves + direction.split()
                    cost = action[2]+ cs[2]
                    e = (action[0], temp_actions, action[2])
                    pq.push(e,cost)
    return moves

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    ##LIKE UNIFORM COST BUT WITH HEURISTIC

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    visited = set()
    pq = PriorityQueue()
    moves = []
    startPoint = (start, moves, 0)
    pq.push(startPoint, 0)
    while (pq.isEmpty() == False):
        cs = pq.pop()
        moves = cs[1]
        isIn = checkIsIn(cs[0], visited)
        if isIn == False:
            visited.add(cs[0])
            if problem.isGoalState(cs[0]):
                return moves

            successors = successor(problem, cs[0])
            for action in successors:
                isin = checkIsIn(action[0], visited)
                if isin == False:
                    direction = action[1]
                    temp_actions = moves + direction.split()
                    cost = action[2] + cs[2]
                    h_cost = heuristic(action[0],problem)
                    e = (action[0], temp_actions, action[2])
                    total = cost+h_cost
                    pq.push(e, total)
    return moves


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch