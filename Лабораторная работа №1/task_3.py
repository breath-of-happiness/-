list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
numbers = len(list_players)    # общее число игроков
middle = numbers // 2    # определение числа участников в каждой команде
team_1 = list_players[:middle]    # команда №1
team_2 = list_players[middle:]    # команда №2
print('Состав команды №1:', team_1)
print('Состав команды №2:', team_2)
