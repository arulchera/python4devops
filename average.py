input_string = input('Enter elements of a list separated by space ')
user_list = input_string.split()
print('list: ', user_list)
for i in range(len(user_list)):
       user_list[i]=int(user_list[i])
sum1=sum(user_list)
avg=sum1/len(user_list)
print("avg:",avg)


