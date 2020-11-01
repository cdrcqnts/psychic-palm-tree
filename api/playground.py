import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

x = requests.get('https://wttr.in/~MUC?format=j1')

y = x.json()

pp.pprint(y["weather"][0].keys())
pp.pprint(y.keys())
pp.pprint(y["current_condition"][0])

# for i in y["weather"]:
#     print(i['date'])
validkeys = ['temp_C', 'uvIndex', 'weatherCode', 'weatherDesc', 'precipMM', 'cloudcover']
f = dict(filter(lambda i:i[0] in validkeys, y["current_condition"][0].items()))

print(f)