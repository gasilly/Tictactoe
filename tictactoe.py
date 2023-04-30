#default game board
'''
         "  a     b     c
               |     |     
         1  -  |  -  |  -  
          _____|_____|_____
               |     |     
         2  -  |  -  |  -  
          _____|_____|_____
              |     |     
         3  -  |  -  |  -  
               |     |      "	
'''
#A dictionary containing all the possible values for the tictactoe board
coordinate_values = {"A1":'-',"B1": '-',"C1": '-',"A2":'-',"B2": '-',"C2": '-',"A3":'-',"B3": '-',"C3": '-'}
def main():
	while True:
		printGrid()
		getUserCoordinate()
		getAICoordinate()
def getUserCoordinate():
		user_coordinate = input("What part of the board would you like to mark? press Q to quit. ")
		if(user_coordinate.capitalize() == 'Q'):
			exit()
		if(user_coordinate in coordinate_values):
			coordinate_values[user_coordinate] = "x" 
def getAICoordinate():
	player_mark_count = 0
#Check if the center is open to be claimed and take it if its not
	if(coordinate_values["B2"] == "-"):
		coordinate_values["B2"] = "o"
#Check for potential player winning positions going from row to column to diagnols
	'''
	for coordinate in coordinate_values:
		for i in range(0,3)
			if(coordinate_values[coordinate] == "x"
				player_mark_count ++
			if(player_mark_counter
		player_mark_count = 0
	'''
	for i in range(0,9,3): #TODO FIX THIS FOR LOOP SO IT GETS THE FIRST 3 VALUES IN THE DICTIONARY THEN THE NEXT AND SO ON
		for x in list(coordinate_values[i:i+3]):
			print(x)
#display the current board for the user
def printGrid():
	print("""                        
			     a     b     c
                                |     |     
                         1   {}  |  {}  |  {}  
                           _____|_____|_____
                                |     |     
                         2   {}  |  {}  |  {}  
                           _____|_____|_____
                                |     |     
                         3   {}  |  {}  |  {}  
                                |     |         
              """
                .format(coordinate_values["A1"],coordinate_values["B1"],coordinate_values["C1"],coordinate_values["A2"],coordinate_values["B2"],coordinate_values["C2"],coordinate_values["A3"],coordinate_values["B3"],coordinate_values["C3"]))


if __name__ == "__main__":
	main()
