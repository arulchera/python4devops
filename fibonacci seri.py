def fun1(n):
   for i in range(2,n):
       sum=mylist[i-1]+mylist[i-2]
       mylist.append(sum)

x=0
y=1
mylist=[]
n=int(input("plz enter the number of series"))
mylist.append(x)
mylist.append(y)
fun1(n)
print("mylist:",mylist)