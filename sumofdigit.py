num=int(input("enter num:"))
sum=0
while num != 0:
    sum=(num%10)+sum
    num=num//10
print("sum is:",sum)


