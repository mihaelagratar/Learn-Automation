#2
#import random
from random import randint
a = randint(1, 9)
while True:
    b = int(input("Enter a guess: "))
    if a == b:
        print("Well guessed!")
        break
    else:
        print("Try again!\n")

