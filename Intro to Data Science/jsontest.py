import json
import requests

url = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=4005c05d541d9a056136d5450be12883&artist=Rihanna&album=Loud&format=json'

data = requests.get(url).text
data = json.loads(data)
print(data)
print()

print('Readable : ', json.dumps(data,indent=4))
print()

print(data['album']['listeners'])
print()

#find the top artist in Spain and # of listeners

geo_url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&api_key=4005c05d541d9a056136d5450be12883&country=spain&format=json'

geo_data = requests.get(geo_url).text
geo_data = json.loads(geo_data)


print('Readable : ', json.dumps(geo_data,indent=4))

spain_top = geo_data['topartists']['artist'][0]

print(spain_top['name'])
print(spain_top['listeners'])
