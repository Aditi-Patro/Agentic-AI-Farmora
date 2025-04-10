from db.memory import log_decision

def run_weather_agent():
    print("[Weather Agent] Fetching weather forecast (simulated)...")
    
    # You can replace this with actual API integration (e.g., OpenWeatherMap)
    forecast = {
        "next_rain": "in 3 days",
        "avg_temp": "29°C",
        "humidity": "60%"
    }

    message = f"Rain expected {forecast['next_rain']}, Avg Temp: {forecast['avg_temp']}, Humidity: {forecast['humidity']}"
    print(f"[Weather Agent] {message}")
    log_decision("Weather Agent", message)
