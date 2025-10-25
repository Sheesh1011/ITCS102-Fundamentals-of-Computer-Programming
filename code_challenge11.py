print("\t\t *" ,end=" ")
for k in range(1, 11, 1):
    for p in range(10, k, -1):
            print(" ", end =" ")
    for m in range(1, k, 1):
            print("*", end=" ")
    for r in range(1, k, 1):
             print("*", end=" ")
    print()