from typing import List
from utils.index import update_index
from utils.search_record import search_record


def update_record(file_name: str, records: List, index) -> None:
    """Обновляет запись в справочнике"""
    print("Сначала найдем нужную запись для изменения!")
    search_record(records)
    record_number = int(input("Введите номер записи которую вы хотите изменить: "))
    old_first_symbol = records[record_number - 1][0][:1]
    result_record = []
    for i in records[record_number - 1]:
        print(f"Старое заначение: {i}")
        new_record_field = input("Введите новое значение: ")
        result_record.append(new_record_field)
    records[record_number - 1] = result_record
    new_first_symbol = records[record_number - 1][0][:1]
    with open(file_name, "w") as file:
        for record in records:
            file.write(";".join(record) + "\n")
    if old_first_symbol == new_first_symbol:
        print("Запись успешно обнавлена")
    else:
        update_index(new_first_symbol, old_first_symbol, index)
        print("Запись успешно обнавлена")
