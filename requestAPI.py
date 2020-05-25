#打api的套件 
#從私人企業伺服器端的資料庫、從中用api取他們的json檔
#json檔就是一串矩陣與物件的排列，表示數據

import requests
r = requests.get('http://t.weather.sojson.com/api/weather/city/101340102')
r.json()
jsonData = r.json()
print('今天要注意: ', jsonData['data']['forecast'][0]['notice']) #今天的天氣日報
print('今日高溫: ', jsonData['data']['forecast'][0]['high']) 
print('今日低溫: ', jsonData['data']['forecast'][0]['low']) 