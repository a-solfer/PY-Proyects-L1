#Instructions

# To take input from a user:

#player1 = input("Please pick a marker 'X' or 'O'")
# Note that input() takes in a string. If you need an integer value, use

# position = int(input('Please enter a number'))

# To clear the screen between moves:

# from IPython.display import clear_output
# clear_output()
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:

# print('\n'*100)
# This scrolls the previous board up out of view. Now on to the program!




#1 FIRST WE MAKE THE BOARD
#each squeare will be represented by a number from 1-9


from IPython.display import clear_output

#we need 10 items in list with the first being a dupe for index 0
board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',]

def display_board(board):
    clear_output()
    
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')



#2 WE ASK THE PLAYER WHICH MARKER HE WANTS TO BE X or O

def player_input():
    
    marker=''
    
    while not (marker =='X' or marker=='O'):
        
        marker = input("Player 1: pick either X or O: ").upper()
        
    if marker =='X':
        return ('X','O')
    else:
        return ('O','X')
    

#3 WE ASSIGN THE MARKER TO THE DESIRED POSITION ON THE BOARD
    

def place_marker(board, marker, position):
    
    board[position]=marker


#4 WE CHECK FOR A WIN

def win_check(board, mark):
    return((board[1]==mark and board[2]==mark and board[3]==mark)or #across
           (board[4]==mark and board[5]==mark and board[6]==mark)or
           (board[7]==mark and board[8]==mark and board[9]==mark)or
           (board[1]==mark and board[5]==mark and board[9]==mark)or #diagonal
           (board[7]==mark and board[5]==mark and board[3]==mark)or
           (board[1]==mark and board[4]==mark and board[7]==mark)or #vertical
           (board[2]==mark and board[5]==mark and board[8]==mark)or
           (board[3]==mark and board[6]==mark and board[9]==mark))

#5 WE PICK WHICH PLAYER GOES FIRST RANDOMLY

import random

from random import randint

def choose_first():
    #old return print('Player'+str(random.randint(1, 2))+' goes first!')
    if random.randint(1,2)==1:
        turn='Player 1 '
        
    else:
        turn='Player 2'
#i forgot to add return so we can use the variable turn afterwards

    return turn


#6 WE CHECK IF THE SPACE ON THE BOARD IS AVAILABLE
def space_check(board, position):
    return board[position] ==' '


#7 WE CHECK IF THE BOARD IS FULL
def full_board_check(board):
    while ' ' in board:
        return False
    else:
        return True
    
#8 WE ASK THE PLAYER WHAT HIS NEXT MOVE WILL BE
    #THEN WE USE STEP 6 TO CHECK IF DESIRED MOVE IS AVAILABLE
    #IF IT IS, WE SAVE THE POSITION TO USE
def player_choice(board):
    
    position=0
    
    while position==0:
        
        next_move = int(input('Pick your next position (1-9): '))
        
        if not space_check(board,next_move):
            print('not available')
        elif space_check(board,next_move):
            position=int(next_move)
               
    return position

#STEP 9: ASK PLAYERS IF THEY WANT TO CONTINUE PLAYING

def replay():
    play=True
    
    replay_check=' '
    #OLD while play==True:
    while replay_check not in ['Y','N']:
        
        replay_check=input('Play? (Y or N): ').upper()
        
        if replay_check not in ['Y','N']:
            print('Please pick Y or N')
        
        #if replay_check=='Y':
         #   return True
        
    if replay_check=='Y':
        return True
    else:
        return False
    

#10 WE TIE IT ALL TOGETHER

print('Welcome to Tic Tac Toe!')

#after every game we need to reset the board and variables to org
while True:

    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',]

    player1_marker,player2_marker=player_input()

    #turn has to be the variable assigned to the result of choose first
    #make sure the fx has return turn
    turn=choose_first()
    print(turn + "goes first!")
    
    play=input('Ready to play? (Y or N): ')
    
    if play.upper()=='Y':
        playing=True
    else:
        playing=False

    #GAME
    while playing:
        
        if turn=='Player 1':
            
            display_board(board)
            position=player_choice(board)
            place_marker(board, player1_marker, position)
            
            if win_check(board, player1_marker): #the ==true is implied
                print( 'Player 1 has won the game')
                playing=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Its a Draw!')
                    break
                else:
                    turn = 'Player 2'

        if turn=='Player 2':

            display_board(board)
            position=player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker): #the ==true is implied
                print( 'Player 2 has won the game')
                playing=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Its a Draw!')
                    break
                else:
                    turn = 'Player 1'
        
    if not replay():
            break