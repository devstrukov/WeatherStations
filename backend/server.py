from flask import Flask
from flask import jsonify
from domain.weather_station import WeatherStation

app = Flask(__name__)

@app.route("/stations")
def hello_world():
    results = list()

    stationOne = WeatherStation(
        'f144cded-b3f2-4871-93a6-1ea7f8bc3cea',
        'Станция в Екатеринбурге',
        56.875,
        60.625,
    17.9,
    47,
    3.2
    )

    stationTwo = WeatherStation(
        '2760e64c-55fc-4a29-9dd0-5825eac8040c',
        'Станция в деревне',
        56.375,
        55.4375,
    18.4,
    52,
    3.4
    )

    results.append(stationOne.toDict())
    results.append(stationTwo.toDict())

    return jsonify(results)