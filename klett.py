# made by maxvel187
# https://guns.lol/maxvel187
# this is for educational purposes only and may violate klett.de Terms of Service
# use this at your own risk!

import requests
from PIL import Image
import os

print("inspect element, go to network tab, refresh, go to the first request and find Cookies")
print("it should look like that")
print("SESSION=xxxxxxxxxxxxx; klett_cookie_consent={%22statistiken%22:true}; klett_session=xxxxxxxxxx; SERVERID=backend4")
session = input("Input your klett.de SESSION: ")
klett_session = input("Input your klett.de klett_session: ")
print("your book id is found in the link of your e-book (https://bridge.klett.de/(here)/?page=x)")
book = input("Input your book id: ")
print("1 = normal")
print("2 = good")
print("3 = high details")
qual = input("In what quality do you want to download: ")

if qual == "1":
    pass
elif qual == "2":
    pass
elif qual == "3":
    qual = "4"
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

downloaded_pages = []

for pg in range(1, 1000):
    url = f"{url1}{pg}{url2}"
    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        filename = f"Page_{pg}.png"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Image for page {pg} downloaded successfully.")
        downloaded_pages.append(filename)
    else:
        print(f"Stopped at page {pg} (status: {response.status_code}).")
        break

if downloaded_pages:
    print("Creating PDF file...")
    images = [Image.open(img).convert("RGB") for img in downloaded_pages]
    pdf_name = f"{book}_klett_book.pdf"
    images[0].save(pdf_name, save_all=True, append_images=images[1:])
    print(f"PDF created successfully: {pdf_name}")

    # Optional cleanup (delete PNGs after PDF creation)
    cleanup = input("Delete all PNG files after creating PDF? (y/n): ")
    if cleanup.lower() == "y":
        for img in downloaded_pages:
            os.remove(img)
        print("All PNG files deleted.")

print("Success or invalid data provided.")
