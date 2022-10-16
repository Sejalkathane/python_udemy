
#1.grater and even no :

# def fun1(a,b):
#     if (a%2)==0 and (b%2)==0:
#         if a<b:
#             print(a)
#         else:
#             print(b)
#     else:
#         if a>b:
#             print(a)
#         else:
#             print(b)
        
#     # elif (a%2)==0 and (b%2)!=0:
#     #     print(a)
#     # elif (a%2)!=0 and (b%2)==0:
#     #     print(b)
#     # elif (a%2)!=0 and (b%2)!=0:
#     #      if a>b:
#     #             print(a)
#     #      else:
#     #         print(b)

# (fun1(2,5))
# (fun1(2,4))


        

#find is in sentence every word start with given letter or not
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

# def an(text):
#    wordlist= text.split()
#    first=wordlist[0]
#    second=wordlist[1]

#    return first[0]==second[0]
     
# print(an('life life'))
# print(an('Live rife'))



#if both no sum is 20 or one of the no is 20 return true else return false
# def no(a,b):
#     #return (a+b)==20 or a==20 or b==20
#     if(a+b)==20 or a==20 or b==20:
#         return True
#     else:
#         return False


# print(no(20,3))
# print(no(2,20))
# print(no(15,5))
# print(no(20,20))
# print(no(2,3))


    
    
    #LEVEL 1 PROBLEMS::

#1. : Write a function that capitalizes the first and fourth letters of a name ex: old_macdonald('macdonald') --> MacDonald

# def mac(a):
#     first_letter=a[0]
#     inbetween = a[1:3]
#     fourth_letter=a[3]
#     remaning=a[4:]
    
#     return first_letter.upper()+inbetween+fourth_letter.upper()+remaning

# print(mac('macdonald'))




#reverse sentence
#2.
# def rever(st):
#     wordlist= st.split()
#     reverse_word_list=wordlist[::-1]
#     return  ' '.join(reverse_word_list)

# print(rever('I am sejal'))




#3.
# def almost_there(n):
#     return(abs(100-n)<=10) or (abs(200-n)<=10)
    

# print(almost_there(130))
# print(almost_there(200))




############################################
#LEVEL 2:: 

#1. we need [3,3] back to back in list

# def has_33(nums):
#     for i in range(0,len(nums)-1):
#         if nums[i]==3 and nums[i+1]==3:
#             return True
#     return False

# print(has_33([1,2,3,3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

# def has_33(nums):
#         for i in range(0,len(nums)-1):
#              if nums[i:i+2]==[3,3]:
#                  return True
#         return False



#2. every word * 3:
# def mul(text):
#     result=''
#     for char in text:
#         result += char*3
#     return result

# print(mul('hello'))
# print(mul('Sejal, Learn Python'))


#BlackJack:
#Given three integers between 1 and 11, if their sum is 
#   less than or equal to 21, return their sum. If their sum
#    exceeds 21 and there's an eleven, reduce the total sum by 10. 
#     Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def sum(a,b,c):
    if sum([a,b,c])<=21:
        return sum([a,b,c])
    elif [a,b,c] and sum([a,b,c])<=31:
        return sum([a,b,c])-10
    

sum(5,6,7)
