str = "anaconda"
print("str[0]=", str[0])
print("str=[1:4]", str[1:4])
print("str=[-1]", str[-1])
print("str=[1:-2", str[1:-2])
print()

str1 = "Hello"
str2 = "Unicorns"
print(str1 + str2)
print(str2 * 3)
print()

count = 0
for letter in "Hello Unicorns":
    if letter == "o":
        count += 1
print(count, "letters found")
print()

str = "summer"
list_enumerate = list(enumerate(str))
print("list(enumerate(str)= ", list_enumerate)
print("len(str) =", len(list_enumerate))
print()

print("She said, \"Who is this boy?\"")