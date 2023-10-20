volume_discrete = 1.44    # объем дискреты в Мб
number_of_pages = 100    # число страниц
number_of_lines = 50    # число строк на одной странице
number_of_characters_per_line = 25    # число символов в строке
symbol_volume = 4    # для хранения одного символа необходимо 4 байта
# переведем информационный объем дискреты в байты
volume_discrete_byte = volume_discrete * 1024 * 1024
# определим занимаемый объем одной книги
size_of_one_book = number_of_pages * number_of_lines * number_of_characters_per_line * symbol_volume
# найдем число книг, которые поместятся на дискрете
number_of_books = volume_discrete_byte // size_of_one_book
print("Количество книг, помещающихся на дискету:", int(number_of_books))
