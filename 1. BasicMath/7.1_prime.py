import math
class Solution:
    def prime(self,n):
        sq = int(math.sqrt(n))
        if n <= 1:
            return False
        for i in range(2,sq+1):
            if n % i == 0:
                return False
        return True      
sol = Solution()
print(sol.prime(5))
print(sol.prime(26))
print(sol.prime(1))