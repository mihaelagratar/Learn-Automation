#2
print("Guess a number between 1 and 9")
a = int(input("Enter a guess:"))
while (a > 9) or (a < 1):
    a = int(input("Enter a guess:"))
else:
    print("Well guessed!")

