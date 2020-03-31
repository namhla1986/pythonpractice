"""This is an example of a guessing game. It will combine some of the things i have learned so far. The If
and comparative statements. It will also contain a while loop. The aim of this is for someone to guess the correct
secret word, so the loop will keep going until they guess correctly. They will be given 3 turns and after guessing
incorrectly it will execute the default statement"""
secret_password = "python"
guesses = ""
number_of_guesses = 0
guess_limit = 3
out_of_guesses = False

print("Welcome to our Guessing Game!! Try guessing the correct word")
while guesses != secret_password and not(out_of_guesses):
    if number_of_guesses < guess_limit:
        guesses = input("Enter your guess: ")
        number_of_guesses += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose")
else:
    print("You win!")
