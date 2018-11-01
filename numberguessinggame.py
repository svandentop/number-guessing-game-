import name
import random
num_1 = random.randint(1,21)
my_name = name.get_full_name()
print("Hello, " + my_name)
print("I'm thinking of a number between 1 and 20. Try to guess it, but be careful. Three strikes and you're out!")
guess = int(raw_input("What is your first guess?\n"))
if guess == num_1:
    print("You guessed the correct number!")
else:
    print("That's not it. Guess again.")
while guess == num_1:
    break
if guess >= num_1 - 3 and guess < num_1:
    print("You almost got it! Guess a little higher.")
if guess < num_1 - 3:
    print("Your guess is too low.")
if guess > num_1 and guess <= num_1 + 3:
    print("You almost got it! Guess a little lower.")
if guess > num_1 + 3:
    print("Your guess is too high.")
second_guess = int(raw_input("What is your second guess?\n"))
if second_guess == num_1:
    print("You guessed the correct number!")
else:
    print("That's not it. Guess again.")
while second_guess == num_1:
    break
if second_guess >= num_1 - 3 and second_guess < num_1:
    print("You almost got it! Guess a little higher.")
if second_guess > num_1 and second_guess <= num_1 + 3:
    print("You almost got it! Guess a little lower.")
if second_guess > num_1 + 3:
    print("Your guess is too high.")
if second_guess < num_1 - 3:
    print("Your guess is too low.")
third_guess = int(raw_input("What is your third guess?\n"))
if third_guess == num_1:
    print("You guessed the correct number!")
else:
    print("That's not it. That was strike three. Sorry, you're out. The number was " + str(num_1) + ". " + "Thanks for playing!")
while third_guess == num_1:
    break








