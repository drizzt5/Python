'''
--------------------------------

 CS 3023 Program Assignment 1 Starter Code

 System: Python 3

 Starter code author: Thomas Otani

 Functions author: Dillon Glasser

 Functions implemented: randomWalker, smartWalker, rightHandWalker, displayWithPath

 Comments: I attempted rightHandWalker recursively but finally just did it
            in a way that is intuitive to me.
--------------------------------
'''
from random import randint

OPEN_S    = '-'
BLOCKED_S = '#'
START_S   = 'S'
GOAL_S    = 'G'
PATH_S    = '.'

VISITED = -1
OPEN    = 0
BLOCKED = 1
START   = 2
GOAL    = 3
PATH    = 9


### +++++++++++++++++++++++++++++++++++++++ ###
###   Helper function to get maze string    ###
###   from a file                           ###
def getMaze(filename):

    datafile = open(filename, "r")

    maze_s = "".join(datafile.readlines())

    datafile.close()

    return maze_s
###                                         ###
### +++++++++++++++++++++++++++++++++++++++ ###

'''
Initialize the maze to the blank state. Set start and goal
and removed any markers that do not exist in the blank maze
Parameter: maze -- maze to clean
           start -- start cell (i,j)
           goal  -- goal cell  (i,j)
Return a maze in clean state
'''
def init(maze, start, goal):
    r,c = start
    maze[r][c] = START

    r,c = goal
    maze[r][c] = GOAL

    rowMax = len(maze)
    colMax = len(maze[0])

    for r in range(rowMax):
        for c in range(colMax):
            if maze[r][c] == VISITED: maze[r][c] = OPEN



'''
Convert a string representation of one row into equivalent
list represenation. Assume input r is valid.
Parameter: r -- string representation of a single row,
                e.g. "---S##"
Return  listrep -- list represenation of r
'''
def convertRow(r):

    oneRow = [OPEN] * len(r)

    for i,ch in enumerate(r):
        if ch == BLOCKED_S:
            oneRow[i] = BLOCKED

        elif ch == START_S:
            oneRow[i] = START

        elif ch == GOAL_S:
            oneRow[i] = GOAL

    return oneRow

'''
Convert the given string representation of a maze to
the list representation, a list of lists of integers

Parameter: String representation of maze
           E.g. "--S---\n##-##-\n-#-#--\n---#G#\n###---"

Return:    A list of lists of integers
           E.g. [[0,0,2,0,0,0],[1,1,0,1,1,0],[0,1,0,1,0,0],[0,0,0,1,3,1],[1,1,1,0,0,0]]
'''
def convert(maze_s):

    rows = maze_s.splitlines()

    maze = [convertRow(x) for x in rows]

    return maze


'''
Return the position of a given cell (START or GOAL) in the maze

Parameter: maze - the maze (list represenation) to locate the specified cell
           cell - either START or GOAL (int)

Return:    the position of the specified cell (r,c); None if cell is not
           START or GOAL
'''
def findCell(maze, cell):
    rowMax = len(maze)
    colMax = len(maze[0])

    for r in range(rowMax):
        for c in range(colMax):
            if maze[r][c] == cell:
                return (r,c)

    return None


'''
Convert the list representation to an equivalent string representation
Assumption: row members are one of  OPEN, BLOCKED, START, GOAL, or PATH
Parameter: row -- list representation of a single row
           open -- list of cell types to convert to OPEN_S
Return:   string equivalent of row
'''
def toString(row):
    s = ""

    for c in row:
        if c == OPEN:
            s += OPEN_S

        elif c == BLOCKED:
            s += BLOCKED_S

        elif c == START:
            s += START_S

        elif c == GOAL:
            s += GOAL_S

        elif c == PATH:
            s += PATH_S

    return s

'''
Display maze on the console output

Parameter: maze  - the maze (list representation) to display

Return:    None
'''
def display(maze):

    for row in maze:
        print(toString(row))


