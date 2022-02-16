print("Welcome to our adventure!")
start = input("Type start to start this adventure. ")
if start == 'start':
    print("Here are the instructions: \n"
    "There are 5 rooms on 3 floors . \n"
    "Each room will either have a sword, a monster, magic stones, up-stairs, down-stairs, or nothing. \n"
    "You will be going through 3 floors and you can either go down or up the floors. \n"
    "You can go left, right, up, down, grab, or fight. \n"
    "You can also access you inventory whenever you want.\n"
    "Your goal is to find and defeat the boss monster, but before you do that, you need a sword and magic stones. \n"
    "You will use only the sword to defeat the monster in rendom rooms, but it will dissapear after you use it. \n"
    "Good Luck and Have Fun!")

#Map of dungeon
dungeon = [
    ['sword', 'monster', 'stairs_down', 'boss_monster', 'prize'], 
    ['magic_stones', 'monster', 'stairs_up', 'stairs_down', 'sword'], 
    ['empty', 'sword', 'stairs_up', 'monster', 'sword']
    ]

#player_info
inventory = []
current_room = 0
current_floor = 2
location = dungeon[current_floor][current_room]

#game loop
while True:
    
    #update location
    location = dungeon[current_floor][current_room]

    #describe where at
    if location == 'empty':
        print("The room is empty. Nothing here is attainable.")
    elif location == 'sword':
        print("There is a sword in the room")
    elif location == 'stairs_up':
        print("There are stairs going up.")
    elif location == 'monster':
        print("There is a monster in the room.")
    elif location == 'magic_stones':
        print("There are magic stones in the room.")
    elif location == 'stairs_down':
        print("There are stairs that go down in the room.")
    elif location == 'boss_monster':
        print("You found the boss monster.")
    else:
        ("You made it to the prize!")
    
    #player choices
    player_choices = input("What would you like to do? (left, right, up, down, grab, fight, inventory.) ")
    print(player_choices)
    if player_choices == 'right':
        current_room += 1
        if current_room == 5:
            print("You can't go any further in that direction.")
            current_room = 4
        elif location == 'monster' or location == 'boss_monster':
            print("You cannot go past a monster. Therefore, you have been eaten and died.")
            print("Game Over")
            break
    
    elif player_choices == 'left':
        current_room -=1
        if current_room == -1:
            print("You can't go any further in that direction.")
            current_room = 0
        elif location == 'monster' or location == 'boss_monster':
            print("You cannot go past a monster. Therefore, you have been eaten and died.")
            print("Game Over")
            break
    
    elif player_choices == 'up':
        if location == 'stairs_up':
            current_floor -= 1
            print("You went up the stairs.")
            if current_floor == -1:
                print("You cannot go any higher.")
                current_floor = 0
        else:
            print("There are no stairs here. You cannot go up.")
    
    elif player_choices == 'down':
        if location == 'stairs_down':
            current_floor += 1
            print("You went down the stairs.")
            if current_floor == 3:
                print("You cannot go any lower.")
                current_floor = 2
        else:
            print("There are no stairs here. You cannot go down.")

    elif player_choices == 'grab':
        if len(inventory) < 3:
            if location == 'sword' or location == 'magic_stones':
                inventory.append(location)
                dungeon[current_floor][current_room] = 'empty'
            elif location == 'prize':
                print("You have grabbed the prize. You win!")
                break
            else:
                print("There is nothing to be grabbed here.")
        else:
            print("You cannot put anything else in you inventory.")

    elif player_choices == 'fight':
        if location == 'monster':
            if 'sword' in inventory:
                print("You have slayed the monster, but your sword broke while fighting.")
                inventory.remove('sword')
                dungeon[current_floor][current_room] = 'empty'
            else:
                print("You do not have the necessary items for the battle. The monster has eaten you.")
                print("Game Over.")
                break
        elif location == 'boss_monster':
            if 'sword' in inventory and 'magic_stones' in inventory:
                print("You have slayed the boss monster. ")
                dungeon[current_floor][current_room] = 'empty'
            else:
                print("You do not have the necessary items for the battle. The monster has eaten you.")
                print("Game Over")
                break
        else:
            print("There is nothing to fight.")
    
    elif player_choices == 'inventory':
        print("You have:")
        print(' '.join(inventory))
    
    else:
        print("That is not an option. Try again.")



    