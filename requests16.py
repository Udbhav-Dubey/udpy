import requests 
r=requests.get("https://www.google.com/")
if 'Set-Cookie' in r.headers:
    print("Cookie from server : ",r.headers['Set-Cookie'])
else :
    print("no cookie set.")
