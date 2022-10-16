
print(20%2==0)
print(21%2==0)

#simple function for this or two find even no
def even_check(num):
      return num%2==0

print(even_check(28))
print(even_check(55))


#check even no is present in given list or not

# def check_even_list(num_list):
#     for number in num_list:
#         if number % 2==0:
#             return True
#         else:
#             pass
#     return False

# print(check_even_list([1,3,5]))
# print(check_even_list([2,4,3]))
# print(check_even_list([1,1,1]))


#check present even no. in given list
def check_even_list(num_list):
   even_number=[]
   for number in num_list:
        if number %2==0:
           even_number.append(number)

        else:
              pass

   return even_number

print(check_even_list([1,2,4,5]))
print(check_even_list([23,4,54,78]))



