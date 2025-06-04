import random

print("Guess My Number")


# Psuedocode:

# Selected a secret number from 1 to 100
# Create a counter variable set to 0

# Start a loop:
#   Prompt the user to guess a number
#   Save their guess as a number
#   Increment the counter variable
#   if their guess was too high, say too high
#   if their guess was too low, say too low
#   if their guess was correct, say correct AND stop looping!

# Tell the user how many guesses it took (the counter)

secret_number = random.randint(1, 100)
# print(secret_number) # TODO: Remove this later!
counter = 0

while True:
    guess = int(input("Guess a number: "))
    counter += 1
    if guess > secret_number:
        print("That guess was too high.  Guess lower")
    if guess < secret_number:
        print("That guess was too low.  Guess higher")
    if guess == secret_number:
        print("That guess was correct! Well done!")
        break

print(f"You got it in only {counter} guesses.")
