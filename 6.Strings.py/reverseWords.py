def reverseWords(s: str) -> str:
    words = s.split()
    revStr = ''
    for i in range(len(words)-1,-1,-1):
        revStr = revStr + " " + words[i]
    return revStr.strip()

s_1 = "the sky is blue"
print(reverseWords(s_1))
s_2 = "  hello world  "
print(reverseWords(s_2))