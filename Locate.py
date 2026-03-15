import requests

def my_custom_function(meme):
    url = "https://api.apileague.com/retrieve-random-meme?keywords={meme}"
    api_key = "b28334841b74464e895b70919752cda2"

    headers = {
        'x-api-key': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    print(my_custom_function())
"""
stuff = {
  "memes": [
    {
      "type": "image/jpeg",
      "description": "Meirl",
      "url": "https://preview.redd.it/c9yq2m399t3c1.jpg?width=640&crop=smart&auto=webp&s=25999ef88a05c5cf6f12eb3e7d7a10eaa51584c4"
    }
  ],
  "available": 578
}
print(stuff["memes"][0][url])#this gets url

"""
