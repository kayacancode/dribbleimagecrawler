from bs4 import BeautifulSoup
import requests as rq
import os

r2 = rq.get("https://dribbble.com/search/shots/popular/illustration?q=sneaker%20")
soup2 = BeautifulSoup(r2.text, "html.parser")

links = []

x = soup2.select('img[src^="https://static.dribbble.com"]')

os.mkdir('dribblephotos')

# Only one for loop required, shouldn't iterate twice if not required
for index, img in enumerate(x):
    # Store the current url from the image result
    url = img["src"]
    # Check the url for screenshot before putting in the links
    if "screenshot" in url:
        links.append(img['src'])
        # Download the image
        img_data = rq.get(url).content
        # Put the image into the file
        with open("dribblephotos/" + str(index + 1) + '.jpg', 'wb+') as f:
            f.write(img_data)

print(links)