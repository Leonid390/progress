from flask import Flask
import random
app = Flask(__name__)

facts_list = ['''Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс,
               когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.
              ''', 
              '''Согласно исследованию, проведенному в 2018 году, 
              более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.''']
oreshka_list = ["Орёл", "Решка"]

@app.route("/")
def fact():
    return  '<h1>факты по ссылке:</h1> <a href="/random_fact">Посмотреть случайный факт!</a>'

@app.route("/random_fact")
def random_fact():
    return  f'<h1>{random.choice(facts_list)}</h1>'

@app.route("/secret")
def secret():
    return  f'<h2>{random.choice(oreshka_list)}</h2>'

app.run(debug=True)


