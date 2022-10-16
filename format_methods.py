# formating with format() method
#first type
print('hi {}'.format('sejal')) 
print ('hi {0} ,how are you {1}'.format('sejal','gitanjali'))
print ('hi {s} ,how are you {g}'.format(s='sejal',g='gitanjali'))

result=100/33
print ("the result is {r} ".format(r=result))

#float formatting follows "{value:width.precision f}"
print ("the result is {r:1.3f} ".format(r=result))

#second type
name="Sejal"
print(f'Hello ,{name}')
print(f'how are you {name} ?')