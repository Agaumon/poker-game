import random

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

deck = []

for suit in suits:
    for number in numbers:
        deck.append(f'{number} of {suit}')

random.shuffle(deck)

print(len(deck))

playerHand = random.sample(deck,2)
deck = [card for card in deck if card not in playerHand]

dealerHand = random.sample(deck,2)
deck = [card for card in deck if card not in dealerHand]

gameStatus = input("Play poker? ")

if gameStatus == "no".upper:
    exit()

else:
    exit()