import random
def check_user_input(gn,mn):

	closeness = ((mn - gn)/mn)*100

	if  0 < closeness < 50:
		return "Guessed number is SMALL."
	elif closeness > 50 :
		return "Guessed number is TOO SMALL."
	elif  0 > closeness > -50:
		return "Guessed number is LARGE."
	elif closeness < -50 :
		return "Guessed number TOO LARGE."
		
	

def guess_number():
	try:
		print("WELCOME! to number guessing game.",end="\n")
		print("Guess the magic number under 5 attempts and win rewards.",end="\n\n")
		
		magic_number = random.randint(1,100)
		reward_multiplier = {1: 5 , 2 : 3 ,3 : 2 , 4 : 1.5 , 5 : 1 }
		entry_fee = int(input("Enter entry fee: "))
		print("",end="\n")
		print("GAME STARTED")
		for attempt in range(1,6):
			print("Attempts remaining: " + str(6- attempt))
			guessed_number = int(input("Guess the magic number between 1 to 100: "))
			
			if guessed_number != magic_number:
				print(check_user_input(guessed_number,magic_number),end="\n\n")
			
			else:
				reward = entry_fee*reward_multiplier[attempt]
				print(f"\nCONGRATULATIONS! You have guessed the number correct.\nYou have earned {reward} rupees in reward.")
				break
		else:
			print("The magic number was " + str(magic_number))
	except ValueError:
		print("INVALID INPUT ENTERED. PROGRAM TERMINATED")
	
guess_number()
			
			
			
					
			
