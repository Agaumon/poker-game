import random

# Creates variables in list for card suits and numbers
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Create empty list for card deck
deck = []

# Take values from suits and numbers and append to deck
for suit in suits:
    for number in numbers:
        deck.append(f'{number} of {suit}')

# Create variables to hold player chip count, dealer chip count, pot, and pairplus
playerChips = 500
dealerChips = 500
dealerBet = 0
pot = 0
anteBet = 0
pairPlus = 0

# Shuffles deck each time to ensure cards picked are random
random.shuffle(deck)

# Function to handle ante bet
def initialBet():
    global playerChips, pot, pairPlus, anteBet, dealerBet
    while True:
        ante = int(input("How much would you like to bet? "))
        if ante <= playerChips:
            dealerBet = ante
            dealerChips -= dealerBet
            pot += ante
            playerChips -= ante
            anteBet = ante + dealerBet
            break
        elif ante > playerChips:
            print("Insufficient chips. Enter a different amount")
        else:
            print("Incorrect input. Try again.")

# Function to handle pair plus bet
def pairBet():
        global playerChips, pairPlus
        print(playerChips)
        while True:
            pairBonus = int(input("(Optional) Place your pair plus bet: "))
            if pairBonus <= playerChips or pairBonus == 0:
                pairPlus += pairBonus
                playerChips -= pairBonus
                break
            elif pairBonus >= playerChips:
                print("Insufficient chips. Enter a different amount")
            elif playerChips == 0:
                print("Cannot place pair plus bet at this time.")
            else:
                print("Incorrect input. Try again.")

# Function to handle double down after player card reveal
def doubleDown():
    global playerChips, pot, anteBet
    while True:
        ddAsk = input("Would you like to double down? ").upper()
        if ddAsk == "YES" or ddAsk == "Y":
            while True:
                ddBet = 2 * anteBet
                if ddBet < playerChips:
                    pot += ddBet
                    break
                else:
                    print("Cannot place a double bet at this time.")
                    break
            break
        elif ddAsk == "NO" or ddAsk == "N":
            break
        else:
            print("Incorrect response. Try again.")

# Function to check card values and assign number values to Ace, Jack, Queen, and King
def checkCards(hand):
    # Creates empty lists
    cardNumbers = []
    cardSuits = []
    values = []

# Goes through each item in the "hand" (playerHand and dealerHand)
    for cards in hand:
        # print(f'Cards: {cards}')
        parts = cards.split(" of ") #Separates the suit and number and removes the "of" in between
        # print(f' Parts: {parts}')
        cardNumber = parts[0] #Assigns the number(s) from the split to a variable
        cardSuit = parts[1] #Assigns the suit(s) from the split to a variable
        # print(f'Card Number: {cardNumber}')
        # print(f'Card Suit: {cardSuit}')
        cardNumbers.append(cardNumber) #Adds the numbers to the above cardNumbers list
        cardSuits.append(cardSuit) #Adds the suits to the above cardSuits list
    # print(f'Card Numbers: {cardNumbers}')
    # print(f'Card Suits: {cardSuits}')

    for number in cardNumbers: #Goes through each number and assigns a number value for each item in the cardNumbers list
        if number == "Ace":
            values.append(11)
        elif number == "Jack":
            values.append(12)
        elif number == "Queen":
            values.append(13)
        elif number == "King":
            values.append(14)
        else:
            values.append(int(number))
        
        values.sort()

    flush = False
    if suits[0] == suits[1] and suits[1] == suits[2]:
        flush = True

    straight = False
    if values[1] == values[0] + 1 and values[2] == values[1] + 1:
        straight = True
    if values == [2, 3, 14]:
        straight = True
    
    threeKind = False
    if values[0] == values[1] and values[1] == values[2]:
        threeKind = True

    pair = False
    if values[0] == values[1] or values[1] == values[2] or values[0] == values[2]:
        pair = True

    if straight and flush:
        return 6, "Straight Flush", values, "sflush"
    elif threeKind:
        return 5, "Three of a Kind", values, "3ofkind"
    elif straight:
        return 4, "Straight", values, "straight"
    elif flush:
        return 3, "Flush", values, "flush"
    elif pair:
        return 2, "Pair", values, "pair"
    else:
        return 1, "High Card", values, "high"

# Function to identify and declare a winner
def gameWin(playerHand, dealerHand):
    global playerChips, dealerBet, dealerChips, pot, anteBet, pairPlus

    playerRank, playerName, playerVal, pHandRank = checkCards(playerHand)
    dealerRank, dealerName, dealerVal, dHandRank = checkCards(dealerHand)

    playerSum = sum(playerVal)
    dealerSum = sum(dealerVal)

    print(f'Player has: ', playerName)
    print(f'Dealer has: ', dealerName)

    if playerRank > dealerRank and pHandRank == "pair":
        print("Player wins")
        totalSum = anteBet + (2*pairBet)
        pot += totalSum
        playerChips += pot
        pot = 0
        dealerBet = 0
    elif playerRank > dealerRank:
        print("Player wins")
        pot = anteBet + dealerBet
        dealerChips = pot
    elif dealerRank > playerRank:
        print("Dealer wins.")
        dealerChips += anteBet
    elif playerRank == dealerRank or dealerRank == playerRank:
        while True:
            if playerSum > dealerSum:
                print("Player wins.")
            elif dealerSum > playerSum:
                print("Dealer wins.")
            else:
                print("Cannot determine winner.")
    else:
        print("Tie")

# Assigns cards to player and dealer and removes them from the deck
playerHand = random.sample(deck,3)
deck = [card for card in deck if card not in playerHand]

dealerHand = random.sample(deck,3)
deck = [card for card in deck if card not in dealerHand]

# Confirm player wants to play game to initialize game
while True:
    startGame = input("Would you like to play poker? ").upper()

    if startGame == "YES" or startGame == "Y":
        initialBet()
        pairBet()
        print(f'{playerHand}')
        doubleDown()
        print(f'{dealerHand}')
        gameWin(playerHand, dealerHand)

    elif startGame == "NO" or startGame == "N":
        exit()

    else:
        print("Incorrect response. Try again.")