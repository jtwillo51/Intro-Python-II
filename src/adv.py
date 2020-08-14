from room import Room
from player import Player
from item import Item

# Declare all the rooms


hat = Item("hat", "put it on your head to cover your bald spot")
sunglasses = Item("sunglasses", "cover those red eyes")
sword = Item("sword", "kinda pointless, but looks cool")
lamp = Item("lamp", "see in the dark")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons", [sunglasses, hat]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [sword]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'], [lamp])



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    current_room = player.current_room
    
    print(player.current_room.name)

    print(player.current_room.description)

    if current_room.items is not None:
        i = 0
        while i < len(current_room.items):
            item = current_room.items[i]
            print(f"you see {item.name}\n purpose: {item.description}")
            i += 1
    else:
        pass

    user_input = input(
        "Choose a direction to move in ('n', 'e', 's', 'w'):\n (You may also choose to 'take <item name>' or 'drop <item name>')\n")
    uI = user_input.split(' ', 1)

    if len(uI) == 2:
        if uI[0] == "get" or "take":
            for item in current_room.items:
                if item.name == uI[1]:
                    item.on_take()
                    player.items.append(item)
                    current_room.items.remove(item)
                    # add to inventory
                    pass
                else:
                    pass
            else:
                print("item is not in room")
        elif uI[0] == "drop":
            if item in player.items:
                item.on_drop()
                player.items.remove(item)
                current_room.items.append(item)
        else:
            print("invalid input")
    elif uI[0] == "n":
        if current_room.n_to is not None:
            player.currrent_room = current_room.n_to
        else:
            print("You ran into a wall!")
    elif uI[0] == "e":
        if current_room.e_to is not None:
            player.currrent_room = current_room.e_to
        else:
            print("You ran into a wall!")
    elif uI[0] == "s":
        if current_room.s_to is not None:
            player.currrent_room = current_room.s_to
        else:
            print("You ran into a wall!")
    elif uI[0] == "w":
        if current_room.w_to is not None:
            player.currrent_room = current_room.w_to
        else:
            print("You ran into a wall!")
    elif uI[0] == 'q':
        break
    else:
        print("invalid input, try again")
