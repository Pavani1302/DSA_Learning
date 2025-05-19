class Solution:
    def prime(self,n):
        if n <= 1:
            return False
        for i in range(2,n):
            if n % i == 0:
                return False
        return True      
sol = Solution()
print(sol.prime(5))
print(sol.prime(26))
print(sol.prime(1))