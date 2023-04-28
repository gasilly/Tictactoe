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
 getUserCoordinate()
def getUserCoordinate():
	#Print the current board out for the user and ask the user to either put in a new location to mark or quit the program
	while True:	
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
		user_coordinate = input("What part of the board would you like to mark? press Q to quit. ")
		if(user_coordinate.capitalize() == 'Q'):
			exit()
		if(user_coordinate in coordinate_values):
			coordinate_values[user_coordinate] = "x" 
def getAICoordinate():
	print()
if __name__ == "__main__":
	main()
