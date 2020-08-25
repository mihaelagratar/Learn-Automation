#1.
while True:
    a = input("What's the starting number?")
    while not a.isdigit():
        a = input("You should enter a number:")
    else:
        a = int(a)
    b = input("What's the ending number?")
    while not b.isdigit():
        b = input("You should enter a number:")
    else:
        b = int(b)
    if b < a:
       print("The ending number should be greater than the starting one.")
       break
    c = input("What is the count?")
    while not c.isdigit():
        c = input("You should enter a number:")
    else:
        c = int(c)
    if c == 0:
        print("The counting number should be greater than 0.")
        break
    for i in range(int(a), int(b), int(c)):
        print(i)
    break
print()

#2.
name = input("What's your name?")
print(name[::-1])
print()

#4.
rows = 5
for i in range(0, rows):
    for j in range(0, i+1):
        print("*", end=" ")
    print()

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print()
print()
