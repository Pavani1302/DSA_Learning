class Solution:
    def amr(self,n):
        temp = n
        sum = 0
        length = len(str(n))
        while temp>0:
            lastDigit = temp % 10
            sum += lastDigit ** length
            temp = temp // 10
        return sum == n
sol = Solution()
print(sol.amr(153))
print(sol.amr(1234))