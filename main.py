from pyllist import sllist
from collections import deque
import json
import random
import sys
import os
import time

# isvedami visi lentos duomenys (testavimui)
def display_linked_list(linked_list):
    current_node = linked_list.first
    while current_node is not None:
        print(current_node.value, end=" -> ")
        current_node = current_node.next 
    print()
#display_linked_list(linked_list)

def display_linked_list_with_positions(linked_list):
    current_node = linked_list.first
    position = 1
    print("\n~~~ Board Plots ~~~")
    while current_node is not None:
        print(f"{position}. {current_node.value['name']}")
        current_node = current_node.next
        position += 1

def add_a_plot(linked_list):
    display_linked_list_with_positions(linked_list)
    while True:
        print("\n~~~ Pick the type of plot you want to add ~~~")
        print("1. ghost")
        print("2. hunt")
        print("3. angel")
        print("4. gamble")
        choice = input("Choose an option (1-4): ").strip()
        plot = {
                'name': "",
                'type': "",
                'owner': "",
                'bonus': 0,
                'bondCost': 0,
                'visitCost': 0,
                'description': "",
                'hidingSpots': [],
                'cards': []
            }
        if choice == '1':
            while True:
                plot['name'] = input("Enter the name of the new plot (unique): ").strip()
                if any(node['name'] == plot['name'] for node in linked_list):
                    print("This name already exists. Please enter a unique name.")
                else:
                    break
            plot['type'] = "ghost"
            plot['bondCost'] = int(input("Input bond cost (number): "))
            plot['visitCost'] = int(input("Input visit cost (number): "))
            plot['description'] = input("Write a description about the ghost: ")
            break

        elif choice == '2':
            while True:
                plot['name'] = input("Enter the name of the new plot (unique): ").strip()
                if any(node['name'] == plot['name'] for node in linked_list):
                    print("This name already exists. Please enter a unique name.")
                else:
                    break
            plot['type'] = "hunt"
            plot['description'] = input("Write a description about the hunt: ")
            print("Enter hiding spots. Type 'done' when finished.")
            while True:
                hiding_spot = input("Enter a hiding spot: ").strip()
                if hiding_spot.lower() == 'done':
                    break
                plot['hidingSpots'].append(hiding_spot)
            break
            
        elif choice == '3':
            plot['name'] = "Angel Protection"
            plot['type'] = "angel"
            plot['bonus'] = int(input("Input bonus amount (number): "))
            plot['description'] = input("Write a description about the angel: ")
            break

        elif choice == '4':
            plot['name'] = "Tarot Cards"
            plot['type'] = "gamble"
            plot['description'] = input("Write a description about tarot cards: ")
            plot['cards'] = ["The Fool", "The Sun", "The Moon", "The Tower", "The Devil", "Death", "The High Priestess"]
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    while True:
        try:
            position = int(input("Enter the position to insert the new plot: ").strip())
            if 1 <= position <= linked_list.size + 1:
                break
            else:
                print(f"Invalid position. Enter a number between 1 and {linked_list.size + 1}.")
        except ValueError:
                print("Invalid input. Please enter a number.")

    if position == 1:
        linked_list.insert(plot, linked_list.first)
    else:
        current = linked_list.first
        for _ in range(position - 2):
            current = current.next
        linked_list.insert(plot, current.next)
    #display_linked_list(linked_list)
    print(f"New plot '{plot['name']}' added at position {position}.")
    print()
    display_linked_list_with_positions(linked_list)

