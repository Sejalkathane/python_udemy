#syntax of for loop
# my_iterable=[1,2,3]
# for item_name in my_iterable:
#     print(item_name)





my_list=[1,2,3,4,5,6,7,8,9,10]
for li1 in my_list:
    print(li1)

#print string multiple time
for li2 in my_list:
         print('hello')


for num1 in my_list:   #check an even number
    if num1 %2==0:
        print(num1)


for num2 in my_list:   #check an odd number
    if num2 % 2!=0:
        print(num2)


for num3 in my_list:   #check an even and odd both number
    if num3 %2==0:
        print(f"Even Number : {num3}")
    else:
        print(f"Odd Number : {num3}")



#sun of number
list_sum=0
for num4 in my_list:
    list_sum=list_sum+num4
    print(list_sum)



#for loop in list📑📜
mylist=[(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))
for item in mylist:
    print(item)
for a,b in mylist:
    print(b)



#For loop in dictionary 📓📓
d={'k1':1,'k2':2,'k3':3}
for item in d.items():
    print(item)

for key,value in d.items():
    print(value)

for value in d.values():
    print(value)