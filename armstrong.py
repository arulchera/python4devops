num=int(input("num:"))
num1=num
sum=0
d=0
while num != 0:
    d=num%10
    sum=(d*d*d)+ sum
    num=num//10
if ( sum == num1 ):
    print("Armstrong")
else:
    print("Not Armstrong")