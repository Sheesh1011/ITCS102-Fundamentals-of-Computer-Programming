candy = True

while candy == True:
    flavor = input("Is the candy sweet? (yes/no): ").lower()
    if flavor == 'no':
        print("Yuck!")
        continue
    else:
        print("Tasty!")
        break