import requests 
url="https://upload.wikimedia.org/wikipedia/en/1/14/The_Incredible_Hulk_Issue_181.jpg"
res=requests.head(url)
for key,value in res.headers.items():
    print(key," : ", value)
