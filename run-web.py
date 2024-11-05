from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def base():
    return render_template('base.html', url="/extended", url2="/test")


@app.route('/extended')
def base_extended():
    cards = [
        {'title': CatBase[i][0], 'image': f'{i + 1}.png', 'description': ' '.join(CatBase[i][1:])} for i in range(len(CatBase))
    ]
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


if __name__ == '__main__':
    CatBase = list()
    conn = sqlite3.connect('cats.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cat_breeds')
    users = cursor.fetchall()
    for user in users:
        CatBase.append(user[1:])
    conn.close()
    app.run()
