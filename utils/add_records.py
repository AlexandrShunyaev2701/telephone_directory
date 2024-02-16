from typing import Dict
from utils.index import save_index


def add_record(file_name: str, index: Dict) -> None:
    """
    Функция для добовления новой записи в справочник
    """
    print("Введите данные, после ввода нажмите ENTER")
    first_name = input("Фамилия: ")
    index[first_name[:1]] += 1  # Обновляем значение в json по ключу = первой букве фамилии
    last_name = input("Имя: ")
    surname = input("Отчество: ")
    organization = input("Организация: ")
    work_phone = input("Рабочий телефон: ")
    personal_phone = input("Личный телефон: ")
    new_record = {
        "Фамилия": first_name,
        "Имя": last_name,
        "Отчество": surname,
        "Организация": organization,
        "Рабочий телефон": work_phone,
        "Личный телефон": personal_phone,
    }
    with open(file_name, "a") as file:
        file.write("\n" + ";".join(new_record.values()))
        print("Новая запись успешно добавлена.")
    save_index(index)  # Сохраняем изменения в json
