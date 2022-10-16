#Comment : Singleline and multiline
#single line
'''This is multiline Comment'''

#Function
def say_hello():
    print("hello")
    print('are')
    print('you')

say_hello()



def name_fun(name='sk'):  #this is set as default value if we does not provide any input then this print
    print(f'Hello {name}')

name_fun('Sejal')
    


def sum(a,b):
    return (a+b)

re=sum(2,5)
print(re)


#let's se deffrence between return and print in python

def print_result(a,b):
    print(a+b)  # by using print we directly print value

def return_result(c,d):
    return (c+d) #after write return then wefirst assign value then print

print_result(2,4)

r=return_result(3,5)
print(r)


print(type(r))


#dont write number as a string ex:
def s(x,y):
    print(x,y)

print(s('2','3'))  #this is wrong
