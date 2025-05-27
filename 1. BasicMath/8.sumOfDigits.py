def sumDigits(n):
    sum = 0
    while n>0:
        last_digit = n % 10
        sum += last_digit
        n //= 10
    return sum

n = int(input("Enter number n: "))
print(sumDigits(n))