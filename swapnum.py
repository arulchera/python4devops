
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if(num1<num2):
    num2=num1+num2
    num1=num2-num1
    num2=num2-num1
    print("the number has been swaped")
    print("First num:",num1)
    print("second num:",num2)
else:
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    print ("swaped")
    print("First num:", num1)
    print("second num:", num2)

