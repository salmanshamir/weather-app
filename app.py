import requests
import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, flash, session
from datetime import datetime
import pycountry


load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"]=os.getenv("SECRET_KEY")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/weather", methods=["POST", "GET"])
def weather():
    if request.method=="POST":
        try:
            city = (request.form.get("city")).capitalize()
            api_key = os.getenv("API_KEY")
            URL = "https://api.openweathermap.org/data/2.5/weather"
    
            params = {
                "q": city,
                "appid": api_key,
                "units": "metric"
            }
            response = requests.get(URL, params=params)
            data = response.json()
            city = data["name"]
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]
            icon = data["weather"][0]["icon"]
            pressure = data["main"]["pressure"]
            visibility = data["visibility"]/100
            sunrise = datetime.time(datetime.fromtimestamp(data["sys"]["sunrise"]))
            sunset = datetime.time(datetime.fromtimestamp(data["sys"]["sunset"]))
            date = datetime.date(datetime.now())
            country_code = data["sys"]["country"]
            country_match = pycountry.countries.get(alpha_2=country_code)
            country= country_match.name if country_match else country_code
            return render_template("index.html", city=city, date=date, temp_min=temp_min, temp_max=temp_max, country=country, feels_like=feels_like, temperature=temperature, humidity=humidity, description=description, wind_speed=wind_speed, icon=icon, pressure=pressure, visibility=visibility, sunrise=sunrise, sunset=sunset)
        except:
            flash("City does not found")
            return redirect(url_for("index"))
        
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

