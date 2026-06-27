from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
import random

app = FastAPI()


fem_1_en = ["Yama", "Kita", "Minami", "Nishi", "Higashi", "Oo", "Ko", "Matsu", "Taka", "Kawa"]
fem_2_en = ["da", "ta", "moto", "shita", "mura", "gawa", "kawa", "wara", "ue", "oji"]
name_male_1_en = ["Hiro", "Ken", "Ryu", "Sho", "Dai", "Kazu", "Take", "Toshi", "Shin", "Yu"]
name_male_2_en = ["ta", "to", "suke", "ro", "ki", "ya", "hei", "ma", "o", "ichi"]
name_fem_1_en = ["Sakura", "Yuki", "Haru", "Ai", "Mi", "Hana", "Nana", "Rin", "Ao", "Ami"]
name_fem_2_en = ["ko", "mi", "ka", "na", "ri", "no", "ho", "e", "yo", "yu"]


fem_1_ru = ["Яма", "Кита", "Минами", "Ниси", "Хигаси", "Оо", "Ко", "Мацу", "Така", "Кава"]
fem_2_ru = ["да", "та", "мото", "сита", "мура", "гава", "кава", "вара", "уэ", "одзи"]
name_male_1_ru = ["Хиро", "Кен", "Рю", "Шо", "Дай", "Кадзу", "Такэ", "Тоси", "Син", "Ю"]
name_male_2_ru = ["та", "то", "сукэ", "ро", "ки", "я", "хэй", "ма", "о", "ити"]
name_fem_1_ru = ["Сакура", "Юки", "Хару", "Ай", "Ми", "Хана", "Нана", "Рин", "Ао", "Ами"]
name_fem_2_ru = ["ко", "ми", "ка", "на", "ри", "но", "хо", "э", "ё", "ю"]

def generate_names(count: int = 1, lang: str = "en"):
    if lang == "ru":
        fem_1, fem_2 = fem_1_ru, fem_2_ru
        name_male_1, name_male_2 = name_male_1_ru, name_male_2_ru
        name_fem_1, name_fem_2 = name_fem_1_ru, name_fem_2_ru
    else:
        fem_1, fem_2 = fem_1_en, fem_2_en
        name_male_1, name_male_2 = name_male_1_en, name_male_2_en
        name_fem_1, name_fem_2 = name_fem_1_en, name_fem_2_en

    result = []
    for _ in range(count):
        surname = random.choice(fem_1) + random.choice(fem_2)
        if random.choice(["male", "female"]) == "male":
            first = random.choice(name_male_1) + random.choice(name_male_2)
        else:
            first = random.choice(name_fem_1) + random.choice(name_fem_2)
        result.append(f"{surname} {first}")
    return result

@app.get("/api/generate")
def api_generate(
    count: int = Query(1, description="Number of names (max 10)"),
    lang: str = Query("en", description="Language: en or ru")
):
    count = min(count, 10)
    names = generate_names(count, lang)
    return JSONResponse({"names": names})

@app.get("/", response_class=HTMLResponse)
def index():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🎌 Japanese Name Generator</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; text-align: center; padding: 50px; background: #f8f4f0; }
            h1 { color: #2c3e50; font-size: 3em; }
            .controls { margin: 30px 0; }
            label { font-size: 1.2em; margin: 0 10px; }
            input, select, button { padding: 12px 20px; font-size: 1em; border-radius: 10px; border: 1px solid #ccc; }
            button { background: #2c3e50; color: white; cursor: pointer; transition: 0.2s; }
            button:hover { background: #1a252f; }
            #result { margin-top: 40px; display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; }
            .name-card { background: white; padding: 20px 30px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); font-size: 1.8em; font-weight: bold; color: #2c3e50; }
        </style>
    </head>
    <body>
        <h1>🎌 Japanese Name Generator</h1>
        <div class="controls">
            <label>Count:</label>
            <input type="number" id="count" value="1" min="1" max="10">
            <label>Language:</label>
            <select id="lang">
                <option value="en">English</option>
                <option value="ru">Русский</option>
            </select>
            <button onclick="generate()">Generate</button>
        </div>
        <div id="result"></div>
        <script>
            async function generate() {
                const count = document.getElementById('count').value;
                const lang = document.getElementById('lang').value;
                const response = await fetch(`/api/generate?count=${count}&lang=${lang}`);
                const data = await response.json();
                const resultDiv = document.getElementById('result');
                resultDiv.innerHTML = data.names.map(name => `<div class="name-card">${name}</div>`).join('');
            }
        </script>
    </body>
    </html>
    """
    return html_content