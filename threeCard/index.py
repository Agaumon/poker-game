import random, os, time, math

# Creates variables in list for card suits and numbers
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Create empty list for card deck
deck = []

# Take values from suits and numbers and append to deck
for suit in suits:
    for number in numbers:
        deck.append(f'{number} of {suit}')

# Created variables
playerChips = 500
dealerChips = math.inf
dealerBet = 0
pot = 0
anteBet = 0
pairPlus = 0

# Shuffles deck each time to ensure cards picked are random
random.shuffle(deck)

# Function to handle initial betting
def initialBet():
    global playerChips, dealerChips, pot, pairPlus, anteBet, dealerBet
    while True:
        time.sleep(1)
        os.system("clear")
        playerInput = input("How much would you like to bet? ")
        try:
            ante = int(playerInput)
            if ante <= playerChips and ante != 0:
                dealerBet = ante
                anteBet = ante
                dealerChips -= dealerBet
                playerChips -= anteBet
                pot = anteBet + dealerBet
                print()
                print(f'Ante Bet: {anteBet}')
                print()
                break
            elif ante > playerChips:
                print("Insufficient chips. Enter a different amount")
                time.sleep(1)
                os.system("clear")
            elif ante <= 0:
                print("Ante cannot be zero.")
                time.sleep(1)
                os.system("clear")
        except ValueError:
            print("Incorrect input. Try again.")
            time.sleep(1)
            os.system("clear")

# Function to handle pair plus bonus bet
def pairBet():
        global playerChips, pairPlus
        time.sleep(2)
        os.system("clear")
        while True:
            print(f'Player Chips: {playerChips}')
            print()
            pairBonus = int(input("(Optional) Place your pair plus bet: "))
            if pairBonus <= playerChips or pairBonus == 0:
                pairPlus = pairBonus
                playerChips -= pairBonus
                print()
                print(f'Pair Plus Bet: {pairPlus}')
                break
            elif pairBonus >= playerChips:
                print("Insufficient chips. Enter a different amount")
            elif playerChips == 0:
                print("Cannot place pair plus bet at this time.")
            else:
                print("Incorrect input. Try again.")

# Function to ask double down after player card reveal
def doubleDown():
    global playerChips, pot, anteBet, dealerBet
    time.sleep(1.5)
    os.system("clear")
    while True:
        print(f'Player Hand: {playerHand}')
        print()
        print(f'Player Chips: {playerChips}')
        print()
        ddAsk = input("Would you like to double down? ").upper()
        if ddAsk == "YES" or ddAsk == "Y":
            while True:
                ddBet = anteBet
                if ddBet <= playerChips:
                    anteBet += ddBet
                    playerChips -= ddBet
                    dealerBet += ddBet
                    print()
                    print(f'Ante Bet: {anteBet}')
                    print()
                    print(f'Pair Plus: {pairPlus}')
                    pot += ddBet * 2
                    print()
                    print(f'Pot: {pot}')
                    break
                else:
                    print("Cannot place a double bet at this time.")
                    break
            break
        elif ddAsk == "NO" or ddAsk == "N":
            break
        else:
            print("Incorrect response. Try again.")

# Function to check card values and assign number values to each card
def checkCards(hand):
    # Creates empty lists
    cardNumbers = []
    cardSuits = []
    values = []

# Goes through each item in the "hand" (playerHand and dealerHand)
    for cards in hand:
        parts = cards.split(" of ") #Separates the suit and number and removes the "of" in between
        cardNumber = parts[0] #Assigns the number(s) from the split to a variable
        cardSuit = parts[1] #Assigns the suit(s) from the split to a variable
        cardNumbers.append(cardNumber) #Adds the numbers to the above cardNumbers list
        cardSuits.append(cardSuit) #Adds the suits to the above cardSuits list

    for number in cardNumbers: #Goes through each number and assigns a number value for each item in the cardNumbers list
        if number == "Ace":
            values.append(14)
        elif number == "Jack":
            values.append(11)
        elif number == "Queen":
            values.append(12)
        elif number == "King":
            values.append(13)
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

    if cardNumbers[0] == cardNumbers[1]:
        pairName = f'{cardNumbers[0]}'
    elif cardNumbers[1] == cardNumbers[2]:
        pairName = f'{cardNumbers[1]}'
    elif cardNumbers[0] == cardNumbers[2]:
        pairName = f'{cardNumbers[2]}'

    if straight and flush:
        return 6, "Straight Flush", values, "sflush"
    elif threeKind:
        return 5, "Three of a Kind", values, "3ofkind"
    elif straight:
        return 4, "Straight", values, "straight"
    elif flush:
        return 3, "Flush", values, "flush"
    elif pair:
        return 2, f'Pair of {pairName}', values, "pair"
    else:
        return 1, "High Card", values, "high"

