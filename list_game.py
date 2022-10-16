game_list =[0,1,2]

def display_game(game_list):
    print("Heare is the current list : ")
    print(game_list) 

display_game(game_list)


def position_choice():

    choice='wrong'

    while choice not in ['0','1','2']:
        choice = input("pick a position (0,1,2) : ")

        if choice not in ['0','1','2']:
            print("sorry,invalid choice!")

    return int(choice)
    
position_choice()


def replacement_choice(game_list,position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    print(game_list)

replacement_choice(game_list,1)


def gaemon_choice():

    choice='wrong'

    while choice not in ['y','n']:
        choice = input("Keep playing ? (y or n) ")

        if choice not in ['y','n']:
            print("sorry, i dont understand, please choose y or n")
    
        if choice=='y':
           return True
        else:
           return False

gaemon_choice()




