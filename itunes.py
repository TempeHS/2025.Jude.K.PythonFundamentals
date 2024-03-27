import requests
import sys

if len(sys.argv) != 2:
    sys.exit()


response = requests.get(
    "https://itunes.apples.com/search?entity=songs&limit=1&term=" + sys.argv[1]
)
print(response.json())
