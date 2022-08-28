# Create functions

def pickup_item(inventory,Room_items,current_room):
    print('Entering the room, you see there is something on the floor. Pick it up?')
    pickup_command = input()
    if pickup_command == 'yes': 
        inventory.append(Room_items[current_room])
        del Room_items[current_room]
        print('You now have added an item to your inventory.')
    elif pickup_command == 'no':
        print('you leave the item in the floor.')
    else:
        print('You left the item on the floor.')
        
    print(inventory)
    return inventory,Room_items

# Create Dictionary for rooms in game

Room_items = {
    'Family room' : 'Ammo',
    'Library' : 'Iron Sight',
    'Kitchen' : 'Grip',
    'Office' : 'Clip',
    'Living room' : 'Gun frame',
    'Foyer' : 'Burglar',
    'Garage' : 'Muzzle',
}

Rooms = {
    'Bedroom': {"go east" : "Family room"}, 
    'Family room': {'go north': 'Living room', 'go west' : 'Bedroom', "go east": 'Kitchen',  'go south': 'Library'},
    'Library': {'go north': 'Family room', 'go east': 'Office'},
    'Office': {'go west': 'Library'},
    'Living room': {'go south': 'Family room', 'go east': 'Garage'},
    'Garage': {'go west': 'Living room'},
    'Kitchen':  {'go west': 'Family room', 'go north': 'Foyer'},
    'foyer': {'go south': 'Kitchen'},

}

# Starting instructions

print("                       ****Welcome to Protect and Serve!****")
print("A burgler has broken into your home, where you now have to protect yourself! But oh no,")
print('But oh no, you now find yourself having to assemble your weapon! Run around your house')
print('           and find the parts that you need to assemble your weapon!')
print('How to play: Type commands such as "go north, go south, go east, and go west, to travel."')
print('       Type "yes" or "no" to pick up part and store it inside your inventory.')
print()

#Game start 

user_input = input('Enter your character name:')
location = "Bedroom"
inventory = []

#Direction

while True:
    print()
    print('Alright', user_input, 'you are in the', location, '.')
    if location == "Foyer":
        print()
        print('You see the burglar, you lose!!')                                    #losing condition
        break
    elif location in Room_items:												    #finding the item in said room 
        inventory,Room_items = pickup_item(inventory,Room_items,location)
        if len(inventory) == 6:
            print()
            print("You've assembled your gun! You win! Oh wait, it's only your daughter getting home early from that sleepover.") # victory condition
            break
    Direction_possibilities = list(Rooms[location].keys())
    print()
    print("You can go:", *Direction_possibilities)                      #letting player know what directions can be taken
    print()
    user_dir = input("Which direction would you like to go?:").lower()

    if user_dir in Rooms[location].keys():  
        location = Rooms[location][user_dir]                                        #Updating what the player location is by renewing location var

    elif user_dir == 'exit':
        print('Goodbye')
        break
    else:
        print('You cannot go that way!')


