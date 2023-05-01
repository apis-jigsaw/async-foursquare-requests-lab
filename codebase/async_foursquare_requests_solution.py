import requests
import json
import time
import aiohttp
import asyncio

async def fetch(url, params = {}):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params = params) as response:
            return await response.text()


client_id = "ALECV5CBBEHRRKTIQ5ZV143YEXOH3SBLAMU54SPHKGZI1ZKE"
client_secret = "3JX3NRGRS2P0KE0NSKPTMCOZOY4MWUU4M3G33BO4XTRJ15SM"
date = "20190407"

start = time.time()

terms = ["pizza", "tacos", "ice cream", "italian", "chinese", "korean"]

async def get_venues_search(term):
    url = "https://api.foursquare.com/v2/venues/search"
    params = {"ll": "40.7,-74", "query": "tacos", 
            "client_id": client_id, "client_secret": client_secret, "v": date}
    response_text = await fetch(url, params = params)
    json_object = json.dumps(response_text, indent=4)
    # change the code so that we can make requests to 

    with open("sample.json", "a") as outfile:
        outfile.write(json_object)
    

def get_venues_searches(terms):
    return [get_venues_search(term) for term in terms]

async def main(terms):
    coros = get_venues_searches(terms)
    await asyncio.gather(*coros)

if __name__ == "__main__":
    asyncio.run(main(terms))

end = time.time()
print(end - start)