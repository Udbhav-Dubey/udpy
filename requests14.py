import requests
r=requests.get("https://www.google.com/",allow_redirects=False)
if r.status_code in {301,302}:
    print(r.headers['Location'])
else:
    print("no redirection.")

