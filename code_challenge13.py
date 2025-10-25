name = input("Type your name---> ")
print(" +++++++++++++++++++ ")
print("ODD NUMBER SUMMATION (press 0 to stop) ")
print(" ++++++++++++++++++++\n ")

number = True
sum = 0
odd = " " #string

while number == True:
        num = eval(input("Input a Random number ---> "))
        
        if num % 2  == 1:
            print("ODD NUMBER DETECTED, the code continues")
            sum += num
            odd += str(num) + " "
            continue
        elif num == 0:
             print("Program Stops!")
             break
        else:
             if num % 2 == 0:
                 print("EVEN NUMBER DETECTED, continue")
             else:
                     print("invalid input")
                     continue
print(f"Hello {name}, the sum of all odd number is {sum}")
print(f"ODD Numbers Detected included the following {odd}")