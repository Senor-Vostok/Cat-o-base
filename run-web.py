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
        {'title': 'Название 1', 'image': 'ger.jpg', 'url': '/page1'},
        {'title': 'Название 2', 'image': 'cat2.jpg', 'url': '/page2'},
        {'title': 'Название 3', 'image': 'cat3.jpg', 'url': '/page3'},
        {'title': 'Название 4', 'image': 'cat4.jpg', 'url': '/page4'},
        {'title': 'Название 5', 'image': 'cat5.jpg', 'url': '/page5'},
        {'title': 'Название 6ывпаыпврапропыроваыы', 'image': 'cat6.jpg', 'url': '/page6'},
    ]
    ads = [
        {"image": "ad1.jpg", "url": "https://example.com/ad1"},
        {"image": "ger.jpg", "url": "https://example.com/ad2"},
    ]
    return render_template('extended.html', cards=cards, ads=ads)


if __name__ == '__main__':
    app.run()
