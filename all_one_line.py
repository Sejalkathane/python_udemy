# mystring='hello'
# mylist=[]
# for letter in mystring:
#       mylist.append(letter)
#       print(mylist)

#Dont do this typr becaue it is not easy to read
#❎❎

# mylist=[x for x in 'word']
# print(mylist)

mylist =[x for x in range(0,11)]
print(mylist)

a=[num**2 for num in range(1,11)]
print(a)

b=[num*2 for num in range(1,11)]
print(b)

c=[x for x in range(0,11) if x%2==0]
print(c)


me=[]
for x in [2,3,4]:
    for y in [1,10,100]:
         me.append(x*y)
print(me)