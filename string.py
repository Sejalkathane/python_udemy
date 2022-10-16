#try i windows powersheel

# >>> me="Sejalkathane"
# >>> me
# 'Sejalkathane'
# >>> me[4]
# 'l'
# >>> me[3]
# 'a'
# >>> me="Sejalkathane"
# >>> me
# 'Sejalkathane'
# >>> me[4]
# 'l'
# >>> me[3]
# 'a'
# >>> me[-3]
# 'a'
# >>> me[-8]
# 'l'
# >>> me[6:]
# 'athane'
# >>> me[2:
# ... ]
# 'jalkathane'
# >>> me[:5
# ... ]
# 'Sejal'
# >>> me[:-3]
# 'Sejalkath'
# >>> me[-3:]
# 'ane'

me='Sejal kathane'
# select one charecter
print (me[0])
print (me[2])

#for start no. to end
print (me[2:])
print (me[6:])

#from starting upto that no.
print (me[:5])
print(me[:8])

#starting no to ending no
print (me[0:5])
print (me[6:8])
print (me[2:5:7])

print('......................................')

#reverse all avove no.this 
print (me[-3])
print (me[-5:])
print (me[:-7])
print (me[-8:-2])

#double collon ::
print (me[::])  #print full string
print (me[2::6])







