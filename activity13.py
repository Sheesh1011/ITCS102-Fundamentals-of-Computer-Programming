#ask user to input ten(10) numbers
#after, get the summation of all numbers

plus = 0
for n in range(1,11,1):
    print(n)
    add = eval(input("Enter any number: "))
    plus += add

print("The sum of the given numbers is:", plus)