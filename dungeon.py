import random

name = input("Greetings adventurer. What is your name? ")
player_class = input(f"Ahh, a fine name. Well {name}, it's dangerous to go alone. So tell me your class... Be you warrior, mage, archer, or rogue? ").lower()
if player_class == 'warrior':
    print("Heh, a classic choice. Steel will be your advocate. Take this Iron Sword!")
elif player_class == 'mage':
    print("Ah, a seeker of the arcane! This Willow Staff should channel your power.")
elif player_class == 'archer':
    print("Keen eyes! Here is a Recurve Bow and a quiver of arrows.")
elif player_class == 'rogue':
    print("Silent and deadly. These Twin Daggers will suit you well.")
else:
    print(f"A {player_class}? Never heard of that one. Here, just take this Rusty shovel, you miscreant and good luck...")
