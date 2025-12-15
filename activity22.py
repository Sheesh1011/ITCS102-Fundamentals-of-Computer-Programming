import random
print("Guess the number")

value = random.randrange(1,5)
no_attempts = 0

while True:
    num = eval(input("Guess a number ==> "))

    if value == num:
        no_attempts += 1
        print(num,"Correct!")
        break
    else:
        no_attempts += 1
        print(num, "Incorrect!")
        continue

print("You had",no_attempts,"attempts!")