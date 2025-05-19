import math
class Solution:
    def divisors(self,n):
        div = []
        sq = int(math.sqrt(n))
        for i in range(1,sq+1):
            if n % i == 0:
                div.append(i)
                if i != n // i:
                    div.append(n//i)
        div.sort()
        return div

sol = Solution()
print(sol.divisors(6))
print(sol.divisors(16))
print(sol.divisors(25))