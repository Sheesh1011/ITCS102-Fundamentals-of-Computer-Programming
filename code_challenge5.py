print("THE FACTORIAL PROGRAM")

prod = eval(input("Enter any number: "))
factor = 1
for k in range(prod, 0, -1):
    factor *= k
print("The factorial of",prod,"is", factor)