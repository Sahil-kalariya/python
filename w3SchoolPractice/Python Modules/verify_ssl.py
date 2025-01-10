import requests

response = requests.get('http://rigaux.org/', verify = False)
print(response)

response1 = requests.get('http://google.com')
print(response)

response1 = requests.get('http://rigaux.org/',verify = True)
print(response1) 

