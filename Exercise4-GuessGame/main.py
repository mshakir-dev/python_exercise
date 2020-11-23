import random
guessesTaken = 0
print('Hello! What is your name?')
myName = input()
number = random.randint(1, 10)
while guessesTaken < 5:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed the right number in ' + guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope, ' +myName+ '.  The Correct number is ' + number)
