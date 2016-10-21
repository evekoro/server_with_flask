import csv

#user_list=[
#{'username': '30.323317051', 'idnb': '430593', 'ISIpubdate': 'image', 'local_hour': 'luiza_orlenko', 'URL': '01/07/14', 'tags': '2', 'lat\tlon\tdistance': '59.97082081', 'local_month': '9', 'type': '7', 'local_wday': 'ботаническийсад***ботаника***практика', 'local_date': '3', None: ['https://scontent.cdninstagram.com/t51.2885-15/e15/11909192_910892238997360_1863117603_n.jpg?ig_cache_key=NzU0Nzg3MzkwMTQ0NTAxOTEw.2', '0']}
#{'username': '30.323317051', 'idnb': '430598', 'ISIpubdate': 'image', 'local_hour': 'indigo25', 'URL': '01/07/14', 'tags': '2', 'lat\tlon\tdistance': '59.97082081', 'local_month': '8', 'type': '7', 'local_wday': 'лето***spbgram***спб***ботаническийсад***ирисы***санктпетербург***питер***summertime***saintpetersburg***цветы***spb***floralwaltz***flowers', 'local_date': '3', None: ['https://scontent.cdninstagram.com/t51.2885-15/e15/10483337_902855776397157_1820912684_n.jpg?ig_cache_key=NzU0NzU1MDA5OTExMjMzMTc1.2', '0']}
#{'username': '30.34190125', 'idnb': '430602', 'ISIpubdate': 'image', 'local_hour': 'bel4aka', 'URL': '01/07/14', 'tags': '2', 'lat\tlon\tdistance': '59.96692039', 'local_month': '7', 'type': '7', 'local_wday': '', 'local_date': '3', None: ['https://scontent.cdninstagram.com/t51.2885-15/e15/10453982_1567307460163288_197384173_n.jpg?ig_cache_key=NzU0NzIyNjcyNzU5MDYyMjg1.2', '0']}
#{'username': '30.307333268', 'idnb': '430603', 'ISIpubdate': 'image', 'local_hour': 'linevichtanya', 'URL': '01/07/14', 'tags': '2', 'lat\tlon\tdistance': '59.973718571', 'local_month': '7', 'type': '7', 'local_wday': 'kotyatky', 'local_date': '3', None: ['https://scontent.cdninstagram.com/t51.2885-15/e15/10522852_510478639080614_1654309762_n.jpg?ig_cache_key=NzU0NzIxODQyNDYwMjE5MzQw.2', '0']}
#]

with open('example.csv', 'r', encoding='utf-8') as f:
    fields = ['idnb', 'lat', 'lon', 'distance', 'username', 'tags', 'local_hour', 'local_wday', 'local_month', 'local_date', 'type', 'URL', 'ISIpubdate']
    reader = csv.DictReader(f, fields, delimiter='\t')
    for user in reader:
        print(user['username'], user['URL'])	