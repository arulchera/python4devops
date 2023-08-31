def strfn(mystr):
   count=0
   for i in mystr:
     count=count+1
   return count

mystr=input("enter the string you want to see the length")
lenstr=strfn(mystr)
print("the length of string is:",lenstr)
