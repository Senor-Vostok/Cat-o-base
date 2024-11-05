from flask import Flask, render_template, request, redirect
import time
import json
import requests
import os


app = Flask(__name__)


@app.route("/")
def base():
    return render_template('base.html', url="/extended")


@app.route('/extended')
def base_extended():
    cards = [
        {'title': 'Название 1', 'image': 'ger.jpg', 'url': '/page1', 'description': 'Описание для Названия 1'},
        {'title': 'Название 2', 'image': 'cat2.jpg', 'url': '/page2', 'description': 'Описание для Названия 2'},
        {'title': 'Название 3', 'image': 'cat3.jpg', 'url': '/page3', 'description': 'Описание для Названия 3'},
        {'title': 'Название 4', 'image': 'cat4.jpg', 'url': '/page4', 'description': 'Описание для Названия 4'},
        {'title': 'Название 5', 'image': 'cat5.jpg', 'url': '/page5', 'description': 'Описание для Названия 5'},
        {'title': 'Название 6', 'image': 'cat6.jpg', 'url': '/page6', 'description': 'Описание для Названия 6'},
    ]
    ads = [
        {"image": "ad_ibio.png", "url": "https://discord.com/oauth2/authorize?client_id=834775714011938866&permissions=8&scope=bot"},
        {"image": "ad_main.png", "url": "https://ost-arbetsatt.itch.io/main-element"},
        {"image": "ad_akmor.png", "url": ""},
    ]
    return render_template('extended.html', cards=cards, ads=ads)



if __name__ == '__main__':
    app.run()
