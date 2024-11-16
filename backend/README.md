# Backend for Data-Driven Weather Project

This folder contains two backend implementations:

1. **Traditional Backend**:
   - Fetches and displays raw weather data (temperature, description, humidity).
   - Located in `traditional_backend.py`.

2. **Data-Driven Backend**:
   - Fetches 5-day weather data and processes it to calculate average temperature and provide insights.
   - Located in `data_driven_backend.py`.

## Prerequisites
- Python 3.x
- Flask
- Requests library

## Instructions
1. Install dependencies:
   ```bash
   pip install flask requests
   ```

2. Run the desired backend:
   - Traditional Backend:
     ```bash
     python traditional_backend.py
     ```
   - Data-Driven Backend:
     ```bash
     python data_driven_backend.py
     ```

3. Use the APIs:
   - Traditional API: `http://127.0.0.1:5000/api/weather?city=London`
   - Data-Driven API: `http://127.0.0.1:5000/api/weather-insights?city=London`
