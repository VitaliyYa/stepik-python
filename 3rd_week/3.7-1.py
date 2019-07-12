"""
Link task: https://stepik.org/lesson/3380/step/1?thread=solutions&unit=963

Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом
матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже. Порядок вывода команд произвольный.

Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2

Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1

"""


def add_games(*teams):
    for team in teams:
        if TEAMS.get(team):
            TEAMS[team]["games"] += 1
        else:
            TEAMS[team] = {"games": 1, "wins": 0, "draws": 0, "defs": 0}


def add_results(team1, score1, team2, score2):
    if int(score1) > int(score2):
        TEAMS[team1]["wins"] += 1
        TEAMS[team2]["defs"] += 1

    elif int(score2) > int(score1):
        TEAMS[team2]["wins"] += 1
        TEAMS[team1]["defs"] += 1

    else:
        TEAMS[team1]["draws"] += 1
        TEAMS[team2]["draws"] += 1


TEAMS = {}

for _ in range(int(input())):
    team1, score1, team2, score2 = input().split(";")
    add_games(team1, team2)
    add_results(team1, score1, team2, score2)

for team in TEAMS:
    print("{}:{} {} {} {} {}".format(
        team, TEAMS[team]["games"], TEAMS[team]["wins"],
        TEAMS[team]["draws"], TEAMS[team]["defs"],
        TEAMS[team]["wins"] * 3 + TEAMS[team]["draws"]
    ))
