# Завдання 1

# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

# Наприклад:

# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000

# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.



# Вимоги до завдання:

# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
# Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
# Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.


def total_salary(path):
    try:
        salaries = [] 

        with open(path, encoding="utf-8") as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line: 
                    salary = int(cleaned_line.split(',')[1])
                    salaries.append(salary)

        
        total = sum(salaries)
        if salaries:
            average = total / len(salaries)
        else:
            average = 0

        return total, average

    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return 0, 0
    except ValueError:
        print("Invalid data format in file.")
        return 0, 0


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
