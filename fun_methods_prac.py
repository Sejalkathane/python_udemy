#fun to find volume of given sphere

# def funsp(rad):
#     vol=4/3*3.14*rad*rad*rad
# #     4/3*3.14*rad**3
#     print(vol)

# funsp(2)


#...................................................................................


#Write a function that checks whether a number is in
#  a given range (inclusive of high and low)


# def ran_check(num,low,high):
#     if(num in range(low,high+1)):
#         return True
#     else:
#         return False

# print(ran_check(4,1,5))
# print(ran_check(3,1,10))
# print(ran_check(78,1,4))



#...................................................................................

# Write a Python function that accepts a string and calculates
# the number of upper case letters and lower case letters.

#HINT: Two string methods that might prove useful: .isupper() and .islower()


# def up_low(s):
#       #distionary method
#       d={'upper':0,'lower':0}

#       for char in s:
#             if char.isupper():
#                   d['upper']+=1  
#             elif char.islower():
#                   d['lower']+=1
#             else:
#                   pass

#       print(d["lower"])
#       print(d["upper"])

   #variable method
      # lowercase=0
      # uppercase=0

      # for char in s:
      #       if char.isupper():
      #             uppercase+=1  
      #       elif char.islower():
      #             lowercase+=1
      #       else:
      #             pass
      # print(uppercase)
      # print(lowercase)
      
# up_low('Hi I am Sejal')


#...................................................................................


#Write a Python function that takes a list and returns a new
#  list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# def unique_list(lst):
#        return list(set(lst))

#another way to do this:
# def unique_list(lst):
#       seen_no=[]
#       for num in lst:
#             if num not in seen_no:
#                   seen_no.append(num)
#       return seen_no

#print(unique_list([1,1,1,3,5,3,3,4,4,4,5,5,5,5]))


#...................................................................................



#

# def mult(num):
#       total =1
#       for n in num:
#             total=total*n

#       return total

# print(mult([2,9,4]))
      
#...................................................................................



#check given string is palidrom is or not 
#palidron means same read from backward and infront
# def palidrom(s):
#       s=s.replace(' ','')
#       return s==s[::-1]

# print(palidrom('karaarak'))
# print(palidrom('hi i am sejal'))



#Hard
# import string
# def ispangram(str1,alphabet=string.ascii_lowercase):
      
#       #create aset of given alphabet
#       alphaset=set(alphabet)

#      #remove any spaces from the input string
#       str1=str1.replace(' ','')

#       #convert all in lower case
#       str1=str1.lower()

#       #grab all unique letters from the string set()
#       str1=set(str1)

#       #alphabet set== string set input
#       return str1==alphaset

# print(ispangram("The quick brown fox jumps over the lazy dog"))
    



