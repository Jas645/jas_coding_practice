import random


position = (0,0)
path = []

start = (0,0)
end = (8,8)

def generate_maze(rows, cols, wall_prob = 0.3):
    maze = []
    
    for r in range(rows):
        row = []
        for c in range(cols):
            if random.random() > wall_prob:
                row.append(0)
            else:
                row.append(1)
        maze.append(row)
    
    return maze

def print_maze(maze, start, end, path):
    rows = len(maze)
    cols = len(maze[0])
    
    print ("- " * (cols +2))
    for r in range(rows):
        print("-", end = " ")
        for c in range(cols):
            if (r, c) == start:
                print("S", end=" ")  # Start
            elif (r, c) == end:
                print("E", end=" ")
            elif (r, c) in path:
                print(".", end =" ")
            elif maze[r][c] == 1:
                print("#", end=" ")  # Wall
            else:
                print(" ", end=" ")  #path
        print("-")
    print ("- " * (cols +2))


def valid_moves(maze, position):
    row, col = position
    rows = len(maze)
    cols = len(maze[0])
    moves = []
    
    if row > 0 and maze[row-1][col] == 0:
        moves.append((row-1, col))
    
    if row < rows-1 and maze[row+1][col] == 0:
        moves.append((row+1, col))
        
    if col > 0 and maze[row][col-1] == 0:
        moves.append((row, col-1))
        
    if col < cols-1 and maze[row][col+1] == 0:
        moves.append((row, col+1))
        
    return moves

    
def solve(maze, position, end, visited, path):    
    if position == end:
        return True
    
    visited.add(position)
    path.append(position)
    for move in valid_moves(maze, position):
        if move not in visited:
            if solve(maze, move, end, visited, path):
                return True
            print_maze(maze, start, end, path)
            
    path.pop()
    return False


maze = generate_maze(8,8)
print_maze(maze, start, end, path)
solve(maze, start, end, set(), path)
print(path)