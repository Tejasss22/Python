import random

def guess_number():
	number = random.randint(1,10)
	guessed_number = int(input("guess a number between 1 to 10: "))
	if guessed_number == number:
		return "You guessed the number correct."
	else:
		return "You guessed the number wrong."
		
print(guess_number())
