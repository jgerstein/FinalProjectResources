active_character = ''

class Character:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

beth = Character("Beth Parillo")
justine = Character("Justine Williams")
adrian = Character("Adrian Rocha")

choice = input("Pick beth, justine, or adrian")

if choice == 'beth':
    active_character = beth
if choice == 'justine':
    active_character = justine
if choice == 'adrian':
    active_character = adrian

print(active_character.name)
