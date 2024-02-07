from pyMaze import maze, agent, COLOR

#Function for the DFS
def DFS(m):
    #Start cell is the last cell
    start = (m.rows, m.cols)
    explored =[start]
    frontier = [start]

    #Declare an empty dictionary
    dfsPath = {}

    while len(frontier) > 0:
        currCell = frontier.pop()
        if currCell == (1,1):
            break #As it the goal to find the cell 1,1
    
        #Explore eacxh of the directions
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                
                #After finding the child cell, check if it is in explored list, if true move to next cell
                if childCell in explored:
                    continue
                #add child cell in explored and frontier
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell] = currCell
    forwardPath = {}
    cell = (1,1)
    while cell != start:
        forwardPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return forwardPath

#Create the maze
m = maze(25,15)
m.CreateMaze()

path = DFS(m)

a = agent(m, footprints = True)
m.tracePath({a:path})

m.run()