# Function to identify and declare a winner
def gameWin(playerHand, dealerHand):
    global playerChips, dealerBet, dealerChips, pot, anteBet, pairPlus

    time.sleep(2.5)
    os.system("clear")

    print(f'Length of deck {len(deck)}')

    playerRank, playerName, playerVal, pHandRank = checkCards(playerHand)
    dealerRank, dealerName, dealerVal, dHandRank = checkCards(dealerHand)

    playerSum = sum(playerVal)
    dealerSum = sum(dealerVal)

    print(f'Player has: ', playerName)
    print()
    print(f'Dealer has: ', dealerName)
    print()

    pairSum = pairPlus * 2

    if playerRank > dealerRank and pHandRank == "pair":
        pot += pairSum
        playerChips += pot
        print(f'Player wins the {pot} chips pot')
        print()
        print(f'Player Chips: {playerChips}')
        pot = 0
        dealerBet = 0
        anteBet = 0
        time.sleep(5)
    elif playerRank > dealerRank:
        playerChips += pot
        print(f'Player wins the {pot} chips pot.')
        print()
        print(f'Player Chips: {playerChips}')
        pot = 0
        anteBet = 0
        dealerBet = 0
        pairPlus = 0
        time.sleep(5)
    elif dealerRank > playerRank:
        print(f'Dealer wins.')
        dealerChips += pot
        print()
        print(f'Player Chips: {playerChips}')
        dealerBet = 0
        anteBet = 0
        pot = 0
        pairPlus = 0
        time.sleep(5)
    elif playerRank == dealerRank or dealerRank == playerRank:
        while True:
            if playerSum > dealerSum and pHandRank == "pair":
                pot += pairSum
                playerChips += pot
                print(f'Player wins the {pot} chips pot.')
                print()
                print(f'Player Chips: {playerChips}')
                pot = 0
                dealerBet = 0
                anteBet = 0
                pairPlus = 0
                time.sleep(5)
                break
            elif playerSum > dealerSum:
                playerChips += pot
                print(f'Player wins the {pot} chips pot.')
                print()
                print(f'Player Chips: {playerChips}')
                pot = 0
                anteBet = 0
                dealerBet = 0
                pairPlus = 0
                time.sleep(5)
                break
            elif dealerSum > playerSum:
                print("Dealer wins.")
                dealerChips += pot
                print()
                print(f'Player Chips: {playerChips}')
                dealerBet = 0
                anteBet = 0
                pot = 0
                pairPlus = 0
                time.sleep(5)
                break
            else:
                print("Cannot determine winner.")
                time.sleep(3)
                break
    else:
        print("Tie")
        time.sleep(3)

# Assigns cards to player and dealer and removes them from the deck
playerHand = random.sample(deck,3)
deck = [card for card in deck if card not in playerHand]

dealerHand = random.sample(deck,3)
deck = [card for card in deck if card not in dealerHand]

# Confirm player wants to play game to initialize game
while True:
    os.system("clear")
    print(f'Player Chips: {playerChips}')
    print()
    startGame = input("Would you like to play poker? ").upper()

    if startGame == "YES" or startGame == "Y":
        initialBet()
        pairBet()
        doubleDown()
        gameWin(playerHand, dealerHand)

    elif startGame == "NO" or startGame == "N":
        exit()

    else:
        print("Incorrect response. Try again.")
        time.sleep(2)