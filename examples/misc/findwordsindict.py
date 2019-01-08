import random

words = {'iced': 'dice', 'cat': 'act'}
curr_word = random.choice(list(words.keys()))

print(curr_word)
print(words['iced'])
print(words['cat'])
print(f"The anagram for cat is: {words['cat']}")
print(f"The anagram for iced is: {words['iced']}")
print(f"The anagram for {curr_word} is: {words[curr_word]}")