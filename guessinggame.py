from random import randint

print "Hullo! What's your name?"
name = raw_input()

print "I've got a game for you, %s." % name
print "I'm thinking of a number between 1 and 100. Guess my number."
guess = int(raw_input())

number = randint(1,101)

while guess != number:
    if guess < number:
        print "Too low, guess again."
    else:
        print "Too high, guess again"
    guess = int(raw_input())

print "Right on! You win!"