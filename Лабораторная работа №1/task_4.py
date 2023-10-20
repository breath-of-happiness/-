users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
# создание словаря с нулевыми значениями ключей
dictionary = {"Общее количество": 0, "Уникальные посещения": 0}
quantity = len(users)    # ключ для общего количества
unique_visitors = len(set(users))    # ключ для уникальных поситителей
# замена ключей словаря, вывод на печать
dictionary["Общее количество"] = quantity
dictionary["Уникальные посещения"] = unique_visitors
print(dictionary)
