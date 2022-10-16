for num in range(11):
    print(num)

print('.....................')

for a in range(1,6):
    print(a)

print('.....................')

for b in range(1,11,2):
    print(b)
print('.....................')
for c in range(0,11,2):
    print(c)

print('.....................')

print(list(range(0,11,2)))

print('.....................')



index_count=0
word='sejal'
# for letter in 'sejal':     
#     print('at index {} the letter is {}'.format(index_count,letter))
#     index_count +=1

for letter in word:
    print(word[index_count])
    index_count +=1


print('.....................')

word='sejal'
# for item in enumerate(word):     #print in tuple form 
#     print(item)
for index,letter in enumerate(word):     #print whwtever you want is index value or letter
    print(index)
    print(letter)
    print('\n')


print('.....................')

mylist1=[1,2,3]
mylist2=['a','b','c']
# for item in zip(mylist1,mylist2):   # print this in tuple format
#     print(item)

for a,b in zip(mylist1,mylist2):
    print(b)

print('.....................')
# check wheather this value is present in loop or not return true or false

# 1 in [1,2,3]
# True
from random import shuffle
print(1 in[1,2,3])
print('g' in 'sejal')
print('.....................')

d={'mykey':123}   #present in distionary or not
print(123 in d.values())     #present as value
print(123 in d.keys())       #present as key





