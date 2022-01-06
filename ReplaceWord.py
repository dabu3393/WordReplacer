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
