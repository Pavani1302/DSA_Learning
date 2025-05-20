def Nto1(n,i):
    if n<1:
        return 
    print(n, end=" ")
    Nto1(n-1,i)
n = int(input("n: "))
Nto1(n,1)