import os

def calc_sum(file_path):
    total_sum = 0.0

    try:
        file = open(file_path, 'r')
        for line in file:
            parts = line.strip().split("--")

            if len(parts) == 2:
                total_sum += float(parts[1])
        file.close()
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

    return total_sum

def display_contents(file_path):
    try:
        file = open(file_path, 'r')
        contents = file.read()
        file.close()

        if contents:
            print("Зміст файлу:")
            print(contents)
        else:
            print("Файл порожній.")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)

file_path = os.path.join(current_directory, "output.txt")

print(f"Файл буде створено за шляхом: {file_path}\n")

clear_file_choice = input("Чи потрібно очистити файл перед записом нових даних? (Так/Ні): ").strip().lower()

file = open(file_path, 'a' if clear_file_choice == 'ні' else 'w')
while True:
    data = input("Введіть назву товару та його вартість (або кінець для завершення, або перегляд для перегляду даних): \n")
    if data == 'кінець':
        break
    elif data.lower() == 'перегляд':
        display_contents(file_path)
        continue

    parts = data.split()

    if len(parts) != 2:
        print("Неправильна кількість введених даних. Введіть назву товару та його вартість \n")
        continue

    name, price = parts

    try:
        float_price = float(price)
    except ValueError:
        print("Неправильно введена ціна. Введіть ціну числом.\n")
        continue

    if clear_file_choice == 'так':
        file.seek(0)
        file.truncate()
        clear_file_choice = 'ні' 

    file.write(f"{name} -- {float_price:.2f}\n")

file.close()

sum_total = calc_sum(file_path)
print(f"Загальна вартість товарів: {sum_total:.2f}")