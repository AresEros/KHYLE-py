#GUESSING GAME
'''secret_word = 'fish'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input ('Enter guess: ')
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:

    print ('Out of guesses,YOU LOSE!')
else:
     print ('You win!')'''

# This is a guess the number game.
import random
secretNumber = random.randint(1, 30)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))