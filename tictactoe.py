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
	#TODO add a way to make the user attempt to enter a valid entry again if they fail to do so the first time
		#get the users next move or exit. And if they select a coordinate make sure its valid and empty before trying to continue 
		user_coordinate = input("What part of the board would you like to mark? press Q to quit. ").upper()
		if(user_coordinate == 'Q'):
			exit()
		if(user_coordinate in coordinate_values and coordinate_values[user_coordinate] == '-'):
			coordinate_values[user_coordinate] = 'x' 
def getAICoordinate():
	#Check if the center is open to be claimed and take it if its not
	if(coordinate_values["B2"] == "-"):
		coordinate_values["B2"] = "o"
	#TODO figure out why placing another value after a successful block causes the program to crash. Index out of range error
	#Checks to see if the player is about to have a game winning position by row and column then attempts to block it if it finds one,
	for i in range(0,9,3):
		current_row = list(coordinate_values.values())[i:i+3]
		#current_column = list(coordinate_values.values())[i,i + 3, i + 6]
		print(current_column)
		#Count the number of times a player mark occurs and make sure the last space is empty
		if(current_row.count('x') == 2 and 'o' not in current_row): 
			#Get the exact location in the row or column that is currently empty and replace it with an AI mark
			value = {l for l in list(coordinate_values)[i:i+3] if coordinate_values[l] == '-'}
			coordinate_values[list(value)[0]] = "o" 
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
