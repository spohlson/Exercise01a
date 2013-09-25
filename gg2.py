from random import randint
print "Welcome! Get ready for a guessing game!"
name = raw_input("What's your name? ")
number = randint (1,100)
tries = 0

print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name


while True:
    tries = tries + 1
    guess = int(raw_input("Your guess? "))
    if guess < number:
        print "Your guess is too low, try again."
    elif guess > number:
        print "Your guess is too high, try again."
    else:
        print "Well done, %s! You found my number in %d tries!" % (name,tries)
        break