#2.
a_list = [2, 4, 6, 8, 10, 12]
def b(a_list):
    return [a_list[0], a_list[-1]]
print(b(a_list))
print()
#3.
def fib (a, b):
    return a + b
x = int(input("How many Fibonacci numbers should I generate? "))
fibonacci_list = []
for n in range(x):
    if n in [0, 1]:
        fibonacci_list += [1]
    else:
        fibonacci_list.append(fib(fibonacci_list[n-1], fibonacci_list[n-2]))
print("The first", x, "Fibonacci numbers are:", fibonacci_list)
print()
#1.
y = int(input("What's the number?"))
def z(n):
    result = 0
    for i in range(n + 1):
        result = result + i
    return result
print(z(y))
print()
#4.
bla = 'print("Como estas?")'
blabla = """
def sum(x,y):
    return x+y
print("Sum is" , sum(20, 23))
"""
exec(bla)
exec(blabla)
