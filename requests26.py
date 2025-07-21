import requests as rq
url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.21&current_weather=true"
r=rq.get(url)
print(r.text)
print("\nmit\n")
r2=rq.get('https://www.mit.edu/~ecprice/wordlist.10000')
print(r2.text[:50])
r3 = rq.get('https://jsonplaceholder.typicode.com/posts')
print(r3.text.split('\n')[:3])
