class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    print("""While travelling along the post-apocalyptic landscape, you find an underground bunker.""")

    # create room 0
    room = Room("""You are in a dark cavern with glowing mushrooms.
It looks almost like the former inhabitants of this bunker were growing them. 
There are rooms to the North, South, and West.""",
                7,
                None,
                1,
                5)
    room_list.append(room)

    # create room 1
    room = Room("""You are in a room with various boxes placed on the floor.
This looks like a living room of sorts.
There are rooms to the North and East.""",
                0,
                2,
                None,
                None)
    room_list.append(room)

    # create room 2
    room = Room("""You are in a room with a large table in the middle.
Various moth-eaten maps are strewn about.
You notice that the nearest parking lot has been circled in ink. 
There are rooms to the North and West.""",
                3,
                None,
                None,
                1)
    room_list.append(room)

    # create room 3
    room = Room("""You are in a room with light streaming in from a trapdoor in the ceiling.
A handmade wooden ladder leans against the stone walls and reaches to the trapdoor.
There are rooms to the South and West.""",
                None,
                None,
                2,
                4)
    room_list.append(room)

    # create room 4
    room = Room("""You are in a room with a collapsed tunnel.
A note is tacked to the stone wall near the rubble.
It says "The zombies found a way to get inside our base. 
Collapsing the entrance was the only way to protect ourselves.
Tomorrow we are escaping for good."
There are rooms to the East and South.""",
                None,
                3,
                5,
                None)
    room_list.append(room)

    # create room 5
    room = Room("""You are in a room that used to be a bedroom.
It seems everything of value was taken with the previous inhabitants.
There are rooms to the North, East, and West.""",
                4,
                0,
                None,
                6)
    room_list.append(room)

    # create room 6
    room = Room("""You are in a room that used to be a bathroom. 
A natural underground pool seems to take up much of the room.
There is a room to the East.""",
                None,
                5,
                None,
                None)
    room_list.append(room)

    # create room 7
    room = Room("""You are in a room that used to store food.
You recognise brands such as Chef Boyardee and Campbell.
There is a room to the South.""",
                None,
                None,
                0,
                None)
    room_list.append(room)

    # main loop
    while not done:
        print(room_list[current_room].description)
        direction = input("Which direction would you like to go? (N, E, S, W)\nOr, would you like to quit? (Q)\n")

        # north
        if direction[0].lower() == "n":
            next_room = room_list[current_room].north

        # east
        elif direction[0].lower() == "e":
            next_room = room_list[current_room].east

        # south
        elif direction[0].lower() == "s":
            next_room = room_list[current_room].south

        # west
        elif direction[0].lower() == "w":
            next_room = room_list[current_room].west

        # quit or continue
        elif direction[0].lower() == "q":
            print("""Are you sure you want to quit?
Yes, I want to quit. (Y)
No, I want to continue. (C)""")
            direction = input("What is your choice?\n")

            if direction[0].lower() == "y":
                done = True

            if direction[0].lower() == "c":
                continue

        # check for invalid directions
        else:
            print("Please pick a valid letter. (N, E, S, W, Q)\n")

            continue

        # check if a room is in the chosen direction
        if next_room == None:
            print("You can't go that way!")
            continue

        # change rooms
        current_room = next_room

    print(room_list)


main()
