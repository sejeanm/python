# Matcher (C) 2023 sejeanm

import csv
import json
import copy
import random

GRID_FILE = 'grid2.csv'

PLAYER_NAME = 'name'
PLAYER_GAMES = 'games'
PLAYER_OPPONENT = 'opponent'
PLAYER_POINTS = 'points'
PLAYER_RESULT = 'result'


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def load(name):
    games=[]
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                players = row[1:]
                print('Players {}'.format(players))
            line_count += 1
            print(row)
            grid_pos = 0
            player = row[0]
            for item in row:
                # print('{},'.format(item), end="")
                if player == players[grid_pos]:
                    grid_pos += 1
                    continue
                if item in ['0', '1']:
                    print('Player {} played against {}'.format(player, players[grid_pos]))
                else:
                    print('Player {} did not played against {}'.format(player, players[grid_pos]))
                grid_pos += 1


            print("")
            #if line_count == 0:
                #    print(f'Column names are: {", ".join(row)}')
                #line_count += 1
                #else:
                #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                #line_count += 1
        print(f'Processed {line_count} lines.')


def played_together(grid, name_1, name_2):
    for player in grid:
        if name_1 == player['name']:
            for games in player['games']:
                if name_2 == games['opponent']:
                    return True
    return False


def get_player_names(grid):
    players_name = []
    for player_record in grid:
        players_name.append(player_record[PLAYER_NAME])
    return players_name


def get_players_with_not_played(grid, player_name):
    players_with_not_played = []
    opponents = get_player_names(grid)
    opponents.remove(player_name)
    for opponent in opponents:
        if not played_together(grid, player_name, opponent):
            players_with_not_played.append(opponent)
    return players_with_not_played


def find_matching(grid):
    games_proposal = []
    selected_players = []
    players = get_player_names(grid)
    random.shuffle(players)
    for player in players:
        opponents = get_players_with_not_played(grid, player)
        random.shuffle(opponents)
        if len(opponents) < 1:
            print('No opponents for {}'.format(player))
            return []
        print('Opponents for player {}: {}'.format(player, opponents))
        added = False
        for opponent in opponents:
            if player not in selected_players and opponent not in selected_players:
                selected_players.append(player)
                selected_players.append(opponent)  # Take first opponent
                games_proposal.append([player, opponent])
                added = True
    print('Debug: selected_players: {}'.format(selected_players))
    return games_proposal


def find_matching_sure(grid, expected_games, iterations=50):
    games = 0
    while expected_games != games and iterations > 0:
        games_proposal = find_matching(grid)
        games = len(games_proposal)
        iterations -= 1
    if iterations == 0:
        print('Error: Could not found expected number of games')
    return games_proposal


def load2(name):

    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        player = {}
        # player_points = 0
        players = []
        line_count = 0
        players_details = []
        for row in csv_reader:
            player_games = []
            if line_count == 0:
                players = row
                print('Players: {}'.format(players))
                line_count += 1
                continue
            print(row)
            grid_pos = 1
            player_name = row[0]

            for item in row[1:]:
                print('{}: '.format(item), end="")
                #if player == players[grid_pos]:
                #    grid_pos += 1
                #    continue
                if item == '0':
                    print('Player {} lost a game with {}'.format(player_name, players[grid_pos]))
                    player_games.append({'opponent': players[grid_pos], 'result': 0})
                elif item == '1':
                    print('Player {} won a game with {}'.format(player_name, players[grid_pos]))
                    player_games.append({'opponent': players[grid_pos], 'result': 1})
                elif item.upper() == 'X':
                    print('', end="")
                else:
                    print('Player {} did not played this game with {}'.format(player_name, players[grid_pos]))
                grid_pos += 1
            player['name'] = player_name
            player['games'] = player_games
            player['points'] = sum(item['result'] for item in player_games)
            players_details.append(copy.copy(player))
            print('Player details: {}', format(player))
            line_count += 1

        print(f'Processed {line_count} lines.')
        print(player_games)
        return players_details

