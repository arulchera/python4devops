str1=input("enter string")
char1=input("enter the char to be checked")
count = 0
i = 0
for i in range(len(str1)):
    if (str1[i] == char1):
        count=count+1

print("count is :",count)
