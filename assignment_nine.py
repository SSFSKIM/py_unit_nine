#Steve
#24.01.18
#Game of War

import random

#hand of each player
Player1 = []
Player2 = []

#winning point of each player
P1W = 0
P2W = 0
#render of suits, got from canvas
RESET = "\033[0m"
RED = "\033[31m"
BLACK = "\033[30m"
class Deck:
    def __init__(self):
        '''
        dictionary of scale of each number as some are alphabet(line 29)
        dictionary of actual shape for word(line28)
        rank of suits(line27)
        others are suits, numbers, cards
        '''
        self.suits = ['spades', 'hearts', 'diamonds', 'clubs']
        self.numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        #got an information about dictionaries from google, w3school
        self.rank = {'spades': 4, 'hearts': 3, 'diamonds': 2, 'clubs': 1}
        #got from chatGPT how to apply ANSI code to print special shape and color
        self.shapes = {'clubs': f"{BLACK}♣{RESET}", 'diamonds': f"{RED}♦{RESET}", 'spades': f"{BLACK}♠{RESET}", 'hearts': f"{RED}♥{RESET}"}
        #example code in assignment description
        self.cards = [{'suits': suit, 'numbers': number} for suit in self.suits for number in self.numbers]
        self.scale = {}
        for i in range(len(self.numbers)):
            self.scale[str(self.numbers[i])] = i + 2
    def shuffle(self): #looked up about algorithm from wikipidia
        '''
        shuffle the card
        no parameter
        :return:nothing
        '''
        n = 52
        while n > 0:
            swap = random.randint(0, n-1)
            self.cards[n-1], self.cards[swap] = self.cards[swap], self.cards[n-1]
            n = n-1
    def deal(self, number):
        '''
        hand each player a card by popping card from deck
        :param number: card that each player have in hand
        :return:
        '''
        for i in range(number):
            Player1.append(self.cards.pop())
            Player2.append(self.cards.pop())
deck = Deck()
def intident(a): #got from chatGPT asking a code to identify integer
    '''
    determine if input is integer on input value.
    apply int function, see if it is error
    :param a:
    :return: if integer, return true and if error,return false
    '''
    try:
        int(a)
        return True
    except ValueError:
        return False
def get_input():
    '''
    get input from user with asking to give proper input
    :return: input of user
    '''
    b = input('How many cards should each player get? Enter a number between 1 and 26')
    if intident(b) == False:
        print('Invalid input. Please enter a number between 1 and 26')
        get_input()
    else:
        b = int(b)
        if not 1 <= b <= 26:
            print('Please enter a number between 1 and 26')
            get_input()
        else:
            print(f'Dealer deals {b} card to each player...')
            return b




def show_hand():
    '''
    print the hand of each player.
    :return: nothing
    '''
    print(f'Player1 hand:', end = ' ') #got from chatGPT how to use end to print things in one line
    for i in range(len(Player1)): #for each card(dic form), print number+shape form by using shape dictionary
        print(str(Player1[i]['numbers']) + deck.shapes[Player1[i]['suits']], end = '  ')

    print(f'\nPlayer2 hand:', end = ' ')
    for i in range(len(Player2)):
        print(str(Player2[i]['numbers']) + deck.shapes[Player2[i]['suits']], end = '  ')


BOLD = "\033[1m"

def round(round):
    '''
    run each round
    :param round: round number
    :return: winner
    '''
    #show what each player handed
    nb = 'numbers'
    st = 'suits'
    word = f'Round {round}'
    print(f'\n{BOLD}{word}{RESET}:')
    #same way of printing shape with line 94.
    print(f'Player1: {Player1[round-1][nb]} of {deck.shapes[Player1[round-1][st]]}')
    print(f'Player2: {Player2[round-1][nb]} of {deck.shapes[Player2[round-1][st]]}')
    global P1W
    global P2W
    #compare the number of card using using scale dictionary(hand->card->number->scale), return winner
    if deck.scale[str(Player1[round-1]['numbers'])] > deck.scale[str(Player2[round-1]['numbers'])]:
        P1W += 1
        print('Player1 wins this round!')
        return Player1
    elif deck.scale[str(Player1[round-1]['numbers'])] < deck.scale[str(Player2[round-1]['numbers'])]:
        P2W += 1
        print('Player2 wins this round!')
        return Player2
    #if number is same, compare suit using the rank dictionary(hand(list)->card(dict)->suits(str)->rank(int)), return winner
    else:
        if deck.rank[Player1[round-1]['suits']] > deck.rank[Player2[round-1]['suits']]:
            P1W += 1
            print('Player1 wins this round!')
            return Player1
        else:
            P2W += 1
            print('Player2 wins this round!')
            return Player2


def game_start():
    '''
    run the game. Print the winner
    :return: nothing
    '''
    global P1W
    global P2W
    P1W = 0
    P2W = 0
    print('Welcome to the game of Compare. You will decide how many cards we get and then we\'ll play them one by one.')
    print('Whoever has the higher card wins that round. Whoever wins the most rounds wins the game.')
    #shuffle the deck
    deck.shuffle()
    #get input
    c = get_input()
    #deal the card
    deck.deal(c)
    #show hand of each player
    show_hand()
    #run rounds for all cards
    for i in range(c):
        round(i+1)
    #game over
    over = '\nGame Over!'
    GREEN = "\033[32m"
    #show how much each player one, print winner
    P1 = 'Player 1 wins the game!'
    P2 = 'Player 2 wins the game!'
    print(f'{BOLD}{over}{RESET}')
    print(f'Player 1 wins: {P1W} rounds')
    print(f'Player 2 wins: {P2W} rounds')
    #print the winner
    if P1W > P2W:
        print(f'{GREEN}{BOLD}{P1}{RESET}')
    elif P1W < P2W:
        print(f'{GREEN}{BOLD}{P2}{RESET}')
    else:
        print('It\'s a tie!')

game_start()
