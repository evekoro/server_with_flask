import requests

def get_weather(url):
	result = requests.get(url)
	if result.status_code == 200:
		return result.json()
	else: 
		print("Something went wrong!")


if __name__ == "__main__":
	data = get_weather("http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=b3744bff49fc93bd96cc993d8279cac7&units=metric")
	print(data)