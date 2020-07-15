for i in range(5):
    print(i+2)
for i in range(5):
    print(i+1, end=(' ' if i < 4 else '\n'))
print()
for i in "Datacamp":
    if i == "D":
        print(i)
print()
sequence = [1, 2, 3, "vaca", "bou", "vaca", "bou"]
for i in sequence:
    print(i)
print()
sequence = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(sequence)):
    print(sequence[i])
print()
for i in range(1, 15, 3):
    print(i)
print()
for i in range(10):
    for j in range(i):
        print(i, end=" ")
    print()

