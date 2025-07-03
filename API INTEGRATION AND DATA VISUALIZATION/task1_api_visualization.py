import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fetch weather data for a few cities
cities = ['London', 'New York', 'Tokyo', 'Delhi', 'Paris']
API_KEY = 'your_openweathermap_api_key_here'  # Replace with your API key
data = []

for city in cities:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        weather = response.json()
        data.append({
            'City': city,
            'Temperature (°C)': weather['main']['temp'],
            'Humidity (%)': weather['main']['humidity'],
            'Wind Speed (m/s)': weather['wind']['speed']
        })

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)

# Plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x="City", y="Temperature (°C)", data=df)
plt.title("City-wise Temperature")
plt.savefig("temperature_plot.png")
plt.show()
