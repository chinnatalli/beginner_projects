import random


def guess(x):
    random_number=random.randint(1,x)
    guess =0
    while guess!=random_number:
        guess =int(input(f'guess a number between 1 to {x}: '))
        if guess >random_number:
            print("sorry ,guess agin . too high")
        elif guess < random_number:
            print("sorry,guess again. too low")
    print(f"Yay ,congrats ! you have guessed the number {random_number} correctly!!")


guess(10)