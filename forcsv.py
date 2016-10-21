import csv
with open('spg-meta-d2.csv', 'r', encoding='utf-8') as f:
    fields = ['idnb', 'lat	lon	distance', 'username', 'tags', 'local_hour', 'local_wday', 'local_month', 'local_date', 'type', 'URL', 'ISIpubdate']
    reader = csv.DictReader(f, fields, delimiter='	')
    for row in reader:
        print(row)						
