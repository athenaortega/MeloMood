import json

json_string = ('{"coord":{"lon":-122.3321,"lat":47.6062},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"base":"stations","main":{"temp":284.16,"feels_like":283.38,"temp_min":282.69,"temp_max":285.39,"pressure":1027,"humidity":79,"sea_level":1027,"grnd_level":1017},"visibility":10000,"wind":{"speed":3.6,"deg":160},"clouds":{"all":75},"dt":1729619485,"sys":{"type":2,"id":2041694,"country":"US","sunrise":1729607945,"sunset":1729645681},"timezone":-25200,"id":5809844,"name":"Seattle","cod":200}')

#Convert the string to a JSON object
json_obj = json.loads(json_string)

print(json_obj)

for item in json_obj
    print(item)
    pass