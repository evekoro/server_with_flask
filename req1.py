
	import requests 

def get_weather(url):
	result = requests.get(url)
	print(result.json()["name"])

if __name__ == "__main__":
	get_weather("http://api.openweathermap.org/data/2.5/weather?q=Londont&APPID=b3744bff49fc93bd96cc993d8279cac7")
