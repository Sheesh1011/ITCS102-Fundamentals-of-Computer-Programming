multiply = 1
for k in range(1,6):
    prod = eval(input(f"{k}. Give a number: "))
    multiply *= prod
print(f"The sum of all numbers given is {multiply}")
