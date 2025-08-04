import random
list_words = input("Enter a list of words separated by comma: ").split(',')


word_selected = random.choice(list_words)
print(word_selected)
lives = 6
length = 0
for i in word_selected:
    length += 1
print(length)
new_list = []
for i in word_selected:
    new_list.append('-')
print(new_list)
game_over = False
while not game_over:
    letter = input("Enter a letter: ")

    for i in range(len(word_selected)):
        if word_selected[i]== letter:
            new_list[i] = letter
    if letter not in word_selected:
        lives -= 1
        if lives == 0:
            game_over = True
    if '-' not in new_list:
        game_over = True


print(new_list)
























print(new_list)
































