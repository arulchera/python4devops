year=int(input("enter year"))
if((year%400 == 0) | (year%100 != 0) & (year%4 == 0)):
    print("yes this is leap year")
else:
    print("no this is not leap year")
