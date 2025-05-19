class Solution:
    def divisors(self,n):
        div = []
        for i in range(1,n+1):
            if n%i==0:
                div.append(i)
        return div

sol = Solution()
print(sol.divisors(6))
print(sol.divisors(16))
print(sol.divisors(25))