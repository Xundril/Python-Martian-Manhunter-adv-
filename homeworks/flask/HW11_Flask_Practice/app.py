from flask import Flask, render_template, request, jsonify, Response
import requests
from config import Config

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():
    city = request.form.get("city")
    querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
                   "units": "metric"}

    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }

    response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        weather = data['list'][0]
        return render_template("weather.html", weather=weather)

    return Response(status=404)


@app.route('/search_position', methods=['POST'])
def search_weather_position():
    weather = []
    lon = request.form.get("lon")
    lat = request.form.get("lat")
    querystring = {"q": "", "cnt": "1", "mode": "null", "lon": lon, "type": "link, accurate", "lat": lat,
                   "units": "metric"}

    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }

    response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
    data = response.json()

    if response.status_code == 200:
        weather.append(data['list'][0])
        return render_template("weather.html", weather=weather)
    else:
        weather.append(data)
        return render_template("incorrect_data.html", weather=weather)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
