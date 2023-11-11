def find_item(items_list, finding_item):
    if finding_item not in items_list: return None
    return items_list.index(finding_item)


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for finding_item in ['банан', 'груша', 'персик']:
    index_item = find_item(items_list, finding_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{finding_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{finding_item}' не найден в списке.")