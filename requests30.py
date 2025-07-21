import requests
response=requests.get("https://api.github.com/")
print(response)
print(response.ok)
print(response.links)
url = "https://api.github.com/users/octocat/repos"
response = requests.get(url)

print(response.links)
