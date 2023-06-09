import random
import requests
import time
import csv
import os


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}/"
    response = requests.get(url)
    pokemon = response.json()
    return {
        "name": pokemon["name"],
        "id": pokemon["id"],
        "height": pokemon["height"],
        "weight": pokemon["weight"],
        "hp": pokemon["stats"][0]["base_stat"],
        "attack": pokemon["stats"][1]["base_stat"],
        "defense": pokemon["stats"][2]["base_stat"],
    }


def print_stats(pokemon):
    print(f""" 
-------------------------------
id: {pokemon['id']}
height: {pokemon['height']}
weight: {pokemon['weight']}
hp: {pokemon['hp']}
attack: {pokemon['attack']}
defense: {pokemon['defense']}
-------------------------------
    """)


def opponent_stat_choice():
    stat = ["id", "height", "weight", "hp", "attack", "defense"]
    random_stat = random.choice(stat)
    return random_stat


def run():
    my_pokemon = random_pokemon()
    print(f"\nYou were given {my_pokemon['name'].capitalize()}")
    print_stats(my_pokemon)

    while True:
        stick_or_twist = input(f"Would you like to stick or twist? ").lower()

        if stick_or_twist == "twist":
            my_pokemon = random_pokemon()
            print(f"\nYou have decided to twist, you are now given {my_pokemon['name'].capitalize()}")
            print_stats(my_pokemon)
            time.sleep(1)
            stat_choice = opponent_stat_choice()
            print(f"Opponent has decided to play the {stat_choice} stat.")
            time.sleep(1)
            break

        elif stick_or_twist == "stick":
            while True:
                stat_choice = input(f"Which stat do you want to use? ").lower()
                if stat_choice == "id":
                    break
                elif stat_choice == "height":
                    break
                elif stat_choice == "weight":
                    break
                elif stat_choice == "hp":
                    break
                elif stat_choice == "attack":
                    break
                elif stat_choice == "defense":
                    break
                else:
                    print("Invalid choice, pick again.")

            break

        else:
            print("Invalid choice, pick again.")

    opponent_pokemon = random_pokemon()
    print(f"\nThe opponent chose {opponent_pokemon['name'].capitalize()}")
    print_stats(opponent_pokemon)

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        print(f"You won this round! {my_pokemon['name'].capitalize()} beats {opponent_pokemon['name'].capitalize()} with {stat_choice}, {my_stat} to {opponent_stat}!")
        return "You"

    elif my_stat < opponent_stat:
        print(f"You lost this round! {opponent_pokemon['name'].capitalize()} beats {my_pokemon['name'].capitalize()} with {stat_choice}, {opponent_stat} to {my_stat}!")
        return "Opponent"

    else:
        print("It's a draw!")
        return "Draw"


def one_game():
    my_score = 0
    opponent_score = 0
    tied_games = 0
    player_name = input("Enter player name: ")
    number_of_games = int(input("How many rounds would you like to play? "))

    for i in range(number_of_games):
        time.sleep(3)
        if i == number_of_games - 1:
            print('\n\n##### Final Round! #####')
        else:
            print(f"\n\n##### Round {i + 1} #####")

        result = run()

        if result == "You":
            my_score += 1
        elif result == "Opponent":
            opponent_score += 1
        elif result == "Draw":
            tied_games += 1

    if my_score > opponent_score:
        print(f"\nCongratulations {player_name}, you win! Final score {my_score}:{opponent_score}")
    elif opponent_score > my_score:
        print(f"\nUnlucky {player_name}, you lost! Better luck next time! Final score {my_score}:{opponent_score}")
    else:
        print(f"\nIt's a draw, so close! Final score {my_score}:{opponent_score}")

    field_names = ["player name", "games played", "my score", "opponent score", "tied games", "my win percentage"]
    data = [
        {"player name": player_name,
         "games played": number_of_games,
         "my score": my_score,
         "opponent score": opponent_score,
         "tied games": tied_games,
         "my win percentage": round((my_score+(0.5*tied_games))/number_of_games*100, 2)},
    ]

    with open("top trump results.csv", "a", newline="") as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
        if os.stat("top trump results.csv").st_size == 0:
            spreadsheet.writeheader()
            spreadsheet.writerows(data)
        else:
            spreadsheet.writerows(data)


def play_game():
    one_game()
    play_again = input("\nDo you want to play again? y/n ").lower()
    while play_again == "y":
        time.sleep(2)
        play_game()
    else:
        time.sleep(2)
        print("\nGame has ended.")


play_game()
