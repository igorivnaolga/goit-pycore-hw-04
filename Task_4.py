# Завдання 4

# Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.

# ☝ Бот помічник повинен стати для нас прототипом застосунку-асистента, який ми розробимо в наступних домашніх завданнях. Застосунок-асистент в першому наближенні повинен вміти працювати з книгою контактів та календарем.


# У цій домашній роботі зосередимося на інтерфейсі самого бота. Найпростіший і найзручніший на початковому етапі розробки інтерфейс - це консольний застосунок CLI (Command Line Interface). CLI достатньо просто реалізувати.

# Будь-який CLI складається з трьох основних елементів:

# Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
# Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
# Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції - handler-а.


# На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, скористаємося словником. У словнику будемо зберігати ім'я користувача, як ключ, і номер телефону як значення.



# Вимоги до завдання:

# Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
# Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. Команди та аргументи мають бути розпізнані незалежно від регістру введення.
# Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. В разі введення команди "exit" або "close", програма повинна завершувати виконання.
# Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
# Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
# Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.



def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Use: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "invalid input. Use: change <name> <new_phone>"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found"
    

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid input. Use: phone <name>"
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}:{phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

    