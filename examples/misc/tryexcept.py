first_card = -1
second_card = -1

while first_card < 0 or first_card > 15:
    try:
        first_card = int(input("Pick a number for a card that is unpicked"))
    except:
        print("You need to provide a number")

while second_card < 0 or second_card > 15:
    try:
        second_card = int(input("Pick a number"))
    except:
        print("You need to provide a number")

print(first_card, second_card)