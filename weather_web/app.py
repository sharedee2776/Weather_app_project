import os
import requests
from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv

# Load .env (for local development)
load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("ERROR: API_KEY is not set. Create a .env file or add it to your deployment environment.")

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
ONECALL_URL = "https://api.openweathermap.org/data/3.0/onecall"  # use 2.5 if you're on free tier

app = Flask(__name__)

def get_weather_icon(description):
    description = description.lower()
    if "clear" in description:
        return "☀️"
    if "cloud" in description:
        return "☁️"
    if "rain" in description:
        return "🌧️"
    if "thunder" in description:
        return "⛈️"
    if "snow" in description:
        return "❄️"
    if "fog" in description or "mist" in description:
        return "🌫️"
    return "🌍"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]

        # Current weather request
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        res = requests.get(CURRENT_URL, params=params)
        data = res.json()

        if res.status_code != 200:
            return render_template("result.html", error=True, message=data.get("message", "Invalid city"))

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        icon = get_weather_icon(desc)

        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        # Weather alerts (One Call API)
        alert_params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric"}
        alert_res = requests.get(ONECALL_URL, params=alert_params)
        alert_data = alert_res.json()

        alerts = alert_data.get("alerts", [])

        return render_template(
            "result.html",
            city=city.capitalize(),
            temp=temp,
            desc=desc,
            icon=icon,
            alerts=alerts
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
