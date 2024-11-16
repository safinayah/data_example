from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "your_openweathermap_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

@app.route('/api/weather-insights', methods=['GET'])
def get_weather_insights():
    city = request.args.get('city', 'London')
    response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")
    if response.status_code == 200:
        data = response.json()
        temps = [entry["main"]["temp"] for entry in data["list"]]
        avg_temp = sum(temps) / len(temps)
        return jsonify({
            "city": city,
            "average_temperature": round(avg_temp, 2),
            "forecast_count": len(temps),
            "insight": f"The average temperature in {city} for the next 5 days is {round(avg_temp, 2)}°C."
        })
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
