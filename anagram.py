str1=input("enter the str1")
str2=input("enter the str2")
l1=list(str1)
l2=list(str2)
l1.sort()
l2.sort()
print("l1:",l1)
print("l2:",l2)
if l1 ==l2:
    print("its anagram")
else:
    print("its not anagram")
