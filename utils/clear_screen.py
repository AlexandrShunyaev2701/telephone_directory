import os


def clear_screen() -> None:
    """
    Функция для очистки экрана консоли
    """
    os.system('cls' if os.name == 'nt' else 'clear')
