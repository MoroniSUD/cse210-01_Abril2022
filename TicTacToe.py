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
#This while you go through all the options of the game
    while lap < 9:
        #First check if there are players loaded
        if player_1 == '':
            print("Enter the player's name 1 (X): ")
            player_1 = input()
            print("Enter the player's name 2 (O): ")
            player_2 = input()
        else:
            #Whose turn is it
            if turn_1:
                print(player_1 + ' Select a board position: ') 
            else:
                print(player_2 + ' Select a board position: ')   
                
            #I save the player option
            move_player = int(input()) 

            #Evaluated the value returned by the function change board
            value = change_board(board, move_player, turn_1) 
            if value == 0:
                #Change the status from true to false or false to true
                turn_1 = not turn_1
                #Add one more lap
                lap += 1
                #Print the new board
                print_board(board)
                #Check if there is a winner
                if who_won(board) == 1:
                    print('Well played! The winner is ' + player_1)
                    break
                elif who_won(board) == 2:
                    print('Well played! The winner is ' + player_2)
                    break
            else:    
                print(value)
            #In case of tie
            if lap == 9:
                print('The strategy was not good!' + player_1 + 'and' + player_2 + 'They tied.')
    
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

def change_board(board, position, turn_player):
    '''Modify the board based on player options and choices.
    Parameters:
    board: the dictionary containing the data format.
    position: option entered by the user
    trun_player: the player's turn, true player_1 false player_2.
    return the board with the options marked by the player and the options of the next player.
    '''
    if turn_player:
        symbol = 'X'
    else:
        symbol = 'O'

    if position == 1:
        if board [0][0] == '1':
            board[0][0] = symbol
            return 0
        else:
            return 'This position is filled'      
    elif position == 2:
        if board [0][2] == '2':
            board[0][2] = symbol
            return 0
        else:
            return 'This position is filled'
    elif position == 3:
        if board [0][4] == '3':
            board[0][4] = symbol
            return 0
        else:
            return 'This position is filled' 
    elif position == 4:
        if board [2][0] == '4':
            board[2][0] = symbol
            return 0
        else:
            return 'This position is filled' 
    elif position == 5:
        if board [2][2] == '5':
            board[2][2] = symbol
            return 0
        else:
            return 'This position is filled'
    elif position == 6:
        if board [2][4] == '6':
            board[2][4] = symbol
            return 0
        else:
            return 'This position is filled'
    elif position == 7:
        if board [4][0] == '7':
            board[4][0] = symbol
            return 0
        else:
            return 'This position is filled'
    elif position == 8:
        if board [4][2] == '8':
            board[4][2] = symbol
            return 0
        else:
            return 'This position is filled'
    elif position == 9:
        if board [4][4] == '9':
            board[4][4] = symbol
            return 0
        else:
            return 'This position is filled'                                                     
    else:
        return 'This position does not exist.'

def who_won(board):
    '''Validates all values entered, to know if there is a winner.
    Parameters:
    board: the dictionary containing the data format.
    return value 1 if the winner is player_1, value two if the winner is player_2. 
    '''
    for symbol in ['X', 'O']:
        row_0 = board[0][0] == symbol and board[0][2] == symbol and board[0][4] == symbol
        row_2 = board[2][0] == symbol and board[2][2] == symbol and board[2][4] == symbol
        row_4 = board[4][0] == symbol and board[4][2] == symbol and board[4][4] == symbol
        column_0 = board[0][0] == symbol and board[2][0] == symbol and board[4][0] == symbol
        column_2 = board[0][2] == symbol and board[2][2] == symbol and board[4][2] == symbol
        column_4 = board[0][4] == symbol and board[2][4] == symbol and board[4][4] == symbol
        line_down = board[0][0] == symbol and board[2][2] == symbol and board[4][4] == symbol
        line_up = board[4][0] == symbol and board[2][2] == symbol and board[0][4] == symbol

        if row_0 or row_2 or row_4 or column_0 or column_2 or column_4 or line_down or line_up:
            if symbol == 'X':
                return 1
            elif symbol == 'O':
                return 2
            break 
        
# Call main to start this program.
if __name__ == "__main__":
    main() 