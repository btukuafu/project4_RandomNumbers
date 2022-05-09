import os

def random_card():
	return os.system("cmd /c python rng.py") % 52

def shuffle(cards):
	for i in range(len(cards)):
		place = random_card()
		cards[i], cards[place] = cards[place], cards[i]

names = [
	"", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"
]

def hand_value(hand):
	value = 0

	aces = 0
	for card in hand:
		if card == 1: aces += 1
		value += min(card, 10)
	
	if aces and value + 10 <= 21:
		value += 10

	return value

def handle_blackjack(house, player):
	house_blackjack = (house[1] == 1 or house[1] == 10) and house[0] + house[1] == 11
	player_blackjack = (player[1] == 1 or player[1] == 10) and player[0] + player[1] == 11

	if house_blackjack and player_blackjack:
		print(f"Dealt cards:\n\tHouse:\t{names[house[0]]}, {names[house[1]]} ({hand_value(house)})\n\tYou:\t{names[player[0]]}, {names[player[1]]} ({hand_value(player)})")
		print("It's a push")
		return True
	elif house_blackjack:
		print(f"Dealt cards:\n\tHouse:\t{names[house[0]]}, {names[house[1]]} ({hand_value(house)})\n\tYou:\t{names[player[0]]}, {names[player[1]]} ({hand_value(player)})")
		print("Blackjack, the house wins")
		return True
	elif player_blackjack:
		print(f"Dealt cards:\n\tHouse:\t{names[house[0]]}, {names[house[1]]} ({hand_value(house)})\n\tYou:\t{names[player[0]]}, {names[player[1]]} ({hand_value(player)})")
		print("Blackjack, you win")
		return True

def play():
	deck = [i+1 for i in range(13)] * 4
	# shuffle(deck)

	# deal cards
	house, player = [], []
	player.append(deck.pop())
	house.append(deck.pop())
	player.append(deck.pop())
	house.append(deck.pop()) # face up
	player = [1, 1]

	if handle_blackjack(house, player):
		return

	# get value
	print(f"Dealt cards:\n\tHouse:\t{names[house[1]]} (?)\n\tYou:\t{names[player[0]]}, {names[player[1]]} ({hand_value(player)})")

	# hit or stand
	answer = input("Hit (h) or Stand (s)?")
	while answer != "s":
		player.append(deck.pop())
		print(f"Dealt cards:\n\tHouse:\t{names[house[1]]} (?)\n\tYou:\t{[names[card] for card in player]} ({hand_value(player)})")
		if hand_value(player) >= 21: break
		answer = input("Hit (h) or Stand (s)?")

	if hand_value(player) > 21:
		print("You bust, the house wins")
		return

	# hit or stand house
	while hand_value(house) < 17:
		house.append(deck.pop())

	if hand_value(house) > 21:
		print(f"Dealt cards:\n\tHouse:\t{[names[card] for card in house]} ({hand_value(house)})\n\tYou:\t{[names[card] for card in player]} ({hand_value(player)})")
		print("The house busted, you win")
		return

	print(f"Dealt cards:\n\tHouse:\t{[names[card] for card in house]} ({hand_value(house)})\n\tYou:\t{[names[card] for card in player]} ({hand_value(player)})")
	if hand_value(player) > hand_value(house):
		print("Player wins")
	elif hand_value(house) > hand_value(player):
		print("House wins")
	else:
		print("It's a push")

play()