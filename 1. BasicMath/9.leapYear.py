def leapYear(y):
    if y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False
y = int(input("Enter year y: "))
print(leapYear(y))