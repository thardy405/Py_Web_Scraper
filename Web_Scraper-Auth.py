import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
print(res.text[:250])