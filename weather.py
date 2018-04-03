import requests

def get_weather_forecast():
	# Connecting to the weather API
	# You will need to get an api key from the weathermap and then add this after the = at the end
	url = 'http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid='
	weather_request = requests.get(url)
	weather_json = weather_request.json()

	# Parsing the JSON
	description = weather_json['weather'][0]['description']
	temp_min = weather_json['main']['temp_min']
	temp_max = weather_json['main']['temp_max']

	# Creating our forecast string
	forecast = 'The London forecast for today is ' 
	forecast += description + ' with a high of ' + str(temp_max)
	forecast += ' Celsius and a low of ' + str(temp_min) + " Celsius."

	return(forecast)

