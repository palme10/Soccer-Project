# Women's Soccer Season Game
# Team Members:
# Elijah Palmer
# Adam Cammack
# Name 3

import random


def display_intro():
    """
    Displays the intro/rules, asks for the player's name,
    and returns the name to main.
    """
    print("Welcome to the Women's Soccer Season Game!")
    print("You will choose a home team and an opponent.")
    print("The computer will simulate the game with random scores.")
    print("There are no ties. Each game will end in a win or a loss.")
    print()

    sName = input("Enter your name: ").strip()
    print(f"\nWelcome, {sName}!\n")
    return sName


def display_menu():
    """
    Displays the menu and returns the user's choice.
    """
    print("Menu")
    print("1. Play a game")
    print("2. View team record")
    print("3. Quit")

    sChoice = input("Enter your choice: ").strip()
    return sChoice


def choose_team(teams_list, excluded_team=None):
  
    
    #Displays a menu of teams. If excluded_team is provided, 
    #it filters that team out of the selection process.
    
    # Create a local copy 
    available_teams = [team for team in teams_list if team != excluded_team]

    print("\n--- Select a Team ---")
    for index, team in enumerate(available_teams, start=1):
        print(f"{index}. {team}")

    # Basic input handling
    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(available_teams):
                selected_name = available_teams[choice - 1]
                print(f"Selected: {selected_name}")
                return selected_name
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def play_game(home,opponent):
   
    """4. Generate random scores (no ties) and return W or L for the home team."""
    home_score = 0
    away_score = 0
    
    # Ensure no ties as per instructions
    while home_score == away_score:
        home_score = random.randint(0, 5)
        away_score = random.randint(0, 5)
    
    print(f"\nFINAL SCORE: {home} {home_score} - {away_score} {opponent}")
    
    if home_score > away_score:
        print(f"{home} Wins!")
        return "W"
    else:
        print(f"{home} Loses.")
        return "L"

def display_record(sTeamName, iWins, iLosses):
    """
    Receives the team name and its record, then displays it.
    """
    print()
    print(f"Team Record for {sTeamName}")
    print(f"Wins: {iWins}")
    print(f"Losses: {iLosses}")
    print()

    
def main():
    """
    Main function that controls the game.
    """
    lstTeams = ["BYU","Utah","UVU","Weber State","Utah State","SUU"]
    sPlayerName = display_intro()
    sLastHomeTeam = ""
    iWins = 0
    iLosses = 0

    sChoice = ""

    while sChoice != "3":
        sChoice = display_menu()

        if sChoice == "1":
            print(f"\n{sPlayerName}, let's play a game.")

            sHomeTeam = choose_team(lstTeams)
            sOpponentTeam = choose_team(lstTeams, sHomeTeam)

            sResult = play_game(sHomeTeam, sOpponentTeam)

            sLastHomeTeam = sHomeTeam

            if sResult == "W":
                iWins += 1
            else:
                iLosses += 1

        elif sChoice == "2":
            if sLastHomeTeam == "":
                print("\nNo game has been played yet.\n")
            else:
                display_record(sLastHomeTeam, iWins, iLosses)

        elif sChoice == "3":
            print("\nThanks for playing!")

        else:
            print("\nInvalid choice. Try again.\n")


main()