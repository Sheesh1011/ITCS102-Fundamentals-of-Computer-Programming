n1 = eval(input("Enter your first number: "))
n2 = eval(input("Enter your second number: "))

add = n1 + n2
minus = n2 - n1
multiply = n1 * n2
divide = n2 / n1
exponent = n1**n2
remainder = n1 % n2
fd = n1 // n2


print("The sum of", n1,"and",n2,"is",add)
print("The difference of",n2,"and",n1,"is",minus)
print(n1,"multiplied by",n2,"is",multiply)
print(n2,"divided by",n1,"is",divide)
print(n1,"exponent by",n2,"is",exponent)
print("The remainder of",n1,"and",n2,"is",remainder)
print("The floor division of",n1,"and",n2,"is",fd)

