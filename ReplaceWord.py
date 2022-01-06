# ReplaceWord.py replaces a word in the file and saves it in a new file. It aslo let's you know how many times it does it.

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
