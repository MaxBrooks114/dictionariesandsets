fruit = {"orange": "A sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
#
# fruit["lime"] = "great with tequila"
#
# print(fruit)
#
# del fruit["lemon"]
#
# print(fruit)
#
# fruit.clear()

# while True:
#     dict_key = input("please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "we do not have " + dict_key)
#     print(description)
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("we do not have {}".format(dict_key))
#
# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)
#
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + " is " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " is " + fruit[f])
# for f in fruit:
#     print(f + " is " + fruit[f])

print(fruit.keys())

print(fruit.values())

f_tuple = tuple(fruit.items())

for snack in f_tuple:
    item, description = snack
    print(item, description)