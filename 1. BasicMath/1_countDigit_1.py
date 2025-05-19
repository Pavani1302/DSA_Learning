class Solution:
    def countDigit(self,n):
        count = 0
        while n>0:
            count += 1
            n = n // 10
        return count
cnt = Solution()
print(cnt.countDigit(12345))
print(cnt.countDigit(9812345671223))
