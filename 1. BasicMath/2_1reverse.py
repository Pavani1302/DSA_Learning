# This works for both positive and negative numbers
class Solution:
    def reverse(self,n):
        revNum = 0
        if n < 0:
            sign = -1
        else:
            sign = +1
        n = abs(n) 
        while (n>0): 
            rem = n % 10
            revNum = (revNum*10) + rem
            n = n // 10
        revNum *= sign
        if revNum < -2**31 or revNum > 2**31-1:
            return 0
        return revNum
sol = Solution()
print(sol.reverse(-153))
print(sol.reverse(21546))
print(sol.reverse(98271234567))