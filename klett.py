# made by maxvel187
# https://guns.lol/maxvel187
# this is for educational purposes only and may violate klett.de Terms of Service
# use this at your own risk!
import requests
print("inspect elemement, go to network tab, refresh, go on any and find Cookies")
print("it should look like that")
print("SESSION=xxxxxxxxxxxxx; klett_cookie_consent={%22statistiken%22:true}; klett_session=xxxxxxxxxx; SERVERID=backend4")
session = input("""Input your klett.de SESSION:""")
klett_session = input("""Input your klett.de klett_session:""")
print("your book id is found in the link of your e-book (https://bridge.klett.de/(here)/?page=x)")
book = input("Input your book id:")
print("1 = normal")
print("2 = good")
print("3 = high details")
qual = input("In what quality do you want to download:")

if qual == "1":
    print("")
elif qual == "2":
    print("")
elif qual == "3":
    qual = "4"
    print("")
else:
    print("invalid quality, downloading normal")
    qual = "1"

url1 = f"https://bridge.klett.de/{book}/content/pages/page_"
url2 = f"/Scale{qual}.png"
headers = {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6",
    "priority": "i",
    "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0"
}
cookies = {
    "SESSION": f"{session}",
    "klett_cookie_consent": '{"statistiken":true}',
    "klett_session": f"{klett_session}",
    "SERVERID": "backend4"
}

for pg in range(1, 1000):
    url = f"{url1}{pg}{url2}"
    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        filename = f"Padge_{pg}.png"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Image for page {pg} downloaded successfully.")
    else:
        print(f"Failed to download image from page {pg}. Status code: {response.status_code}")
        break

print("Success or invalid data provided.")
