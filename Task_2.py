# Завдання 2

# У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:

# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5

# Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.



# Вимоги до завдання:

# Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
# Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


def get_cats_info(path):
    try:
        cats = []

        with open(path, encoding = "utf-8") as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line:
                    cat_id, name, age = line.split(',')
                    cat = {"id": cat_id, "name": name, "age": int(age)}
                    cats.append(cat)

        return cats
    
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return []
    except ValueError:
        print("Invalid data format in file.")
        return []
    
cats_info = get_cats_info("cats.txt")
print(cats_info)


        