class Solution:
    def palindrome(self,n):
        revNum = 0
        temp =  n
        while temp>0:
            lastDigit = temp % 10
            revNum = (revNum*10) + lastDigit
            temp = temp // 10
        if revNum == n:
            return "Palindrome Number"
        else:
            return "Not Palindrome"
pal = Solution()
print(pal.palindrome(-2332))
print(pal.palindrome(2332))
print(pal.palindrome(1234))
print(pal.palindrome(10))