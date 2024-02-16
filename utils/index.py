import json

INDEX_FILE = "index.json"


def save_index(index):
    """Сохраняет состояние словаря index в файл"""
    with open(INDEX_FILE, "w") as file:
        json.dump(index, file)


def load_index():
    """Загружает данные из словаря index"""
    try:
        with open(INDEX_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print('Ошибка обновления загрузки данных в индекс')


def first_name_counter(name: str):
    """Функция для определения диапазона в общем списке записей в который входит искомая фамилия"""
    index = load_index()
    couner_befor = 0
    couner_after = index[name[:1]]
    for k in index.keys():
        if k < name[:1]:
            couner_befor += index[k]
        elif k == name[:1]:
            couner_after += couner_befor
    return couner_befor, couner_after


def update_index(first_new_symbol, old_first_symbol, index):
    """Обновляет значения в словере index"""
    index[first_new_symbol] += 1
    index[old_first_symbol] -= 1
    save_index(index)
