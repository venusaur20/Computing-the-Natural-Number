import math

def exp(x,accuracy):
    e = sum([
        x**n / math.factorial(n)
        for n in range(0,accuracy)
    ])
    return e

x = complex(input("The 'x' value: "))
accuracy = int(input("Your preferred accuracy: "))
print(exp(x,accuracy))
