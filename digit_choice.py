#Repeat uptill you not enter number
def user_choice():

    #initial
    choice='Wrong'
    acceptable_range = range(0,10)
    within_range = False

    #Two condotion to check
    #Digit within range==False
    while choice.isdigit()==False or within_range ==False:
        choice = input("Please enter a number(0-10) : ")

             #Digit Check                                             
        if choice.isdigit()==False:
            print("Sorry that is not a digit! ")

            #Range check
        if choice.isdigit()== True:
            if int(choice) in acceptable_range:
                within_range=True
                
            else:
                print("Sorry, you are not of acceptable range(0-10) ")
                within_range ==False
            
                                                            
    return int(choice)


user_choice()