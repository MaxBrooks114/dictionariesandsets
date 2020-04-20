locations = {
    0: "computer",
    1: "road",
    2: "hill",
    3: "building",
    4: "valley",
    5: "forest"
}

exits= [{'Q':0},
        {'W': 2, "E": 3, "N": 5, "S": 4, "Q": 0},
        {"N":5, "Q": 0},
        {"W": 1, "Q":0},
        {"N":1, "W":2, "Q": 0},
        {"W": 2, "S":1, "Q": 0}]

loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    direction = input("Available exits are " + available_exits + " ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("you cannot go in that direction")



