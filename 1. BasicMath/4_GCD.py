class Solution:
    def gcd(self,n1,n2):
        while n2 != 0:
            rem = n1 % n2
            n1 = n2
            n2 = rem
        return n1

sol = Solution()
print(sol.gcd(8,6))
print(sol.gcd(5,18))