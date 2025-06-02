def indexOfFirstOcc(str_1, str_2):
    for i in range(len(str_1)):
        if str_2 == str_1[i:i+len(str_2)]:
            return i
    return -1

str_1 = "butsad"
str_2 = "sad"
print(indexOfFirstOcc(str_1,str_2))