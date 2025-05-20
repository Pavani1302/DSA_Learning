def pali(s):
    s_new = ''
    for char in s:
        if char.isalnum():
            s_new += char.lower()
    return s_new == s_new[::-1]

s = input("Enter the string: ")
print(pali(s))