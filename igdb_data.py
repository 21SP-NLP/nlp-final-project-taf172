import requests
import json
from igdb.wrapper import IGDBWrapper

# Get credentials
f = open('credentials.txt')
credentials = json.load(f)
token = credentials['token']
id_ = credentials['id']

wrapper = IGDBWrapper(id_, token)

def getGames(offset):
# Returns 500 games from IGDB relative to offset

    offset = str(offset:int)

    byte_array = wrapper.api_request(
            'games',
            f'fields *; limit 500; offset {offset}; sort id;'
            )

    return json.loads(byte_array)

# Pull game data
offset = 0
limit = 150000
data = []

while offset < limit:
    batch = getGames(offset)

    if not batch:
        break
    else:
        data += batch
        offset += len(batch)

# Save to file
with open('game_data.txt', 'w') as outfile:
    json.dump(data, outfile)
