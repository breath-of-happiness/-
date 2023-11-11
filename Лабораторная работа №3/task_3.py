def count_letters(text):
    counter = {}
    for symbol in text:
        symbol = symbol.lower()
        if symbol.isalpha():
            if symbol in counter:
                counter[symbol] += 1
            else:
                counter[symbol] = 1
    return counter


def calculate_frequency(counter):
    length = 0
    for value in counter.values():
        length += value
    for key in counter.keys():
        counter[key] = counter[key] / length
    return counter


main_text = """У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

final_dict = calculate_frequency(count_letters(main_text))
for key in final_dict:
    rounded = str(round(final_dict[key], 2))
    if float(rounded) == 0:
        rounded += '0'
    print(key + ": " + rounded)