def delete_a_plot_by_position(linked_list):
    display_linked_list_with_positions(linked_list)
    try:
        position = int(input("Enter the position of the plot to delete: ").strip())
        if not (1 <= position <= linked_list.size):
            print(f"Invalid position. Please enter a number between 1 and {linked_list.size}.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if position == 1:
        linked_list.popleft()
        print(f"Plot at position {position} deleted.")
        display_linked_list_with_positions(linked_list)
        return
    current = linked_list.first
    for _ in range(position - 2):
        current = current.next
    linked_list.remove(current.next)
    print(f"Plot at position {position} deleted.")
    display_linked_list_with_positions(linked_list)

def delete_a_plot_by_name(linked_list):
    display_linked_list_with_positions(linked_list)
    plot_name = input("Enter the name of the plot to delete: ").strip()
    current_node = linked_list.first
    position = 1
    found = False
    while current_node is not None:
        if current_node.value['name'] == plot_name:
            found = True
            print(f"\nPlot found at position {position}: {current_node.value['name']}")
            choice = input("Do you want to delete this plot? (yes/no): ").strip().lower()
            if choice == 'yes':
                linked_list.remove(current_node)
                print(f"Plot '{plot_name}' at position {position} has been deleted.")
                display_linked_list_with_positions(linked_list)
                return
        current_node = current_node.next
        position += 1
    if not found:
        print(f"No plot found with the name '{plot_name}'.")
    else:
        print(f"No other plot named '{plot_name}' was deleted.")
    display_linked_list_with_positions(linked_list)

def edit_board(linked_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("\n~~~ Edit Board ~~~")
        print("1. View all plots")
        print("2. Add a plot")
        print("3. Delete a plot by position")
        print("4. Delete a plot by name")
        print("5. Return to main menu")
        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            display_linked_list_with_positions(linked_list)
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            add_a_plot(linked_list)
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            delete_a_plot_by_position(linked_list) 
        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            delete_a_plot_by_name(linked_list)
        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def board_menu(linked_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("\n👻👻👻 Spooky Monopoly 👻👻👻")
        print("1. Start the game")
        print("2. Edit the board")
        print("3. Exit the game")
        choice = input("Choose an option (1-3): ").strip()
        if choice == '1':
            break
        elif choice == '2':
            edit_board(linked_list)
        elif choice == '3':
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# nustatomas zaideju kiekis ir "sanity" kiekis
def get_number_of_players():
    while True:
        try:
            players = int(input("Choose the number of players (2 or 3): "))
            if players in (2, 3):
                return players
            else:
                print("Invalid input. Please enter 2 or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (2 or 3).")

# zaidejams priskiriami vardai, starto pozicija, sanity kiekis, jie yra deke
class Player:
    def __init__(self, name, position, sanity):
        self.name = name
        self.position = position
        self.sanity = sanity
        self.skip_turn = False

def display_status(all_players, active_players):
    active_names = {player.name for player in active_players}
    for player in all_players:
        if player.name not in active_names:
            print(f"{player.name} is out of the game! 💀")
        else:
            print(f"{player.name} is on the position '{player.position.value['name']}' with {player.sanity} sanity.")
    print()

# zaideju ejimu implementacija su deko metodu, kuris pirma elementa deda i gala (po atlikto ejimo)
def take_turns(players):
    all_players = list(players) # kopijuoja zaideju sarasa (zaideju statusui rodyti)
    while True:
        for _ in range(len(players)):  # Loop'ina per kiekviena zaideja deke
            current_player = players[0]  # dabartinis zaidejas yra pirmas deke/eileje

            os.system('cls' if os.name == 'nt' else 'clear')
            display_status(all_players, players) # visu zaideju pozicija, sanity ir busena rodoma kiekvieno ejimo metu

            # Kortos 'The Fool' efektas - praleidzia ejima
            if current_player.skip_turn:
                print(f"{current_player.name} skips this turn due to the 'The Fool' card's effect.")
                current_player.skip_turn = False
                players.rotate(-1)
                continue

            print(f"{current_player.name}'s turn.")
            print(f"{current_player.name} is at position '{current_player.position.value['name']}' with {current_player.sanity} sanity.")
            

            # kauliuko metimas su random modulio implementacija
            input("Press Enter to roll the dice...")
            def roll_dice():
                # random.randint(a, b) funkcija generuoja atsitiktinį skaičių, įskaitant abu galus (t. y. 1 ir 6)
                return random.randint(1, 6)
            result = roll_dice()
            print(f"You rolled a {result}.")

            # judama per tiek laukeliu, koks iskrito kauliuko skaicius, jei pasiekiamas saraso galas, pradedama nuo pradzios
            for _ in range(result):
                if current_player.position.next is not None:
                    current_player.position = current_player.position.next
                else:
                    current_player.position = linked_list.first # judejimo cikliskumas

            print(f"{current_player.name} is at position '{current_player.position.value['name']}' with {current_player.sanity} sanity.")
            
            playerLost = False
            
            
            # ghost laukelis
            if current_player.position.value['type'] == "ghost":
                if current_player.position.value['owner'] == "":
                    if current_player.sanity > current_player.position.value['bondCost']:
                        if input(f"Press Enter if you want to make a contract with '{current_player.position.value['name']}' for {current_player.position.value['bondCost']} sanity or type 'no' to skip this action: ").strip().lower() == 'no': # lower() No nO NO -> no
                            print("The contract was not formed.")
                        else:
                            current_player.sanity -= current_player.position.value['bondCost']
                            current_player.position.value['owner'] = current_player.name
                            print(f"The contract was formed between {current_player.name} and {current_player.position.value['name']}, now the {current_player.position.value['name']} will hunt other players.")
                    else:
                        print(f"Player {current_player.name} does not have enough sanity to form a bond worth {current_player.position.value['bondCost']} sanity.")
                else:
                    print(f"'{current_player.position.value['name']}' is already friends with player {current_player.position.value['owner']}.")
                    if current_player.name == current_player.position.value['owner']:
                        print(f"{current_player.name} has formed the bond with '{current_player.position.value['name']}' already, so {current_player.name} does not lose sanity.")
                    else:
                        print(f"{current_player.position.value['description']}")
                        if current_player.sanity > current_player.position.value['visitCost']:
                            current_player.sanity -= current_player.position.value['visitCost']
                        else:
                            print(f"{current_player.name} died from insanity 💀 💀 💀 💀 💀 💀 💀 💀.")
                            playerLost = True

            # hunt laukelis
            if current_player.position.value['type'] == "hunt":
                print(f"{current_player.position.value['description']}")
                hiding_spots = current_player.position.value['hidingSpots']
                for i, spot in enumerate(hiding_spots, start=1):
                    print(f"{i}. {spot}")
                while True:
                    try:
                        choice = int(input("Enter the number of the hiding spot: "))
                        if 1 <= choice <= len(hiding_spots):
                            chosen_spot = hiding_spots[choice - 1]
                            print(f"Your hiding spot is {chosen_spot}.")
                            break
                        else:
                            print("Wrong choice, choose a number from the list.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                ghost_choice = random.choice(hiding_spots)
                print(f"The {current_player.position.value['name']} checks the {ghost_choice}👻👻👻")
                if ghost_choice == chosen_spot:
                    print(f"The {current_player.position.value['name']} finds player {current_player.name}! {current_player.name} dies! 💀 💀 💀 💀 💀 💀 💀 💀")
                    playerLost = True
                else:
                    print(f"{current_player.name} is safe! The ghost could not locate the player.")

            # angel laukelis
            if current_player.position.value['type'] == "angel":
                print(f"{current_player.position.value['description']}")
                current_player.sanity += current_player.position.value['bonus'] # kodel neprisideda?

            # gamble laukelis
            if current_player.position.value['type'] == "gamble":
                input("Press Enter to draw a card...")
                random_card = random.choice(current_player.position.value['cards'])
                print(f"You drew {random_card}.")
                if random_card == "The Fool":
                    current_player.skip_turn = True
                    print(f"{current_player.name} will skip the next turn due to 'The Fool' card.")
                elif random_card == "The Sun":
                    current_player.sanity += 30
                    print(f"'{random_card}' increases sanity by 30. New sanity: {current_player.sanity}.")
                elif random_card == "The Moon":
                    current_player.sanity -= 30
                    print(f"'{random_card}' decreases sanity by 30. New sanity: {current_player.sanity}.")
                elif random_card == "The Tower":
                    current_player.sanity += 15
                    print(f"'{random_card}' increases sanity by 15. New sanity: {current_player.sanity}.")
                elif random_card == "The Devil":
                    current_player.sanity -= 15
                    print(f"'{random_card}' decreases sanity by 15. New sanity: {current_player.sanity}.")
                elif random_card == "Death":
                    print(f"{current_player.name} drew 'Death' and died 💀.")
                    playerLost = True
                elif random_card == "The High Priestess":
                    current_player.sanity += 100
                    print(f"'{random_card}' increases sanity by 100. New sanity: {current_player.sanity}.")


            if playerLost == False or current_player.sanity < 1:
                print(f"{current_player.name} is at position '{current_player.position.value['name']}' with {current_player.sanity} sanity.")
                #display_linked_list(linked_list)
                # kairiausia elementa deke (pirma elementa) ideda i desiniausia puse (eiles gala)
                players.rotate(-1)
            else:
                players.popleft()  
                
            if len(players) == 1:
                print(f"\n{players[0].name} is the winner! 😈")
                time.sleep(5)
                return
            if input("\nType 'e' to end the game or press Enter to continue: ").strip().lower() == 'e':
                print("Game ended.")
                time.sleep(5)
                return 

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('board.json', 'r') as file:
        data = json.load(file)
    linked_list = sllist()
    for item in data['board']:
        linked_list.append(item)

    board_menu(linked_list)

    num_players = get_number_of_players()
    amount_sanity = int(input("Enter sanity amount for this game (recommended: 100): "))
    print(f"Starting game with {num_players} players. Each player has {amount_sanity} sanity.")

    players = deque()
    for i in range(num_players):
        player_name = input(f"Enter player {i+1} name: ")
        player = Player(name=player_name, position=linked_list.first, sanity=amount_sanity)
        players.append(player)
    
    take_turns(players)
