import requests
import json
import time
client_id = "ALECV5CBBEHRRKTIQ5ZV143YEXOH3SBLAMU54SPHKGZI1ZKE"
client_secret = "3JX3NRGRS2P0KE0NSKPTMCOZOY4MWUU4M3G33BO4XTRJ15SM"
date = "20190407"


start = time.time()

terms = ["pizza", "tacos", "ice cream", "italian", "chinese", "korean"]
for term in terms:
    url = "https://api.foursquare.com/v2/venues/search"
    params = {"ll": "40.7,-74", "query": "tacos", 
            "client_id": client_id, "client_secret": client_secret, "v": date}
    response = requests.get(url, params = params)
    dictionary = response.json()
    json_object = json.dumps(dictionary, indent=4)
    # change the code so that we can make requests to 

    with open("sample.json", "a") as outfile:
        outfile.write(json_object)

end = time.time()
print(end - start)