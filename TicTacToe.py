#W02 Introduction: Ponder and Prove
#Autor: Carrasco Dario
#Instructor: Bro. Lythgoe

def main():
    
    #I create the TicTacToe board
    board = [['1','|','2','|','3'],
    ['-','+','-','+','-'],
    ['4','|','5','|','6'],
    ['-','+','-','+','-'],
    ['7','|','8','|','9']
    ]

    #Declare the variables to use.
    turn_1 = True
    player_1 = ''
    player_2 = ''
    lap = 0

    #Prints board status
    print_board(board)

    
def print_board(board):
    '''I print the board in grid format. 
    Parameters:
    board: the dictionary containing the data format.
    return the new board as grid            
    '''
    for row in board:
        for i in range(len(row)):
            if i == len(row)-1:
                print(row[i], end='\n')
            else:
                print(row[i], end=' ')      
    return board                

# Call main to start this program.
if __name__ == "__main__":
    main() 