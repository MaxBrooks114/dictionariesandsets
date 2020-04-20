# locations = {
#     0: "computer",
#     1: "road",
#     2: "hill",
#     3: "building",
#     4: "valley",
#     5: "forest"
# }

# exits = {0: {'Q':0},
#          1: {'W': 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N":5, "Q": 0},
#          3: {"W": 1, "Q":0},
#          4: {"N":1, "W":2, "Q": 0},
#          5: {"W": 2, "S":1, "Q": 0}}
#
# named_exits = {1: {"2": 2, "3": 3, "5": 5, "4": 4 },
#                2: {"5": 5},
#                3: {"1": 1},
#                4: {"1":1, "2": 2},
#                 5: {"2": 2, "1": 1}}

locations = {
    0:{"desc": "computer", "exits": {}, "named_exits": {}},
    1:{"desc": "road", "exits": {'W': 2, "E": 3, "N": 5, "S": 4, "Q": 0}, "named_exits": {"2": 2, "3": 3, "5": 5, "4": 4 }},
    2:{"desc":  "hill","exits": {"N":5, "Q": 0}, "named_exits": {"5": 5}},
    3:{"desc":  "building","exits": {"W": 1, "Q":0}, "named_exits": {"1": 1}},
    4:{"desc":  "valley","exits": {"N":1, "W":2, "Q": 0}, "named_exits": {"1":1, "2": 2}},
    5:{"desc":  "forest", "exits":{"W": 2, "S":1, "Q": 0}, "named_exits": {"2": 2, "1": 1}}
}

vocab = { "QUIT": "Q", "NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W", "ROAD": "1", "HILL": "2", "BUILDING": "3", "VALLEY": "4", "FOREST": "5"}


loc = 1
while True:
    available_exits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        all_exits = locations[loc]["exits"].copy()
        all_exits.update(locations[loc]["named_exits"])
    direction = input("Available exits are " + available_exits + " ").upper()
    print()

    if len(direction):
        words = direction.split()
        for word in words:
            if word in vocab:
                direction = vocab[word]
                break
        # for word in words:
        #     if word in direction:
        #         direction = words[word]
    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print("you cannot go in that direction")



