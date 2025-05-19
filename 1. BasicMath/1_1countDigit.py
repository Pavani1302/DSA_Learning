class Solution:
    def countDigit(self,n):
        count = len(str(n))
        return count
sol = Solution()
print(sol.countDigit(29))
print(sol.countDigit(12345234))