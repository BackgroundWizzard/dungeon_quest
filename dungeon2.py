import random

def main():

    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Orion
            {'name': 'Orion', 'health': 10, 'inventory': []}
        """
        name = input("Greetings adventurer. What is your name? ")
        player_class = input(f"Ahh, a fine name. Well {name}, it's dangerous to go alone. So tell me your class... Be you warrior, mage, archer, or rogue? ").lower()

        if player_class == 'warrior':
            print("Heh, a classic choice. Steel will be your advocate. Take this Iron Sword!")
            starting_weapon = "Iron Sword"
        elif player_class == 'mage':
            print("Ah, a seeker of the arcane! This Willow Staff should channel your power.")
            starting_weapon = "Willow Staff"
        elif player_class == 'archer':
            print("Keen eyes! Here is a Recurve Bow and a quiver of arrows.")
            starting_weapon = "Recurve Bow"
        elif player_class == 'rogue':
            print("Silent and deadly. These Twin Daggers will suit you well.")
            starting_weapon = "Twin Daggers"
        else:
            print(f"A {player_class}? Never heard of that one. Here, just take this Rusty Shovel, you miscreant and good luck...")
            starting_weapon = "Rusty Shovel"

        player = {
            "name": name,
            "health": 10,
            "inventory": [starting_weapon]
        }

        return player


    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        treasures = {
            "gold coin": 5,
            "ruby": 10,
            "ancient scroll": 7,
            "emerald": 9,
            "silver ring": 4,
            "dragon scale": 12,
            "enchanted amulet": 8
        }

        return treasures


    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        print("You are in room " + str(room_number) + ".")
        print("What would you like to do?")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")


    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        outcome = random.choice(["treasure", "trap"])

        if outcome == "treasure":
            treasure_list = list(treasures.keys())
            found = random.choice(treasure_list)
            player["inventory"].append(found)
            print("You found a " + found + "!")
        else:
            player["health"] = player["health"] - 2
            print("It's a trap! You lost 2 health.")
            print("Health remaining: " + str(player["health"]))


    def check_status(player):
        """
        Displays the player's current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        print("Health: " + str(player["health"]))

        if len(player["inventory"]) > 0:
            print("Inventory: " + ", ".join(player["inventory"]))
        else:
            print("Inventory: You have no items yet.")


    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player's final health, inventory contents, and total score value.
        """
        total = 0
        for item in player["inventory"]:
            if item in treasures:
                total = total + treasures[item]

        print("Game Over!")
        print("Final health: " + str(player["health"]))

        if len(player["inventory"]) > 0:
            print("Items collected: " + ", ".join(player["inventory"]))
        else:
            print("Items collected: none")

        print("Total treasure value: " + str(total))
        print("Thanks for playing!")


    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        for room_number in range(1, 6):
            in_room = True

            while in_room:
                display_options(room_number)
                choice = input("Enter your choice: ")

                if choice == "1":
                    search_room(player, treasures)
                    if player["health"] < 1:
                        print("You have died. Game over.")
                        end_game(player, treasures)
                        return
                elif choice == "2":
                    print("Moving to the next room...")
                    in_room = False
                elif choice == "3":
                    check_status(player)
                elif choice == "4":
                    print("You quit the game.")
                    end_game(player, treasures)
                    return
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")

        end_game(player, treasures)


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()