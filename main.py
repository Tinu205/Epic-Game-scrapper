from bs4 import BeautifulSoup
import requests
import json

link = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"

response = requests.get(link)

soup = BeautifulSoup(response.content, "lxml")
#Soup returns json values in the form of string so converting string back to json
js = json.loads(soup.text)
#selecting the needed dict
game_list= js["data"]["Catalog"]["searchStore"]["elements"]
# for some weird reason return value is string so making it as dict
for game in game_list:
    game_name = game["title"]
    game_des = game["description"]
    #avail = game['effectiveDate']
    print(f"Name -> {game_name}\nDescription -> {game_des}\n")
