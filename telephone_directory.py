from utils.sort_records import sort_phonebook
from utils.index import load_index
from utils.display_records import display_records
from utils.add_records import add_record
from utils.search_record import search_record
from utils.update_record import update_record
from utils.clear_screen import clear_screen
from math import ceil

TELEPHONE_DIRECTORY = "telephone_directory.txt"
index = load_index()


def telephone_directory() -> None:
    """
    Основная функция программы
    Позволяет реализовать 4 операции: Вывод постранично записей справочника на экран, добовление новой записи, изменение записи и поиск.
    """
    while True:
        clear_screen()
        print("Телефонный справочник")
        print("1. Показать справочник")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выйти")
        print()
        choice = input('Выберите действие:')

        if choice == "1":
            clear_screen()
            with open(TELEPHONE_DIRECTORY, "r") as file:
                records = [line.strip().split(";") for line in file.readlines()]
            if records:
                page = 1
                records_per_page = 5
                while True:
                    clear_screen()
                    display_records(records, page, records_per_page)
                    if len(records) > records_per_page:
                        print(f"Всего записей:, {len(records)}/ Всего страниц: {ceil(len(records)/records_per_page)}")
                        print(f"Текущая страница: {page}")
                        print("n. Следующая страница")
                        print("p. Предыдущая страница")
                    print("b. Вернуться в главное меню")
                    option = input("Выберите действие: ")
                    if option == "n" and len(records) > (page * records_per_page):
                        page += 1
                    elif option == "p" and page > 1:
                        page -= 1
                    elif option == "b":
                        break
            else:
                print("Справочник пуст.")

        elif choice == "2":
            clear_screen()
            add_record(TELEPHONE_DIRECTORY, index)
            sort_phonebook(TELEPHONE_DIRECTORY)
            input("Нажмите Enter для продолжения...")

        elif choice == "3":
            clear_screen()
            with open(TELEPHONE_DIRECTORY, "r") as file:
                records = [line.strip().split(";") for line in file.readlines()]
            update_record(TELEPHONE_DIRECTORY, records, index)
            sort_phonebook(TELEPHONE_DIRECTORY)
            input("Нажмите Enter для продолжения...")

        elif choice == "4":
            clear_screen()
            with open(TELEPHONE_DIRECTORY, "r") as file:
                records = [line.strip().split(";") for line in file.readlines()]
            search_record(records)
            input("Нажмите Enter для продолжения...")

        elif choice == "5":
            break
        else:
            print("Неккоректный ввод, выберете существующий пункт меню")


if __name__ == "__main__":
    telephone_directory()
