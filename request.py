import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'likes':2, 'Checkins':9, 'Returns':6, 'Category':2,	'commBase':1, 'comm24':10,	'comm48':12,	'comm24_1':5, 'diff_24.48':4, 'length':5, 'shares':12})

print(r.json())