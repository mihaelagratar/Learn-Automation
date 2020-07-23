#3.
tries = 1
import random
game = ["student", "homework", "vacation", "notebook", "pencil"]
print("You have to guess the following word related to school.")
a = random.choice(game)
correct = a
length = len(a)
length = str(length)
b = input("The word is " + length + " letters long. Guess a letter: ")
for i in range(1, len(a)):
    if b not in a:
        print("Try again.")
        tries = tries + 1
        b = input()
    else:
        print("Guess another letter")
        tries = tries + 1
        b = input()
    if tries == 5:

        final = input("The word is:")
        if final == correct:
            print("Yes, the word was", a)
            break
        else:
            print("No, the word was", a)
            break




