#π’π’π’π’π’
#problems on NUMBERS :ππ²π
# from cmath import sqrt

#Write an equtation that use multiplicaation , division, an exponent, addition, and subtraction that is equal to 100.25.

print((((50*2*2)/2)+.3)-.05)   # πgives 100.25

#solve first without code then check answer
#ans= 44,29,34 lets checkπout ,  π€©its, correct
print(4*(6+5))
print(4*6+5)
print(4+6*5)

#find type of result (3+1.5+4) of course float π lets see
# print(type(3+1.5+4))  #i am correctπ

#What would you use to find a number's square root as well as its square π€?
# print(" Square root of given number is : ",sqrt(4)) #squart method we need to use (from cmath import sqrt)
print("Square root of given number is :",4**0.5)
print("Square of given number is : ",(4*4))


#πππβ­
#PROBLEMS ON STRING: π€ͺπ€
#String 'hello' give a index comment that return 'e'::
s='hello'
print(s[1])  #we get e π§

# reverse the string 'hello' π§ using slicing
print(s[::-1])

# Give the two methods to print letter o from hello πΎ
print(s[4]) 
print(s[-1])



##π°π  PROBLEMS ON LISTS
#build this list [0,0,0] two seprate ways
mylist=[0,0,0]
print([0,0,0])
print(mylist)

list3=[1,2,[3,4,'hello']]
#π ---> π
list3[2][2]='goodby'
print(list3)

#sort the list
list4 =[5,3,4,6,1]
print(list4.sort())
print(list4)




#PROBLEMS BASED ON DICTONARIES ππππ  π€©π Nice question fully enjoyable
#using keys and indexing , grab the 'hello from the following dictionaries:
d={'simple_key':'hello'}
print(d['simple_key'])

d1={'k1':{'k2':'hello'}}
print(d1['k1']['k2'])

d2={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d2['k1'][0]['nest_key'][1][0])

d3={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d3['k1'][2]['k2'][1]['tough'][2][0])




#TUPLES PROBLEM
#How do you create tuple example π
#main difference between tuple and list is 
#    tuple are immuatable(not changable) and list is mutuable(changable)
mytuple=(1,2,3,4)
print(mytuple)



#SETS PROBLEM :: set does not repeat there number example is given below
list5=[1,2,2,33,4,5,11,22,3,3,2]
print(set(list5))



#BOOLEANS SIMPLE PROBLEMS
a=2
b=3
print("value of a!=b is : ",a!=b)
print("value of a==b is : ",a==b)
print("value of a>b is : ",a>b)
print("value of a<b is : ",a<b)
print("value of a<=b is : ",a<=b)
print("value of a>=b is : ",a>=b)



#PROBLEm, BASED OF LIST ,DISTIONARY AND BOOLEAN 
l_one=[1,2,[3,4]]
l_two=[1,2,{'k1':4}]

print("l_one[2][0] >= l_two[2]['k1'] answer is : ",l_one[2][0] >= l_two[2]['k1'])