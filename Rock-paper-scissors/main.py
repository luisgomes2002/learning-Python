import random

playerPoints = 0
computerPoints = 0
rouds = 1

def computerOption():
		num = random.randint(1, 3)
		if num == 1:
				return 'r'
		elif num == 2:
				return 'p'
		else:
				return 's'
		
def verifyWinner(playerChoice, computerChoice):
	global playerPoints, computerPoints, rouds

	if playerChoice == computerChoice:
		print("Tie")
	elif(playerChoice == "r" and computerChoice == "s") or \
			(playerChoice == "p" and computerChoice == "r") or \
			(playerChoice == "s" and computerChoice == "p"):
		print("You Win")
		playerPoints += 1
	else:
		print("You lose")
		computerPoints += 1
	print("****************************************************")
	print("                     Results                        ")
	print(f"Player choise: {playerChoice} Computer Choise: {computerChoice}")
	print(f"Player score:  {playerPoints} Computer score: {computerPoints}")
	print("****************************************************")
	rouds += 1

def main():
	global playerPoints, computerPoints, rouds

	while rouds < 4:
		while True: 
			print("Round: ", rouds)
			playerChoice = input("Enter r to Rock, p to Paper and s to Scissors: ").lower()
			
			if playerChoice == 'r' or playerChoice == 'p' or playerChoice == 's':
				computerChoice = computerOption()
				verifyWinner(playerChoice, computerChoice)
				break 
			else:
				print("Invalid input. Please enter r, p, or s.")
		
main()