class Solution:
    def name(self,i,n):
        if i > n:
            return 
        print("sai")
        sol.name(i+1,n)

sol = Solution()
n = int(input("Enter how many times the name should be repeated: "))
sol.name(1,n)
