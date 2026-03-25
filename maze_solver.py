import random
import time


def create_empty_maze(rows, cols):
    return [[1 for _ in range(cols)] for _ in range(rows)]

def carve_maze(maze, row, col):
    
    directions = [
        (2,0),   #up
        (0,2),   #right
        (0,-2),  #left
        (-2,0),  #down
        ]
    
    random.shuffle(directions)
    
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
            if maze[new_row][new_col] == 1:
                maze[row + dr//2][col + dc//2] = 0
                maze[new_row][new_col] = 0
                
                carve_maze(maze, new_row, new_col)
                
def generate_maze(rows, cols):
    
    if rows % 2 == 0:
        rows += 1
    if cols % 2 == 0:
        cols += 1
        
    create_empty_maze(rows, cols)
    maze = create_empty_maze(rows, cols)
    
    start_row, start_col = 0, 0
    maze[start_row][start_col] = 0
    
    carve_maze(maze, start_row, start_col)
    return maze

def print_maze(maze, start, end, path):
    print("\n" * 5)
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
        path.append(position)
        return True
    
    visited.add(position)
    path.append(position)
    
    print_maze(maze, start, end, path)
    time.sleep(0.1)
    for move in valid_moves(maze, position):
        if move not in visited:
            if solve(maze, move, end, visited, path):
                return True
            
    path.pop()
    print_maze(maze, start, end, path)
    time.sleep(0.1)
    return False

position = (0,0)
maze = generate_maze(15,15)
start = (0,0)
end = (len(maze)-1, len(maze[0])-1)
path = []
solve(maze, start, end, set(), path)
print_maze(maze, start, end, path)