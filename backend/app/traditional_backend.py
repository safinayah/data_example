from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "your_openweathermap_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'London')
    response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        })
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
