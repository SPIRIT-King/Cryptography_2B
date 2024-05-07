str = "abcdefg"
str_list = list(str)
for i in range(len(str_list)):
    str_list[i] = ord(str_list[i])-ord("a")+1
print(str_list)
