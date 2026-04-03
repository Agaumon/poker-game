import random

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

deck = []

playerBet = 0
dealerBet = 0
playerChips = 500
dealerChips = 500
pairBet = 0
pot = 0
totalBet = 0
round = 1
chip = [1,2]

for suit in suits:
    for number in numbers:
        deck.append(f'{number} of {suit}')

random.shuffle(deck)

playerHand = random.sample(deck,3)
deck = [card for card in deck if card not in playerHand]

dealerHand = random.sample(deck,3)
deck = [card for card in deck if card not in dealerHand]

def rollDice(sides):
    while True:
        if sides > 1:
            return random.randint(1,sides)
        else:
            print('Try again. ')
            break

def call():
    playerBet = dealerBet
    print(f'You call {playerBet} chips matching the dealers bet of {dealerBet} chips. ')
    totalBet = playerBet + dealerBet
    pot += totalBet
    totalBet = 0
    playerBet = 0
    dealerBet = 0
    round += 1

def raiseBet():
    raiseAsk = input("How much would you like to raise? ")
    
    if raiseAsk < playerChips and raiseAsk <= dealerChips:
        playerBet = raiseAsk
        print(f'You raised {raiseAsk} chips. ')
        dealerBet = playerBet
        print(f'The dealer matches your bet of {dealerBet} chips. ')
        totalBet = playerBet + dealerBet
        pot += totalBet
        dealerBet -= dealerChips
        playerBet -= playerChips
        playerBet = 0
        dealerBet = 0
        totalBet = 0
        round += 1

    elif raiseAsk < playerChips and raiseAsk > dealerChips:
        playerBet = raiseAsk
        print(f'You raised {raiseAsk} chips. ')
        dealerBet = dealerChips
        print(f'The dealer calls {dealerBet} chips. All in.')
        totalBet = playerBet + dealerBet
        pot += totalBet
        playerBet = 0
        dealerBet = 0
        totalBet = 0
        round += 1

    elif raiseAsk > playerChips:
        print('You do not have enough chips. Please input another amount. ')

def fold():
    totalBet = dealerBet + playerBet
    pot += totalBet
    print('You folded. Dealer wins. ')
    dealerChips += pot
    pot = 0
    totalBet = 0
    playerBet = 0
    dealerBet = 0

def checkHands():
    card1 = playerHand[0]
    card2 = playerHand[1]
    card3 = playerHand[2]
    dcard1 = dealerHand[0]
    dcard2 = dealerHand[1]
    dcard3 = dealerHand[2]
    for cards in playerHand:
        number,suit = cards.split(" of ")
        print("Player")
        print(number)
        print(suit)
        print()
    for cards in dealerHand:
        number,suit = cards.split(" of ")
        print("Dealer")
        print(number)
        print(suit)
        print()


gamePlay = input("Play poker? ").upper()
checkHands()

# while gamePlay == "YES" or gamePlay == 'Y' and playerChips != 0 and dealerChips != 0:
    # ante = int(input('How much would you like to bet? '))
    # while True:
    #     if ante <= playerChips:
    #         playerChips -= ante
    #         ante += pot
    #         pairPlus = input(f'(Optional) Would you like to place a pair plus bet? ').upper()
    #         while True:
    #             if pairPlus == 'YES' or pairPlus == 'Y':
    #                 ppBet = int(input('How much would you like to bet? '))
    #                 while True:
    #                     if ppBet <= playerChips:
    #                         playerChips -= ppBet
    #                         ppBet += pairBet
    #                     elif ppBet > playerChips:
    #                         print("Insufficient chips. Enter another amount. ")
    #                     else:
    #                         print("Incorrect input. Try again.")
    #                         break
    #     elif ante > playerChips:
    #         print('Insufficient chips. Enter a smaller amount. ')
    #         break
    #     else:
    #         print('Incorrect selection. Please try again. ')
    #         break
    # dealerButton = rollDice(3)
    # while round == 1 and dealerButton == 1:
    #     dealerBet = random.randrange(0,dealerChips-400,5)
    #     pot += dealerBet
    #     print(f'The dealer bets {dealerBet} what would you like to do?')
    #     dealerBet = 0
    #     playerChoice = input("Call, raise, or fold? ")
        
    #     if playerChoice == "call".upper():
    #         call()
    #         # playerBet = dealerBet
    #         # print(f'You call {playerBet} chips matching the dealers bet of {dealerBet} chips. ')
    #         # totalBet = playerBet + dealerBet
    #         # pot += totalBet
    #         # totalBet = 0
    #         # playerBet = 0
    #         # dealerBet = 0
    #         # round += 1
        
    #     while playerChoice == "raise".upper():
    #         raiseBet()
    #         # raiseAsk = input("How much would you like to raise? ")
            
    #         # if raiseAsk < playerChips and raiseAsk <= dealerChips:
    #         #     playerBet = raiseAsk
    #         #     print(f'You raised {raiseAsk} chips. ')
    #         #     dealerBet = playerBet
    #         #     print(f'The dealer matches your bet of {dealerBet} chips. ')
    #         #     totalBet = playerBet + dealerBet
    #         #     pot += totalBet
    #         #     dealerBet -= dealerChips
    #         #     playerBet -= playerChips
    #         #     playerBet = 0
    #         #     dealerBet = 0
    #         #     totalBet = 0
    #         #     round += 1

    #         # elif raiseAsk < playerChips and raiseAsk > dealerChips:
    #         #     playerBet = raiseAsk
    #         #     print(f'You raised {raiseAsk} chips. ')
    #         #     dealerBet = dealerChips
    #         #     print(f'The dealer calls {dealerBet} chips. All in.')
    #         #     totalBet = playerBet + dealerBet
    #         #     pot += totalBet
    #         #     playerBet = 0
    #         #     dealerBet = 0
    #         #     totalBet = 0
    #         #     round += 1

    #         # elif raiseAsk > playerChips:
    #         #     print('You do not have enough chips. Please input another amount. ')

    # while round == 1 and dealerButton == 2:
        # playerBet = random.randrange(0,playerChips-400,5)
        # pot += playerBet
        # print(f'You have the dealer button. You deal {playerBet} chips. ')
        # playerBet = 0

# print(f'Your cards are ${playerHand}')
# print(f'Dealer cards: {dealerHand}')