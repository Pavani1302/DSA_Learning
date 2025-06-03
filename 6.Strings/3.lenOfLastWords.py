def lenOfLastWord(s):
    words = s.split()
    return len(words[-1])

s = "Hello this is pavani"
print(lenOfLastWord(s))