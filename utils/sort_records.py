def sort_phonebook(file_name: str) -> None:
    """
    Функция для сортировки записей в телефонном справочнике по фамилиям.

    filename: str - Имя файла с данными справочника.
    """
    # Чтение всех строк файла в список и удаление символов новой строки
    with open(file_name, "r") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    # Сортировка списка строк (записей) по фамилиям
    sorted_lines = sorted(lines, key=lambda x: x.split(";")[0])

    # Запись отсортированных записей обратно в файл с добавлением символов новой строки
    with open(file_name, "w") as file:
        file.write("\n".join(sorted_lines))
