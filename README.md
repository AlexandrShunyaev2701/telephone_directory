Этот проект телефонного справочника реализует следующий функционал:
   1. Вывод записей из справочника на экран постранично.
   2. Добавление новых записей в справочник.
   3. Редактирование существующих записей в справочнике.
   4. Поиск записей по одной или нескольким характеристикам.

Интерфейс реализован через консоль, а данные хранятся в текстовом файле telephone_directory.txt. В справочнике содержится информация о фамилии, имени, отчестве, названии организации, рабочем и личном телефоне.
Основная функция telephone_directory() в файле telephone_directory.py запускает работу справочника.
В каталоге utils находятся следующие файлы:
   1. clear_screen.py содержит функцию clear_screen(), которая очищает экран консоли, работая как в Windows, так и в Linux.
   2. display_records.py содержит функции display_record() и display_records(), которые выводят информацию об одной записи и все записи справочника соответственно.
   3. sort_records.py содержит функцию sort_phonebook(), которая сортирует записи справочника по алфавиту (по фамилиям) для удобства восприятия и оптимизации поиска.
   4. index.py содержит функции для оптимизации и ускорения поиска, добавления и редактирования записей. Файл index.json хранит словарь, где ключи - это буквы алфавита, а значения - количество записей, у которых фамилия начинается с соответствующей буквы. Функции save_index(), load_index() и update_index() отвечают за сохранение, загрузку и обновление данных в файле index.json.
   Суть оптимизации такова: в index.json хранится словарь вида index = {"A": 0, "Б": 0 ...} и так далее для всех 33 букв алфавита.
   Ключ это сама буква, а значение это число, показывающее колличство записей в которых фамилия начинается с той или иной буквы.
   Наприме, если в справочнике 3 человека с фамилией Иванов, то  index = {... "И": 3 ...}.
   В дальнейшем, когда нам поднадобится найти нужную запись, программа считает первую букву фамилии которую запрашивает пользователь и будет производить поиск не по всему файлу,
   а только по той его части, где фамилии начинаются с нужной букву.
   6. add_records.py содержит функцию add_record(), которая добавляет новые записи в справочник и обновляет данные в файле index.json.
   7. search_record.py содержит функцию search_record(), которая выполняет поиск записей в справочнике. Пользователь должен ввести фамилию для поиска. По желанию можно добавить имя и отчество через пробел для более точного поиска.
   8. update_record.py содержит функцию update_record(), которая обновляет поля в записи справочника. Пользователь может обновить все поля или только некоторые. Для оставления поля без изменений требуется ввести старую информацию заново.

Запуск проекта:
На Windows:
python telephone_directory.py

На Linux:
python3 telephone_directory.py
