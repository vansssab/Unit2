print("Welcome to our adventure!")
start = input("Type start to start this adventure. ")
if start == 'start':
    print("Here are the instructions: \n"
    "There are 5 rooms on 3 floors . \n"
    "Each room will wither have a sword, a monster, magic stones, up-stairs, down-stairs, or nothing. \n"
    "You will be going through 3 floors and you can either go down or up the floors. \n"
    "Your goal is to find and defeat the boss monster, but before you do that, you need a sword and magic stones to do this \n"
    "You will use only the sword to defeat the monster in rendom rooms, but it will dissapear after you use it. \n"
    "Good Luck and Have Fun!")

#Map of dungeon
dungeon = [
    ['sword', 'stairs_down', 'empty', 'empty', 'boss_monster'], 
    ['magic_stones', 'monster', 'stairs_up', 'empty', 'stairs_down'], 
    ['empty', 'sword', 'stairs_up', 'monster', 'empty']
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
    
    #player choices
    player_choices = input("What would you like to do? (left, right, up, down, grab, fight) ")
    print(player_choices)
    if player_choices == 'right':
        current_room += 1
        if current_room == 5:
            print("You can't go any further in that direction.")
            current_room -= 1
    elif player_choices == 'left':
        current_room -=1
        if current_room == -1:
            print("You can't go any further in that direction.")
            current_room += 1
    elif player_choices == 'up':
        if location == 'stairs_up':
            current_floor += 1
            if current_floor == 3:
                print("You can not go any higher.")
                current_floor -=1
        else:
            print("You can not got up. There are no stairs leading up.")