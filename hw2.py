#1.
a = int(input("What's the starting number?"))
b = int(input("What's the ending number?"))
c = int(input("What is the count?"))
for i in range(a, b, c):
    print(i)
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
