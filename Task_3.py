# Завдання 3

# Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.



# Вимоги до завдання:

# Створіть віртуальне оточення Python для ізоляції залежностей проекту.
# Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
# Використання бібліотеки colorama для реалізації кольорового виведення.
# Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
# Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.



import os
import sys
from colorama import init, Fore

def print_directory_tree(path, indent=""):
    try:
        items = os.listdir(path)
    except PermissionError:
        print(f"{indent}{Fore.RED}[Access Denied] {path}{Fore.RESET}")
        return
    
    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"{indent}{Fore.BLUE}{item}{Fore.RESET}/")
            print_directory_tree(item_path, indent + "  ")
        else:
            print(f"{indent}{Fore.GREEN}{item}{Fore.RESET}")

def main():
    init(autoreset=True) 
    
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    if not os.path.exists(directory_path):
        print(Fore.RED + "Error: Specified path does not exist." + Fore.RESET)
        sys.exit(1)
    
    print_directory_tree(directory_path)

if __name__ == "__main__":
    main()
