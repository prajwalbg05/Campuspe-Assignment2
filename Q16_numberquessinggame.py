#number guessing game
#Bonus (+3 points): Track best score (minimum attempts) and give hints when close (within 5). 
import random   
number = random.randint(1, 100)
attempts = 0
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")
while True:
    guess = int(input("Enter your guess: "))
    gap=abs(guess - number)
    attempts += 1
    if guess == number:
        print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
        break
    elif gap <= 5:
        print("You're very close! Try again.")
    elif guess < number and gap > 5:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
print("Thanks for playing!")