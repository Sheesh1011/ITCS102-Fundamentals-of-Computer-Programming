#Enter 7 random numbers, get the summation at all ODD number given
print("ODD number summation")

sum = 0
for k in range(1,8,1):
    number = eval(input("Enter a number: "))
    if number % 2 == 0:
        number = 0
    
    else:
        sum += number

print("The sum of all odd number is", sum)