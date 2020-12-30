#lab04

from Stack import Stack


def printMaze(maze):
    for row in range(len(maze)):
	    for col in range(len(maze[0])):
		    print("|{:<2}".format(maze[row][col]), sep='',end='')
	    print("|")
    return

def solveMaze(maze, startX, startY):
    stack = Stack()
    stack.push([startX, startY])
    counter = 1
    maze[startX][startY] = counter
    while maze[startX][startY] != 'G':
        if maze[startX - 1][startY] == ' ' or maze[startX - 1][startY] =='G':
            if maze[startX - 1][startY] == 'G':
                return True
            counter += 1
            maze[startX - 1][startY] = counter
            stack.push([startX -1, startY])
            startX = startX - 1
        elif maze[startX][startY + 1] == ' ' or maze[startX][startY + 1] =='G':
            if maze[startX][startY + 1] == 'G':
                return True
            counter += 1
            maze[startX][startY + 1] = counter
            stack.push([startX, startY + 1])
            startY = startY + 1
        elif maze[startX + 1][startY] == ' ' or maze[startX + 1][startY] =='G':
            if maze[startX + 1][startY] == 'G':
                return True
            counter += 1
            maze[startX + 1][startY] = counter
            stack.push([startX + 1, startY])
            startX = startX + 1
        elif maze[startX][startY - 1] == ' ' or maze[startX][startY - 1] =='G':
            if maze[startX][startY - 1] == 'G':
                return True
            counter += 1
            maze[startX][startY - 1] = counter
            stack.push([startX, startY - 1])
            startY = startY - 1
        else:
            stack.pop()
            if stack.isEmpty() == True:
                return False
            startX = stack.peek()[0]
            startY = stack.peek()[1]
