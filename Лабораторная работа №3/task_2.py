def find_common_participants(list_one, list_two, sep = ","):
    list_one = list_one.split(sep)
    list_two = list_two.split(sep)
    common_words = list(set(list_one).intersection(list_two))
    common_words.sort()
    return common_words


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
sep = "|"

print(find_common_participants(participants_first_group, participants_second_group, sep))
