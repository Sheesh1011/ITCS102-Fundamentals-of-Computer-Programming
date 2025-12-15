for k in range(1,11,1):
    for p in range(10, k ,-1):
        print(" ", end='')
    for r in range(1, k, 1):
        print("x", end='')
    for b in range(1, k, 1):
        print("x", end='')
    print()

for k in range(1,11,1):
    for p in range(k,1,-1):
        print(" ",end='')
    for r in range(10,k,-1):
        print("x",end='')
    for b in range(10,k,-1):
        print("x",end='')
    print()