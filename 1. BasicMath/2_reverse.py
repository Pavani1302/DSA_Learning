# This only works for positive numbers
class Solution:
    def reverse(self,n):
        revNum = 0
        while (n>0):
            rem = n % 10
            revNum = (revNum*10) + rem
            n = n // 10
        return revNum
sol = Solution()
print(sol.reverse(153))
print(sol.reverse(21546))