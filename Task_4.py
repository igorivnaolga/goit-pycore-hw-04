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


# Рекомендації для виконання

# По перше, нам треба систематизувати опис форматів наших команд для консольного бота-помічника. Це допоможе зрозуміти які функції треба зробити для кожної команди. Зробімо це:

# 1. Команда "hello", тут можна обійтись поки без функції та використати звичайний print:

# Введення: "hello"
# Вивід: "How can I help you?"


# 2. Команда "add [ім'я] [номер телефону]". Для цієї команди зробимо функцію add_contact:

# Введення: "add John 1234567890"
# Вивід: "Contact added."


# 3. Команда "change [ім'я] [новий номер телефону]". Для цієї команди зробимо функцію change_contact:

# Введення: "change John 0987654321"
# Вивід: "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено


# 4. Команда "phone [ім'я]". Для цієї команди зробимо функцію show_phone:

# Введення: "phone John"
# Вивід: [номер телефону] або повідомлення про помилку, якщо ім'я не знайдено


# 5. Команда "all". Для цієї команди зробимо функцію show_all:

# Введення: "all"
# Вивід: усі збережені контакти з номерами телефонів


# 6. Команда "close" або "exit". Оскільки тут треба перервати виконання програми, можна поки обійтись без функції для цих команд:

# Введення: будь-яке з цих слів
# Вивід: "Good bye!" та завершення роботи бота
# Будь-яка команда, яка не відповідає вищезазначеним форматам, буде вважатися нами невірною, і бот буде виводити повідомлення "Invalid command."