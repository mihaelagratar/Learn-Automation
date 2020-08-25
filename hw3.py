#3.
tries = 1
import random
game = ["pencil", "vacation", "alex", "ana", "homework"]
print("You have to guess the following word")
a = random.choice(game)
b = input("The word is " + str(len(a)) + " letters long.\nGuess a letter: ")
for i in range(0, 4):
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
        if final == a:
            print("Yes, the word was", a)
            break
        else:
            print("No, the word was", a)
            break




