# farm_animals = {"sheep", "cow", "hen"}
#
# for animal in farm_animals:
#     print(animal)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)


sample_text = input("Enter a sentence: ").casefold()
text_set = set(sample_text)

vowels = {"a", "e", "i", "o", "u"}

print(list(sorted(text_set.difference(vowels))))

