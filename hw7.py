#1.
import random
a = ["cat", "dog", "horse", "parrot", "chicken"]
random.shuffle(a)
print(a)
print()

#2.

b = [3, 4.5, 234, "plane", 8.9, [1, 2, 3], "car", 67, "bike", 5.8]
result = 0
for i in b:
    if type(i) == int or type(i) == float:
        result = result + i
    if type(i) == list:
        for i2 in i:
            result = result + i2
print(result)





