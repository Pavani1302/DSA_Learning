def starPyramid(n):
    for rows in range(1,n+1):
        for spaces in range(n - rows):
            print(" ", end="")
        for stars in range(1, 2 * rows):
            print("*", end="")
        print()
n = int(input("Enter n: "))
starPyramid(n)