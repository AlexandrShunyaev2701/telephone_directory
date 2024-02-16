from typing import List


def display_record(record: List) -> str:
    """
    Функция для вывода одной записи справочника
    """
    result = ""
    first_name, last_name, surname, organization, work_phone, personal_phone = record
    result = f"ФИО: {first_name} {last_name} {surname}\n"
    result += f"Организация: {organization}\n"
    result += f"Рабочий телефон: {work_phone}\n"
    result += f"Личный телефон: {personal_phone}\n"
    return result


def display_records(records: List, page: int, records_per_page: int) -> None:
    """
    Функция для вывода страницы записей справочника
    """
    start_index = (page - 1) * records_per_page
    end_index = min(start_index + records_per_page, len(records))

    for i in range(start_index, end_index):
        print(f"Запись {i + 1}:")
        print(display_record(records[i]))
        print()
