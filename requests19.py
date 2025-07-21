import requests
img_url="https://static.wikia.nocookie.net/marveldatabase/images/7/7a/Uncanny_X-Men_Vol_1_251.jpg/revision/latest/scale-to-width-down/1200?cb=20240816194023"
res=requests.get(img_url)
with open('wolverine_crucified.png','wb') as f:
    f.write(res.content)

