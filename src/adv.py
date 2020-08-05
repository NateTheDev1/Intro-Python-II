from room import Room
from player import Player
from item import Item
import textwrap
import random


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "outside"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "foyer"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "overlook"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "narrow"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "treasure"),
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

# Food
apple = Item('Apple', 'Red and juicy.')
steak = Item('Steak', 'Cold, but could help.')

# Weapon
sword = Item('Iron Sword', 'It is incredibly shiny.')

# Loot
coin = Item('Gold Coin', 'Preciouss.. so shiny...')
ruby = Item('Ruby', "Is it red because it's a ruby? Or is red from blood...")

items_list = [coin, ruby, sword, apple, steak]


## Initialize items
# room['outside'].items = []
roomList = ['narrow', 'outside', 'foyer', 'overlook', 'treasure']

for i in items_list:
    item_num1 = random.randint(0,len(items_list) - 1)
    item_num2 = random.randint(0,len(items_list) - 1)
    room_num = random.randint(0,len(room) - 1)
    room[roomList[room_num]].items = [items_list[item_num1], items_list[item_num2]]



def getItemList(roomName):
    try:
        for x in room[roomName].items :
            print(f"{x.name} --- {x.description}")

    except AttributeError:
        print('No Items In This Room')

# Make a new player object that is currently in the 'outside' room.

player1 = Player('outside')


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

print(f"Current Room: {room[player1.location].name}")
print(textwrap.TextWrapper(50).fill(f"Description: {room[player1.location].description}\n"))
print('----------------------------------------------\n')
print(f"Items In Room:")
getItemList(player1.location)
print('----------------------------------------------\n')


user = input("[n] Move North   [w] Move West   [s] Move South   [e] Move East   [q] Quit\n \n")


while not user == 'q':
    if user == 'n':
        try:
            player1.location = room[player1.location].n_to.title
            print(f"Current Room: {room[player1.location].name}")
            print(textwrap.TextWrapper(50).fill(f"Description: {room[player1.location].description}\n"))
            print('----------------------------------------------\n')
            print(f"Items In Room:")
            getItemList(player1.location)
            print('----------------------------------------------\n')
            user = input("[n] Move North   [w] Move Left   [s] Move Up   [e] Move Down   [q] Quit\n \n")

        except AttributeError:
            print("Movement not allowed")
            user = input("[n] Move North   [w] Move Left   [s] Move Up   [e] Move Down   [q] Quit\n \n")

    elif user == 's':
        try:
            player1.location = room[player1.location].s_to.title
            print(f"Current Room: {room[player1.location].name}")
            print(textwrap.TextWrapper(50).fill(f"Description: {room[player1.location].description}\n"))
            print('----------------------------------------------\n')
            print(f"Items In Room:")
            getItemList(player1.location)
            print('----------------------------------------------\n')
            user = input("[n] Move North   [w] Move Left   [s] Move Up   [e] Move Down   [q] Quit\n \n")

        except AttributeError:
            print("Movement not allowed")
            user = input("[n] Move North   [w] Move Left   [s] Move Up   [e] Move Down   [q] Quit\n \n")
    elif user == 'w':
        try:
            player1.location = room[player1.location].w_to.title
            print(f"Current Room: {room[player1.location].name}")
            print(textwrap.TextWrapper(50).fill(f"Description: {room[player1.location].description}\n"))
            print('----------------------------------------------\n')
            print(f"Items In Room:")
            getItemList(player1.location)
            print('----------------------------------------------\n')
            user = input("[n] Move North   [w] Move Left   [s] Move Up   [e] Move Down   [q] Quit\n \n")

        except AttributeError:
            print("Movement not allowed")
            user = input("[n] Move North   [w] Move Left   [s] Move Up   [e] Move Down   [q] Quit\n \n")
    elif user == 'e':
        try:
            player1.location = room[player1.location].e_to.title
            print(f"Current Room: {room[player1.location].name}")
            print(textwrap.TextWrapper(50).fill(f"Description: {room[player1.location].description}\n"))
            print('----------------------------------------------\n')
            print(f"Items In Room:")
            getItemList(player1.location)
            print('----------------------------------------------\n')
            user = input("[n] Move North   [w] Move Left   [s] Move Up   [e] Move Down   [q] Quit\n \n")

        except AttributeError:
            print("Movement not allowed")
            user = input("[n] Move North   [w] Move Left   [s] Move Up   [e] Move Down   [q] Quit\n \n")
    else:
        print("Invalid selection. Please try again.")
        user = input("[n] Move North   [w] Move Left   [s] Move Up   [e] Move Down   [q] Quit\n \n")
        
        