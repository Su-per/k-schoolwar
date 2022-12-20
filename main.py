import os

os.system("pip3 install httpx")

import httpx

url = "https://port-0-kschool-backend-37y7e24l7jiwra5.gksl1.cloudtype.app/pop/?count=50&token=&schoolCode=7380292"

while True:
    r = httpx.post(url)
    r = r.json()
    try:
        if r['error'] == True:
            print("Too many reqeust")
    except:
        print(f"랭킹 : {r['rank']} 개수 : {r['pop']}")
