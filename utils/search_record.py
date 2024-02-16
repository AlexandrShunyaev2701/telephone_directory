from utils.display_records import display_record
from utils.index import first_name_counter, load_index
from typing import List


def search_record(records: List) -> None:
    """
    Функция для поиска записей в справочнике по заданной фамилии.

    Аргументы:
    records: Список записей справочника.
    """
    search_field = input("Укажите фамилию (фамилию и имя/ФИО полностью) через пробел для поиска: ")
    print()
    print("Результат:")
    print()
    load_index()
    start_index, end_index = first_name_counter(search_field)
    search_records = records[start_index:end_index]
    found = False  # Флаг, указывающий, были ли найдены записи
    counter = start_index
    for record in search_records:
        record_str = " ".join(record)
        counter += 1
        if search_field in record_str:
            print(f"Запись№{counter}\n{display_record(record)}")
            found = True
    if not found:
        print("Таких записей нет")
