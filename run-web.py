from flask import Flask, render_template, request
import sqlite3

CatBase = list()
CatPoints = dict()
conn = sqlite3.connect('cats.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM cat_breeds')
users = cursor.fetchall()
for user in users:
    CatBase.append(user[1:])
    CatPoints[user[1]] = 0
conn.close()

app = Flask(__name__)

criteria = {"size": {"small": ['Корниш-рекс', 'Манчкин'],
                     'medium': ['Бирманская', 'Японский бобтейл', 'Девон-рекс', 'Корниш-рекс', 'Шотландская вислоухая',
                                'Абердин', 'Бразильская короткошерстная', 'Петербургский сфинкс', 'Сфинкс',
                                'Бенгальская', 'Абиссинская', 'Русская голубая', 'Персидская', 'Сиамская',
                                'Британская короткошерстная'],
                     'large': ['Турецкий ван', 'Чаузи', 'Норвежская лесная', 'Сибирская', 'Мэйн-кун']},
            'coat_length': {'short': ['Японский бобтейл', 'Девон-рекс', 'Корниш-рекс', 'Шотландская вислоухая',
                                      'Чаузи', 'Петербургский сфинкс', 'Сфинкс'],
                            'medium': ['Абердин', 'Бразильская короткошерстная', 'Манчкин', 'Бенгальская',
                                       'Абиссинская', 'Русская голубая', 'Сиамская', 'Британская короткошерстная'],
                            'long': ['Бирманская', 'Турецкий ван', 'Норвежская лесная', 'Сибирская', 'Персидская',
                                     'Мэйн-кун']},
            'personality': {'playful': ['Девон-рекс', 'Турецкий ван', 'Чаузи', 'Сфинкс', 'Бенгальская', 'Абиссинская',
                                        'Сиамская'],
                            'calm': ['Японский бобтейл', 'Корниш-рекс', 'Петербургский сфинкс', 'Норвежская лесная',
                                     'Сибирская', 'Манчкин', 'Мэйн-кун'],
                            'independent': ['Бирманская', 'Шотландская вислоухая', 'Абердин',
                                            'Бразильская короткошерстная', 'Русская голубая', 'Персидская',
                                            'Британская короткошерстная']},
            'affection': {
                'high': ['Бирманская', 'Японский бобтейл', 'Девон-рекс', 'Турецкий ван', 'Шотландская вислоухая',
                         'Абердин', 'Бразильская короткошерстная', 'Петербургский сфинкс', 'Сибирская',
                         'Сфинкс', 'Бенгальская', 'Персидская', 'Мэйн-кун', 'Сиамская', 'Британская короткошерстная'],
                'moderate': ['Корниш-рекс', 'Чаузи', 'Норвежская лесная', 'Манчкин', 'Абиссинская',
                             'Русская голубая'],
                'low': []},
            'shedding': {'low': ['Мэйн-кун', 'Норвежская лесная', 'Турецкий ван'],
                         'high': ['Японский бобтейл', 'Девон-рекс', 'Корниш-рекс', 'Шотландская вислоухая',
                                  'Чаузи', 'Петербургский сфинкс', 'Сфинкс'],
                         'any': []}}


@app.route("/")
def base():
    return render_template('base.html', url="/extended", url2="/test")


@app.route('/extended')
def base_extended():
    cards = [
        {'title': CatBase[i][0], 'image': f'{i + 1}.png', 'description': ' '.join(CatBase[i][1:])} for i in
        range(len(CatBase))
    ]
    for i in range(len(cards)):
        cards[i]["description"] = CatBase[i][9] + "\n"
        cards[i]["description"] += "Время жизни - " + CatBase[i][1] + "\n"
        cards[i]["description"] += "Интеллект - " + CatBase[i][2] + "\n"
        cards[i]["description"] += "Общительность - " + CatBase[i][3] + "\n"
        cards[i]["description"] += "Ласковость - " + CatBase[i][4] + "\n"
        cards[i]["description"] += "Шерсть - " + CatBase[i][5] + "\n"
        cards[i]["description"] += "Размер - " + CatBase[i][6] + "\n"
        cards[i]["description"] += "Активность - " + CatBase[i][7] + "\n"
        cards[i]["description"] += "Здоровье - " + CatBase[i][8]
    ads = [
        {"image": "ad_ibio.png",
         "url": "https://discord.com/oauth2/authorize?client_id=834775714011938866&permissions=8&scope=bot"},
        {"image": "ad_main.png", "url": "https://ost-arbetsatt.itch.io/main-element"},
        {"image": "ad_akmor.png", "url": "https://t.me/akmor3"},
    ]
    return render_template('extended.html', cards=cards, ads=ads)


@app.route('/test')
def testing():
    return render_template('test.html')


@app.route('/result', methods=['POST'])
def result():
    points = CatPoints
    for crit in criteria:
        for cat in criteria[crit][request.form.get(crit)]:
            points[cat] += 1
    breed = (sorted([i for i in points], key=lambda x: points[x]))
    print(breed)
    for i in CatPoints:
        CatPoints[i] = 0
    return render_template('result.html', breed=breed[0], recommendations=', '.join(breed[1:4]))


if __name__ == '__main__':
    app.run()
