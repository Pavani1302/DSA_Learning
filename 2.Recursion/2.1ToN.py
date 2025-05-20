def oneToN(i,n):
    if i > n:
        return
    print(i, end= " ")
    oneToN(i+1,n)
n = int(input("Enter how many numbers you want to print: "))
oneToN(1,n)