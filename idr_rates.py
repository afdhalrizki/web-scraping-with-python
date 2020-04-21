import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
# print(json_data.json())

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.4522756866811e-5,"date":"Mon, 20 Apr 2020 00:00:01 GMT","inverseRate":15498.407826315},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.9422106905139e-5,"date":"Mon, 20 Apr 2020 00:00:01 GMT","inverseRate":16828.753675739}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
