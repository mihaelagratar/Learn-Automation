#3.
message1 = "Have an awesome day!"
message2 = "Have a good day!"
message3 = "Have a wonderful day!"
b = 10
c = int(input("Whats's the number?"))
if c < b:
    print(message1)
elif c == b:
    print(message3)
else:
    print(message2)


#1.
for i in range(1500, 2701):
    if i % 7 == 0 and 0 == i % 5:
        print(i)

