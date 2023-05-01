import requests
import json
import time
import aiohttp
import asyncio

start = time.time()

client_id = "ALECV5CBBEHRRKTIQ5ZV143YEXOH3SBLAMU54SPHKGZI1ZKE"
client_secret = "3JX3NRGRS2P0KE0NSKPTMCOZOY4MWUU4M3G33BO4XTRJ15SM"
date = "20190407"

async def fetch(url, params = {}):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params = params) as response:
            return await response.text()

terms = ["pizza", "tacos", "ice cream", "italian", "chinese", "korean"]

def get_venues_search(term):
    url = "https://api.foursquare.com/v2/venues/search"
    params = {"ll": "40.7,-74", "query": "tacos", 
            "client_id": client_id, "client_secret": client_secret, "v": date}
    

end = time.time()
print(end - start)