# BLACKJACK
# To play a hand of Blackjack the following steps must be followed:

# Create a deck of 52 cards
# Shuffle the deck
# Ask the Player for their bet
# Make sure that the Player's bet does not exceed their available chips
# Deal two cards to the Dealer and two cards to the Player
# Show only one of the Dealer's cards, the other remains hidden
# Show both of the Player's cards
# Ask the Player if they wish to Hit, and take another card
# If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
# If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
# Determine the winner and adjust the Player's chips accordingly
# Ask the Player if they'd like to play again


#GLOBAL VALUES
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#CLASES

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    
    def __str__(self):
        return self.rank + ' of '+ self.suit
    
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        
        #deck composition:
        deck_comp=''
        for card in self.deck:
            
            #every card has its own string representation, we can
            #call on it using the following method:
            deck_comp += '\n'+ card.__str__()
        
        #return: the deck has this composition
        return "The deck has: "+deck_comp
          

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        # we want to grab a card from myself:
        # grab the deck attribute of this deck class
        #pop off a card item from that list and
        #set it as single_card:
        single_card=self.deck.pop()
        return single_card
    

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        #cards passed in from 
        #the deck.deal() which is a single Card() object
        self.cards.append(card)
        
        #the card has a rank and therefore a value
        #we can now sum the value:
        #we grab that card's rank and we pass that
        #in to the values dictonary as a key
        #and that will determine the value of the card
        self.value += values[card.rank]
        
        #we track our aces
        if card.rank == 'Ace':
            self.aces += 1
            
        
    
    def adjust_for_ace(self):
        
        #we check if the sum of value is greater than 21
        #if its less, we wont do it
        #IF TOTAL VALUE>21 AND I STILL HAVE AN ACE:
        #THEN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11
        #we are treating the self.aces as a boolean
        #zeros are treated as False
        #its the same as self.aces > 0
        
        while self.value > 21 and self.aces:
            self.value -=10
            self.aces -= 1


class Chips:
    
#     alternative option: 
#     def __init__(self,total=100):
#         self.total = total
#         self.bet = 0
        
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    
    def lose_bet(self):
        self.total -= self.bet


#FUNCTION DEFINITIONS:

def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input("How many chips would you want to bet?: "))
                               
        except ValueError:
            print("Please prove an integer")
        
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enought chips, You have {}'.format(chips.total))
            else:
                break

def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing # to control an upcoming while loop
    
    while True:
        x = input('Hit or Stand? h or s ')
        
        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif x[0].lower() =='s':
            print("Dealer's turn")
            playing = False
            
        else:
            print("Sorry, enter only h or s only")
            continue
        break


def show_some(player,dealer):
    #from a OOP POV: Tthe dealer has a list 
    #of 2 cards at the beginning of the game
    #dealer.cards[1]
    
    #Show only One of the dealer's cards
    print("\n Dealer's hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    
    
 #     Show all (2 cards) of the player's hand/cards

    print("\n Player's hand")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    #show the dealer's hand
    
    print("\n Dealer's hand")
    for card in dealer.cards:
        print(card)
    print(dealer.value)
    
#     #alternative:
#     print("\n Dealer's hand: ",*dealer.cards,sept='\n')
        
    #calc and display value (J+K ==20)
    print("Value of Dealer's hand is:", dealer.value)
    
    print("\n Player's hand")
    for card in player.cards:
        print(card)
    print("Value of Player's hand is:", player.value)


def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()

#push is when dealer and player both got 21
def push(player,dealer):
    print("Tie! it is a PUSH")


#GAME 

while True:
    # Print an opening statement
    print("Welcome to Blackjack!")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    #we set a hand for the player and another for the dealer
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
        
    # Set up the Player's chips
    player_chips = Chips()
    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value >21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
        
    
    # Inform Player of their chips total 
    print('\n Player total chips are at {}'.format(player_chips.total))
    # Ask to play again
    new_game = input("Would you like to play another hand? y/n ")
    
    if new_game[0].lower() == 'y':
        playing=True
        continue
    else:
        break

