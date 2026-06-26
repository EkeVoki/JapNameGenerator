#ver 1.1

import random
from datetime import datetime
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

eng = 0
ru = 0
print("Select language:")
print("1. eng")
print("2. ru")
select = (input())
if select == "1":
    eng = 1
if select == "2":
    ru = 1
elif select != "1" and select != "2":
        print("Error, default language!")
        eng = 1

if eng == 1:
    print("Enter the quantity:")
    count = int(input())
if ru == 1:
    print("Введите число")
    count = int(input())

if eng == 1:
    fem_1 = [
        "Yama", "Kita", "Minami", "Nishi", "Higashi", "Oo", "Ko", "Matsu", "Taka", "Kawa"
    ]
    fem_2 = [
        "da", "ta", "moto", "shita", "mura", "gawa", "kawa", "wara", "ue", "oji"
    ]

    name_male_1 = [
        "Hiro", "Ken", "Ryu", "Sho", "Dai", "Kazu", "Take", "Toshi", "Shin", "Yu"
    ]
    name_male_2 = [
        "ta", "to", "suke", "ro", "ki", "ya", "hei", "ma", "o", "ichi"
    ]

    name_fem_1 = [
        "Sakura", "Yuki", "Haru", "Ai", "Mi", "Hana", "Nana", "Rin", "Ao", "Ami"
    ]
    name_fem_2 = [
        "ko", "mi", "ka", "na", "ri", "no", "ho", "e", "yo", "yu"
    ]

if ru == 1:
    fem_1 = [
        "Яма", "Кита", "Минами", "Ниси", "Хигаси", "Оо", "Ко", "Мацу", "Така", "Кава"
    ]
    fem_2 = [
        "да", "та", "мото", "сита", "мура", "гава", "кава", "вара", "уэ", "одзи"
    ]

    name_male_1 = [
        "Хиро", "Кен", "Рю", "Шо", "Дай", "Кадзу", "Такэ", "Тоси", "Син", "Ю"
    ]
    name_male_2 = [
        "та", "то", "сукэ", "ро", "ки", "я", "хэй", "ма", "о", "ити"
    ]

    name_fem_1 = [
        "Сакура", "Юки", "Хару", "Ай", "Ми", "Хана", "Нана", "Рин", "Ао", "Ами"
    ]
    name_fem_2 = [
        "ко", "ми", "ка", "на", "ри", "но", "хо", "э", "ё", "ю"
    ]

names_list = []

for i in range(count):
    # Surname
    start_fem_1 = random.choice(fem_1)
    fin_fem_2 = random.choice(fem_2)
    while start_fem_1.lower() == fin_fem_2.lower():
        fin_fem_2 = random.choice(fem_2)
    fem = start_fem_1 + fin_fem_2
    if fem.startswith("Ooo"): 
        fem = fem.replace("Ooo", "Oo")

    # Male name
    start_name_male_1 = random.choice(name_male_1)
    fin_name_male_2 = random.choice(name_male_2)
    while start_name_male_1.lower() == fin_name_male_2.lower():
        fin_name_male_2 = random.choice(name_male_2)
    name_male = start_name_male_1 + fin_name_male_2

    # Female name
    start_name_fem_1 = random.choice(name_fem_1)
    fin_name_fem_2 = random.choice(name_fem_2)
    if eng == 1:
        while start_name_fem_1 == "Nana" and fin_name_fem_2 == "na":
            fin_name_fem_2 = random.choice(name_fem_2)
        while start_name_fem_1.lower() == fin_name_fem_2.lower():
            fin_name_fem_2 = random.choice(name_fem_2)
        name_fem = start_name_fem_1 + fin_name_fem_2
    if ru == 1:
        while start_name_fem_1 == "Нана" and fin_name_fem_2 == "на":
            fin_name_fem_2 = random.choice(name_fem_2)
        while start_name_fem_1.lower() == fin_name_fem_2.lower():
            fin_name_fem_2 = random.choice(name_fem_2)
        name_fem = start_name_fem_1 + fin_name_fem_2

    # Output
    if random.choice([True, False]):
        full_name = fem + " " + name_fem
    else:
        full_name = fem + " " + name_male
    
    print(full_name)
    names_list.append(full_name)

if eng == 1:
    save = "Save results to file? (y/n): "
    save_choice = input(save).lower()
    if save_choice == "y":
        date = datetime.now().strftime("%Y-%m-%d")
        filename = os.path.join(script_dir, f"names_{date}.txt")
        with open(filename, "w") as file:
            for name in names_list:
                file.write(name + "\n")
        print(f"Saved to {filename}")
    else:
        print("okay ＞＿＜")
else:
    save = "Сохранить результаты в файл? (д/н): "
    save_choice = input(save).lower()
    if save_choice == "д":
        date = datetime.now().strftime("%Y-%m-%d")
        filename = os.path.join(script_dir, f"names_{date}.txt")
        with open(filename, "w") as file:
            for name in names_list:
                file.write(name + "\n")
        print(f"Сохранено в {filename}")
    else:
        print("Ладно ＞＿＜")