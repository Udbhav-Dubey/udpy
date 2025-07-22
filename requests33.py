import requests.auth import HTTPDigestAuth
url = 'https://httpbin.org/digest-auth/auth/user/pass'
response=requests.get(url,auth=HTTPDigestAuth('user','pass'))

