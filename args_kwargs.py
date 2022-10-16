#*args is followed by tuple and

#for ex: if we want to add no. in tuple which is more than your provided variable than use *args
#this * is only use for tuple 
def fun(*args):
    print( sum(args))
    
fun(221,62,34,4,54,4,5,34,87)

print('........................')

def myfun(*h):  #import is * varible you use any
    for item in h:
        print(item)

myfun(1,2,3,4,5)

    



#**kwargs followed by distionary
#for ex: if we want to add 

def my(**kwargs):
    if 'fruit' in kwargs:
        print('MY fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit hear ')

my(fruit='apple',vegis='potato',soap='kiwe')

    

    # * and ** both

def both(*args,**kwargs):
    print('I world like {} {}'.format(args[0],kwargs['food']))

both(1,2,345,fruit ='Orange',food='egg',animal='dog')