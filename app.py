import constants
import os


def get_string_guardians(list_players_team):
    list_guardian = []
    for p in list_players_team:
        list_guardian += p["guardians"]
    return ", ".join(list_guardian)


def separate_experieced_from_inexperienced(list_players_team):
    ex = []
    no_ex = []
    for p in list_players_team:
        if p["experience"] == True:
            ex.append(p)
        else:
            no_ex.append(p)
    return [len(ex), len(no_ex)]


def average_height(list_players_team):
    list_height = []
    for p in list_players_team:
        list_height.append(p["height"])
    return sum(list_height) / len(list_height)


def start():
    team_size = len(constants.TEAMS)
    cleaned_players = constants.PLAYERS.copy()
    players_ex = []
    players_no_ex = []
    teams = constants.TEAMS.copy()
    new_teams = {}

    for players in cleaned_players:
        if players["experience"] == "YES":
            players["experience"] = True
        elif players["experience"] == "NO":
            players["experience"] = False

        if players["experience"]:
            players_ex.append(players)
        else:
            players_no_ex.append(players)

        guardians = players["guardians"]
        if type(guardians) != list:
            players["guardians"] = guardians.split(" and ")

        height = players["height"]
        if type(height) != int:
            players["height"] = int(height[0:2])

    n = len(players_ex) / team_size
    n_start = n
    for i, team in enumerate(teams, start=1):
        players_list = []
        for x, players in enumerate(players_ex, start=1):
            if x > (n - n_start) and (x <= n):
                players_list.append(players)
        new_teams[team] = players_list
        n += n_start

    n = len(players_no_ex) / team_size
    n_start = n
    for i, team in enumerate(teams, start=1):
        players_list = []
        for x, players in enumerate(players_no_ex, start=1):
            if x > (n - n_start) and (x <= n):
                players_list.append(players)
        new_teams[team] += players_list
        n += n_start

    list_teams = list(new_teams.items())

    print("----MENU----")

    print("Here are your choices: ")
    print(" 1) Display Team Stats ")
    print(" 2) Quit ")

    choice = input("Enter an option > ")

    if choice == '1':
        for i, team in enumerate(list_teams, start=1):
            print("{}) {}".format(i, team[0]))

        choice_team = input("Enter an option > ")
        valid_choise = False
        for i, team in enumerate(list_teams, start=1):
            if str(i) == choice_team:
                valid_choise = True
                list_player = []
                list_player_complete = []
                for elem in team[1]:
                    list_player.append(elem["name"])
                    list_player_complete.append(elem)
                team_stat = "Team: {} stats".format(team[0])
                team_stat_size = len(team_stat)
                print(team_stat)
                print('-' * team_stat_size)
                print("Total players: {}".format(len(list_player)))
                ex_no_ex = separate_experieced_from_inexperienced(list_player_complete)
                print("Experienced players: {}".format(ex_no_ex[0]))
                print("Inexperienced players: {}".format(ex_no_ex[1]))
                print("Average height team: {} \n".format(average_height(list_player_complete)))
                print("Players on Team:")
                team_players = ", ".join(list_player)
                print(" {} \n".format(team_players))
                print("Guardians on Team:")
                print(" {} \n".format(get_string_guardians(list_player_complete)))

        if not valid_choise:
            print("Not a valid option!")

    elif choice == '2':
        print('Thank You, see you soon!')
        exit()
    else:
        print('Choice not allowed! ')

    input("Press ENTER to continue... ")
    os.system('cls' if os.name == 'nt' else 'clear')
    start()


if __name__ == "__main__":
    start()


