'''
Display maze with a given path on the console output

DO NOT MODIFY THE PARAMETERS

Parameter: maze  - the maze (list representation) to display
           path  - the path (list of (r,c)) to display

Return:    None
'''
def displayWithPath(maze, path):


    for pos in path:
        row = pos[0]
        col = pos[1]
        maze[row][col] = PATH

    display(maze)


'''
Find a path from START cell to GOAL cell

DO NOT MODIFY THE PARAMETERS

Parameter: maze  - the maze (list representation) to search
           start - position of the start cell
           goal  - position of the goal cell

Return:    the path  (list of (r,c)) from START to GOAL
           for this algorithm, the returned path is a list of all visited cells
'''
def randomWalker(maze, start, goal):

    numRows = len(maze)
    numCols = len(maze[0])
    pos = start
    path = [pos]

    while pos != goal:

        n = (pos[0] - 1, pos[1])  # Northern Coordinates
        s = (pos[0] + 1, pos[1])  # Southern
        w = (pos[0], pos[1] - 1)  # Western
        e = (pos[0], pos[1] + 1)  # Eastern

        adjacentCells = []
        # check to see if it is inbound/ check to see if cell is blocked
        if n[0] >= 0 and maze[n[0]][n[1]] != BLOCKED:
            adjacentCells.append(n)  # append available position to adjacentCells

        if s[0] < numRows and maze[s[0]][s[1]] != BLOCKED:
            adjacentCells.append(s)

        if w[1] >= 0 and maze[w[0]][w[1]] != BLOCKED:
            adjacentCells.append(w)

        if e[1] < numCols and maze[e[0]][e[1]] != BLOCKED:
            adjacentCells.append(e)

        # randomly select a number within the range of available cells
        r = randint(0, len(adjacentCells) - 1)
        # Randomly selected adjacentCell is now the new Position
        pos = adjacentCells[r]
        path.append(pos)

    return path


'''
Find the solution path from START cell to GOAL cell

DO NOT MODIFY THE PARAMETERS

Parameter: maze  - the maze (list representation) to search
           start - position of the start cell
           goal  - position of the goal cell

Return:    the path  (list of (r,c)) from START to GOAL
           for this algorithm, the returned path is the solution path,
           a shortest path from start to goal
'''
def smartWalker(maze, start, goal):

    pos = start
    path = [pos]

    if pos == goal:
        return path

    maze[pos[0]][pos[1]] = VISITED

    numRows = len(maze)
    numCols = len(maze[0])

    n = (pos[0]-1, pos[1]) # North coords
    s = (pos[0]+1, pos[1]) # South coords
    e = (pos[0], pos[1]+1) # East coords
    w = (pos[0], pos[1]-1) # West coords

    adjacentCells = []

    if n[0] >= 0:
        north = maze[n[0]][n[1]]
        if north != BLOCKED and north != VISITED:
            adjacentCells.append(n)

    if s[0] < numRows:
        south = maze[s[0]][s[1]]
        if south != BLOCKED and south != VISITED:
            adjacentCells.append(s)

    if e[1] < numCols:
        east = maze[e[0]][e[1]]
        if east != BLOCKED and east != VISITED:
            adjacentCells.append(e)

    if w[1] >= 0:
        west = maze[w[0]][w[1]]
        if west != BLOCKED and west != VISITED:
            adjacentCells.append(w)

    if len(adjacentCells) == 0:
        return None

    adjacentPaths = []

    for cell in adjacentCells:
        adjacentPath = smartWalker([row[:] for row in maze], cell, goal)

        if adjacentPath != None:
            adjacentPaths.append(path + adjacentPath)

    if len(adjacentPaths) == 1:
        return adjacentPaths[0]

    elif len(adjacentPaths) == 0:
        return None

    else:
        print("Test to make sure this condition is impossible...")

