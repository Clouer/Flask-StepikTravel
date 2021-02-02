from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_main():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def render_departure(departure):
    return render_template('departure.html')


@app.route('/tours/<int:id>/')
def render_tour(id):
    return render_template('tour.html')


app.run(debug=True)
