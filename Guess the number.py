import random
def guess(x):
    guess=0
    random_number=random.randint(1,x)
    while(guess!=random_number):
        guess=int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_number:
            print('Sorry,guess again.Too low.')
        elif guess>random_number:
            print('Sorry,guess again.Too high')
    print(f"You have guess correct random number{random_number}")
guess(100)