#INTERACTIVE PROYECT

# PART 1: DISPLAY OF GAME

#ORIGINAL GAME LIST
#game_list=[0,1,2]


#DISPLAY
def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)

#CHECK
#display_game(game_list)

#PART 2: USER CHOOSES POSITION
#The position actually works as the index of the value in game_list to be replaced with a string
def position_choice():
    
    choice='wrong'
    
    #choice will be returned as a str by input
    while choice not in ['0','1','2']:
        
        choice = input("Pick a position (0,1,2): ")
        
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice! ")
  
    #once we have a valid choice, we convert it to int
    return int(choice)

#RUN THIS TO CHECK USER CAN MAKE THE CHOICE
#position_choice()

#PART 3: REPLACEMENT OF CHOSEN LIST VALUE WITH STRING
def replacement_choice(game_list,position):
    
    user_placement=input("Type a string to place at position: ")
    
    game_list[position]=user_placement
    
    return game_list

#CHECK REPLACEMENT
#replacement_choice(game_list,1)

#PART 4: ASK USER IF HE/SHE WANTS TO KEEP PLAYING
def gameon_choice():
    
    choice='wrong'
    
    #choice will be returned as a str by input
    while choice not in ['Y','N']:
        
        choice = input("Keep Playing? (Y or N): ")
        
        if choice not in ['Y','N']:
            print("Sorry, I don't understand, please choose Y or N ")
            
  
    if choice =='Y':
        return True
    else:
        return False

#CHECK IF KEEP PLAYING
#gameon_choice()

#PART 5: WE CONNNECT IT ALL TOGETHER:

#initial values
game_on = True
game_list=[0,1,2]


while game_on:
    
    #we display the current game list
    display_game(game_list)
    
    #the player chooses the position
    position= position_choice()
    
    #rewrite the position into the game list
    game_list=replacement_choice(game_list,position)
    
    display_game(game_list)
    
    #we give the user the choice to continue playing
    game_on=gameon_choice()