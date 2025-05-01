#CARD CLASS
#SUIT, RANK, VALUE
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


#CLASSES

class Card():
    #we dont need the user to provide the value
    #because we will figure that out based on a dictionary
    #of values we will create later on
    def __init__(self,suit,rank): 
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    
    def __str__(self):
        return self.rank + " of "+self.suit
    
class Deck():
    
    def __init__(self):

        self.all_cards=[]

        for suit in suits:
            for rank in ranks:
                # create card object
                created_card=Card(suit,rank)
                
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
class Player:
    
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
        
    def remove_one(self):
        #we specify pop at index 0
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        
        #a single card object or list
        #this avoids nested lists
        
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            #for a single card
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} had {len(self.all_cards)} cards.'
    

#GAME SET UP
player_one=Player("One")
player_two=Player("Two")

new_deck=Deck()
new_deck.shuffle()


#we split the deck 
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    

game_on = True


#while game_on

round_num=0

while game_on:
    
    round_num +=1
    print(f"Round {round_num}")


# we verify if a player has lost:

    if len(player_one.all_cards)==0:
      print('Player One, out of cards! Player Two Wins!')
      game_on=False #break of the while loop
      break

    if len(player_two.all_cards)==0:
      print('Player Two, out of cards! Player One Wins!')
      game_on=False #break of the while loop
      break

    # NEW ROUND
    
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())

    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())

    #while at_war
    
    at_war=True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            #player one adds their cards back to their deck
            player_one.add_cards(player_one_cards)
            
            #player one adds P2 cards to their deck
            player_one.add_cards(player_two_cards)
            
            #we break out of war
            at_war = False
        
        #we check if P2 has won
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            #player two adds their cards back to their deck
            player_two.add_cards(player_one_cards)
            
            #player two adds P1 cards to their deck
            player_two.add_cards(player_two_cards)
            
            #we break out of war
            at_war = False
        
        #cards are equal to each other:
        else:
            print("WAR TIMEE!")
            
            #check if players have enough cards to go to war
            
            if len(player_one.all_cards) < 15:
                print("Player One unable to declare war ")
                print("PLAYER 2 WINS!")
                
                game_on = False 
                break
                
            elif len(player_two.all_cards) < 15:
                print("Player Two unable to declare war ")
                print("PLAYER 1 WINS!")
                
                game_on = False 
                break
                
            else:
                for num in range(15):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())