def cook_book():
    with open('recipes.txt', 'rt', encoding="utf-8") as file:
        c_book = {}
        for line in file:
            dish = line.strip()
            ingredients_count = int(file.readline())
            structure = []
            for _ in range(ingredients_count):
                ing = file.readline().strip().split(' | ')
                ingredients, quantity, measure = ing
                structure.append({'ingredients': ingredients, 'quantity': quantity, 'measure': measure})
            c_book.update({dish:structure})
            file.readline()
    return c_book

def get_shop_list_by_dishes(dish_list, person_count):
    cb = cook_book()
    shop_list = {}
    for dish in dish_list:
        if dish in cb:
            ing_list = cb.get(dish)
            for x in ing_list:
                ing_list = list(x.values())
                name, measure, quantity = ing_list
                shop_list.update({name:{'measure': ing_list[2], 'quantity': int(ing_list[1])*int(person_count)}})
    return print(shop_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

def read_file(file_name):
    file_list = []
    with open(file_name, 'rt', encoding="utf-8") as file:
        count = int()
        for text in file.readlines():
            count += 1
        file.seek(0)
        data = file.read()
        file_list.append(str(count))
        file_list.append(file_name)
        file_list.append(data)
        # print(file_list)
        return file_list

def new_file():
    files_list = []
    one_file = read_file('files/1.txt')
    two_file = read_file('files/2.txt')
    three_file = read_file('files/3.txt')
    files_list.append(one_file)
    files_list.append(two_file)
    files_list.append(three_file)
    files_list.sort()
    with open('files/all.txt', 'w') as f:
        for count, name, text in files_list:
            f.write(f'{name}\n{count}\n{text}\n')

new_file()