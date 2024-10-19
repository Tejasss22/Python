import random
import math
def display(game_state):
	for i in range(len(game_state)):
		for k in range(2*len(game_state)+1):
			print("-",end="")
		print("")
		print("|",end="")
		for j in range(len(game_state)):
			print(game_state[i][j],end="|")
		print("")
	for k in range(2*len(game_state)+1):
			print("-",end="")
	print("")
	
	
def create_puzzle(size):
	grid = [list(" "*size) for i in range(size)]
	
	for rows in range(size):
		for col in range(size):
			availability = set(grid[rows] + [row[col] for row in grid])
			possibilities = set(range(1,size+1))
			c = list(possibilities - availability)
			if c:
				grid[rows][col] = c[random.randint(0,len(c)-1)]
			else:
				return create_puzzle(size)
	return grid
	
	
def initialize():
	size = int(input("Enter the size of sudoku: "))
	grid = create_puzzle(size)
	display(grid)
	levels = {1:("Very Easy",20),2:("Easy",35),3:("medium",50),4:("hard",60),5:("very hard",75)}
	print("There are 5 levels.")
	for k,v in levels.items():
		print(f"level {k} : {v[0]}")
		
	level = int(input("Enter game level: "))
	no_of_hidden_fields  = math.ceil((levels[level][1] * size * size)/100)
	hidden_fields = []
	for _ in range(no_of_hidden_fields):
		n = all_possibilities.pop(random.randint(0,len(ap)-1))
		hidden_fields += [(math.floor(n/size),(n%size))]
		
def start_game(grid,hidden_fields):
	display(grid)
	for r,c in hidden_fields:
		grid[r][c] = int(input(f"Enter value for row : {r+1} and col : {c+1} in 
	return grid

def sudoku():

	initialize()

	grid = start_game(grid,hidden_fields):
		f

	#stage_game():

sudoku()

