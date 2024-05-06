import requests
data = '123ghghgh'
response = requests.get(f'http://192.168.0.8/?TEST={data}')
contents = response.text
print(contents)