'''
Find the solution path from START cell to GOAL cell

DO NOT MODIFY THE PARAMETERS

Parameter: maze  - the maze (list representation) to search
           start - position of the start cell
           goal  - position of the goal cell

Return:    the path  (list of (r,c)) from START to GOAL

'''
def rightHandWalker(maze, start, goal):
    hand = "" #up, right, left, down


    numRows = len(maze)
    numCols = len(maze[0])
    pos = start
    path = [pos]

    n = (start[0] - 1, start[1])  # Northern
    s = (start[0] + 1, start[1])  # Southern
    w = (start[0], start[1] - 1)  # Western
    e = (start[0], start[1] + 1)  # Eastern

    openCells = []

    if n[0] >= 0 and maze[n[0]][n[1]] != BLOCKED:
        openCells.append(n)

    if s[0] < numRows and maze[s[0]][s[1]] != BLOCKED:
        openCells.append(s)

    if w[1] >= 0 and maze[w[0]][w[1]] != BLOCKED:
        openCells.append(w)

    if e[1] < numCols and maze[e[0]][e[1]] != BLOCKED:
        openCells.append(e)


    if n not in openCells:
        hand = "up"
    if s not in openCells:
        hand = "down"
    if w not in openCells:
        hand = "left"
    if e not in openCells:
        hand = "right"

    while pos != goal:

        if hand == "up":
            if w[1] >=0 and maze[w[0]][w[1]] != BLOCKED:
                pos = w
                path.append(pos)
            else:
                hand = "left"
        if hand == "left":
            if s[0] < numRows and maze[s[0]][s[1]] != BLOCKED:
                pos = s
                path.append(pos)
            else:
                hand = "down"
        if hand == "down":
            if e[1] < numCols and maze[e[0]][e[1]] != BLOCKED:
                pos = e
                path.append(pos)
            else:
                hand = "right"
        if hand == "right":
            if n[0] >= 0 and maze[n[0]][n[1]] != BLOCKED:
                pos = n
                path.append(pos)
            else:
                hand = "up"

        n = (pos[0] - 1, pos[1])  # Northern Coordinates
        s = (pos[0] + 1, pos[1])  # Southern
        w = (pos[0], pos[1] - 1)  # Western
        e = (pos[0], pos[1] + 1)  # Eastern

        openCells = []

        if n[0] >= 0 and maze[n[0]][n[1]] != BLOCKED:
            openCells.append(n)

        if s[0] < numRows and maze[s[0]][s[1]] != BLOCKED:
            openCells.append(s)

        if w[1] >= 0 and maze[w[0]][w[1]] != BLOCKED:
            openCells.append(w)

        if e[1] < numCols and maze[e[0]][e[1]] != BLOCKED:
            openCells.append(e)


        if hand == "up" and n in openCells:
            hand = "right"
        elif hand == "down" and s in openCells:
            hand = "left"
        elif hand == "left" and w in openCells:
            hand = "up"
        elif hand == "right" and e in openCells:
            hand = "down"

    return path



### =================== M A I N =================== ###

'''
This main control loop is provided for your convenience.
This code allows you to input a maze from a designated text file.
'''

if __name__ == "__main__":


    while True:

        filename = input("Enter Maze Filename (RETURN / ENTER to stop):")

        if filename == "":
            break

        maze_s = getMaze(filename)

        maze = convert(maze_s)

        display(maze)

        # print("\nTraversing maze with randomWalker...")
        # solution = randomWalker(maze, findCell(maze, START), findCell(maze, GOAL))
        # print(solution)

        # print("\nTraversing maze with smartWalker...")
        # solution2 = smartWalker(maze, findCell(maze, START), findCell(maze, GOAL))
        # print(solution2)

        print("\nTraversing maze with rightHandWalker...")
        solution3 = rightHandWalker(maze, findCell(maze, START), findCell(maze, GOAL))
        print(solution3)

        print("\nDisplaying with path:")
        displayWithPath(maze,solution3)


    print("Good-bye. Program shutting down...")

