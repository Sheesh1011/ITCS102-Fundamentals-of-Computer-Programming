
print("MULTIPLICATION TABLE MAKER")
a = eval(input("Enter a number: "))
print("\nMultiplication table for",a,":")
for k in range(1, 11, 1):
    b = a * k
    print(a,"x",k,"=",b)