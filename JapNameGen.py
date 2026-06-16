import random

print("Enter the quantity:")
count = int(input())

fam_1 = [
    "Yama", "Kita", "Minami", "Nishi", "Higashi", "Oo", "Ko", "Matsu", "Taka", "Kawa"
]
fam_2 = [
    "da", "ta", "moto", "shita", "mura", "gawa", "kawa", "wara", "ue", "oji"
]

name_male_1 = [
    "Hiro", "Ken", "Ryu", "Sho", "Dai", "Kazu", "Take", "Toshi", "Shin", "Yu"
]
name_male_2 = [
    "ta", "to", "suke", "ro", "ki", "ya", "hei", "ma", "o", "ichi"
]

name_fam_1 = [
    "Sakura", "Yuki", "Haru", "Ai", "Mi", "Hana", "Nana", "Rin", "Ao", "Ami"
]
name_fam_2 = [
    "ko", "mi", "ka", "na", "ri", "no", "ho", "e", "yo", "yu"
]

for _ in range(count):
    # Surname
    start_fam_1 = random.choice(fam_1)
    fin_fam_2 = random.choice(fam_2)
    while start_fam_1.lower() == fin_fam_2.lower():
        fin_fam_2 = random.choice(fam_2)
    fam = start_fam_1 + fin_fam_2
    if fam.startswith("Ooo"):
        fam = fam.replace("Ooo", "Oo")

    # Male name
    start_name_male_1 = random.choice(name_male_1)
    fin_name_male_2 = random.choice(name_male_2)
    while start_name_male_1.lower() == fin_name_male_2.lower():
        fin_name_male_2 = random.choice(name_male_2)
    name_male = start_name_male_1 + fin_name_male_2

    # Female name
    start_name_fam_1 = random.choice(name_fam_1)
    fin_name_fam_2 = random.choice(name_fam_2)
    while start_name_fam_1 == "Nana" and fin_name_fam_2 == "na":
        fin_name_fam_2 = random.choice(name_fam_2)
    while start_name_fam_1.lower() == fin_name_fam_2.lower():
        fin_name_fam_2 = random.choice(name_fam_2)
    name_fam = start_name_fam_1 + fin_name_fam_2

    # Output
    if random.choice([True, False]):
        print(fam + " " + name_fam)
    else:
        print(fam + " " + name_male)