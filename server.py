from datetime import datetime

from flask import Flask, abort, request
from req import get_weather
from news_list import all_news
	
city_id = 524901
apikey = "b3744bff49fc93bd96cc993d8279cac7"

app = Flask(__name__)

@app.route("/")
def index():
	url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (city_id, apikey)
	weather = get_weather(url)
	cur_date = datetime.now().strftime("%d.%m.%Y")
	
	result = "<p><b>Temperature: </b> %s</p> City: %s" % (weather['main']['temp'], weather ["name" ])
	result += "<p><b>Date: </b> %s</p>" % cur_date
	return(result)


@app.route("/news" )
def all_the_news():
		#for item in request.args:
			#print(item)
			#print(request.args.get(item))
	colors = ("green", "red", "blue")

	try:
		limit = int(request.args.get("limit", 0))
	except:
		imit = 10
	color = request.args.get("color", "black") if request.args.get ("color") in colors else "black"
	return "<h1 style=color: %s>News: <small>%s</small></h1>" % (color, limit)




@app.route("/news/<int:news_id>")
def news_by_id(news_id):
	news_to_show = [news for news in all_news if news ["id"] == news_id]
	
	#news_to_show2 = []
	#for news in all_news:
	#	if news["id"] == news_id:
	#		news_to_show2.append(news)
	
	if len(news_to_show) == 1:
		print(news_to_show)
		result = "<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>"
		result = result % news_to_show[0]
		return result
	else:
		abort(404)

if __name__ == "__main__":
	app.run(port=5001, debug=True)