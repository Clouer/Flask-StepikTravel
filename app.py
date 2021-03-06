from random import sample

from flask import Flask, render_template, abort

import data

app = Flask(__name__)


@app.route('/')
def render_main():
    random_tours = {}
    # Генерируем 6 случайных уникальных id туров из общей базы
    random_tours_id = sample(range(min(data.tours.keys()), max(data.tours.keys())), 6)
    # Формируем словарь туров из полученных id
    for tour in random_tours_id:
        random_tours[tour] = data.tours[tour]
    return render_template('index.html',
                           random_tours=random_tours,
                           title=data.title,
                           subtitle=data.subtitle,
                           description=data.description
                           )


@app.route('/departures/<departure>/')
def render_departure(departure):
    if departure not in data.departures:
        abort(404)
    sorted_departures = {}
    # Сортируем и формируем словарь туров по параметру departure
    for tour in data.tours:
        if data.tours[tour]['departure'] == departure:
            sorted_departures[tour] = data.tours[tour]
    return render_template('departure.html',
                           current_departure=departure,
                           tours=sorted_departures,
                           title=data.title + ' | Туры ' + data.departures[departure]
                           )


@app.route('/tours/<int:tour_id>/')
def render_tour(tour_id):
    # Пытаемся получить тур и направление из базы по tour_id. Если не находим, поднимаем 404
    try:
        tour = data.tours[tour_id]
    except KeyError:
        abort(404)
    tour_departure = data.departures[(tour['departure'])]
    return render_template('tour.html',
                           tour=tour,
                           tour_departure=tour_departure,
                           title=data.title + ' | ' + data.tours[tour_id]['title']
                           )


@app.context_processor
def utility_processor():
    return dict(departures=data.departures,
                base_title=data.title)


if __name__ == '__main__':
    app.run()
