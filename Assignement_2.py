# Use for.split() and if to create a statment that 
#    will print out words that stat with 's'::

#1.
st='Sam print only the words that start with s in this sentence'
for word in st.split():
    if word[0]=='s':
       print(word)



#2
# for i in range(0,11):
#     if i%2==0:
#        print(i)

#list(range(0,11,2))        its also correct


#3
#Use a list comprehension to create a list of all numbers between
#  1 and 50 that are divisible by 3
# for a in range(1,51):            
#         if a%3==0:
#           print(a,end=' ')      



#Go through the string below and if the length of a word
#  is even print"even"!
#4.
s='Print every word in this sentence that has an even number of letters'
for word in s.split():
    if len(word)%2==0:
        print(word+' is even!')






#5
#Write a program that prients the integer from 1 to 100 . But for 
# multiple of three print"Fizz" and for 5 print"Bizz".
#  For numbers which which are multiple of both print''

# for b in range(1,101):
#     if(b%3==0 and b%5==0):
#         print('FizzBuzz')
#     elif(b%3==0):
#         print('Fizz')
#     elif(b%5==0):
#         print('Bizz')
#     else:
#         print(b)




#6.
#Use list comprehension to create a list of the first letters 
#     of every word in the string bellow:
st1='Create a list of the first letters of every word in the string'
for word in st1.split():
       print(word[0],end=' ')
