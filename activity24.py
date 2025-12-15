from activity24_1 import info, cont

cont(input("Are you a Kpop Idol (yah/nah): "))
if cont == 'yah':
    print("Jagiya!")
elif cont == 'nah':
    print("Mwo?")
else:
    print("What are you?")

print("\nWould you marry me, jagiya? But first, please introduce yourself.\n")
name = input("Who: ")
age = input("Age: ")
location = input("From: ")

info(name, age, location)