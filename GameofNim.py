# Se Yeon Bark
# Game of Nim
# Feb 14 2023

import random, os, time

Turn = random.choice('01')  # '0' is human player and '1' is computer.

# determine how many stones there will be in the game.
Pile = random.randint(22, 33)


def name():
	# Pre: set the title of the game in this function
	# Post: When this function is called, print the title at the top of the screen
	os.system('color B')
	print("""
	
	 _____ ____  _      _____   ____  _____   _      _  _     
	/  __//  _ \/ \__/|/  __/  /  _ \/    /  / \  /|/ \/ \__/|
	| |  _| / \|| |\/|||  \    | / \||  __\  | |\ ||| || |\/||
	| |_//| |-||| |  |||  /_   | \_/|| |     | | \||| || |  ||
	\____/\_/ \|\_/  \|\____\  \____/\_/     \_/  \|\_/\_/  \|
	                                                          
	               """)


while True:

	name()  # Call name function to print the title on screen
	print("There are " + str(Pile) + " stones.")  # Indicate the number of stones after each turn
	print(Pile * '@ ')  # stones are @. Print number of stones. After each turn, the number of stones will decrease
	time.sleep(1)  # After 1 second, turn goes to the next player

	# Human player
	if Turn == '0':
		# Input statement to ask the player how many stones they want to take
		Take = int(input("It's your turn. \nHow many stones would you like to take? "))
		if 1 <= Take <= 3:  # Player can only take 1 to 3 stones
			print("You removed", str(Take), 'stone(s)')
			# Deduct the number of stones that player want to take away from the original number
			Pile -= Take

		# When the player inputs a number other than a range between 1 and 3
		while Take not in range(1, 4):
			print("Invalid number!")  # Print this when player inputs wrong number
			Re_Input = int(input("Please pick a number between between 1-3: "))  # Ask player to input the number again
			if 1 <= Re_Input <= 3:  # When re-input number is correct
				Pile -= Re_Input  # Subtract the number from original number of stones

				break  # break the loop

		os.system('cls')  # After human player's turn, clear the screen
		
		# When there is one stone left after the player's turn, the human player wins
		if Pile == 1:
			os.system('color 2')
			print('''
	█▀▀ █▀█ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀ █   █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█   █░█░█ █ █▄░█ █
	█▄▄ █▄█ █░▀█ █▄█ █▀▄ █▀█ ░█░ ▄█ ▄   █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄   ▀▄▀▄▀ █ █░▀█ ▄''')
			break # Stops the loop, game is over

		Turn = '1' # Computer's turn after the human player's turn

	# Computer's turn
	elif Turn == '1':

		# Computer chooses stones between 1 and 3 to take away
		ChooseStone = random.choice('123')

		# Indicate it's computer's turn
		print("Computer's turn")
		print("Computer took", ChooseStone, "stone(s).")
		# Subtract the randomly picked number from 1 to 3 from the original number of stones
		Pile -= int(ChooseStone)

		# When less than 3 stones are left
		while Pile < 4:
			# Computer only picks 1 or 2 stone(s)
			ChooseStone = random.choice("12")
			break  # Stops randomly picking stones
			while Pile == 2:
				ChooseStone == "1"
			print("Computer took", ChooseStone, "stone(s).")
			Pile -= int(ChooseStone)

		time.sleep(1)
		os.system('cls')  # clear the screen after computer's turn
		
		# When there is one stone left after computer's turn, the human player loses.
		if Pile == 1:
			os.system('color 4')
			print("""
	█▀ █▀█ █▀█ █▀█ █▄█   █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█ ░   █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
	▄█ █▄█ █▀▄ █▀▄ ░█░   █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄ █   ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄""")

			break # Stops the loop, game is over

		Turn = '0' # Human player's turn after computer's turn
