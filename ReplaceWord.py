# Create program that looks through a file and looks for "Michael". Replace all "Michael"'s with "Mike"

word_count = 0
string = input("Insert File Name: ")
search_text = input("Enter word you want replaced: ")
replaced_text = input("Enter word you want to replace it with: ")

with open(string, 'r') as file:
    data = file.read()
    word_count = data.count(search_text)
    data = data.replace(search_text, replaced_text)

with open(input("New File Name: "), 'x') as file:
    file.write(data)

print("Text Replaced " + str(word_count) + " times")




# find_the = stuff.find("the", 0, len(stuff))
#
# with open(string) as openfileobject:
#     for line in openfileobject:
#         find_the = stuff.find("the", 0, len(line))
#         the_count += 1
#         while
#         find_the = stuff.find("the", find_the + 1, len(line))
#         the_count += 1
#
# print(len(stuff))
#
# print(find_the)

# for i in stuff:
#     if i.isspace():
#         space_count += 1
#     elif i.isupper():
#         upper_count += 1
#     else:
#         lower_count += 1
#
#
# print("Space Count: " + str(space_count))
# print("Uppercase Count: " + str(upper_count))
# print("Lowercase Count: " + str(lower_count))