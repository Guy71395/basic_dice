import dice

past_rolls = []

def menu_print():
    print('r -- regular dice roll')
    print('t -- totaled dice roll')
    print('p -- print past rolls')
    print('x -- Exit')

def unrecog_choice():
    print('''
    --Choice not Recognized-- 
            
    --Please try again--
    ''')

def regular_roll():
    try:
        global past_rolls
        side_num = input('Enter number of sides for you dice:\n')
        dice_num = input('Enter number of dice:\n')
        temp_roll = dice.roll(dice_num+"d"+side_num)
        print(temp_roll)
        past_rolls.append(temp_roll)
    except:
        print('error')

def totaled_roll():
    try:
        global past_rolls
        side_num = input('Enter number of sides for you dice:\n')
        dice_num = input('Enter number of dice:\n')
        temp_roll = dice.roll(dice_num+"d"+side_num+"t")
        print(temp_roll)
        past_rolls.append(temp_roll)
    except:
        print('error')

def past_print():
    for roll in past_rolls: print(roll)
        
def main():
    choice = ""

    while choice != "x":
        if choice == "r":
            regular_roll()
        elif choice == "t":
            totaled_roll()
        elif choice == "p":
            past_print()
        elif choice != '':
            unrecog_choice()
        menu_print()
        choice = input("How would you like to continue?:\n")


if __name__ == '__main__':
    main()
