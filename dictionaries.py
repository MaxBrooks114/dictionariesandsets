fruit = {"orange": "A sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
print(fruit["lemon"])
fruit["pear"] = "an odd shaped apple"
print(fruit)

fruit["lime"] = "great with tequila"

print(fruit)

del fruit["lemon"]

print(fruit)
#
# fruit.clear()

while True:
    dict_key = input("please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we do not have {}".format(dict_key))



