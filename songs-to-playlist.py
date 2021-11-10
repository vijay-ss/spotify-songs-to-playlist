import json
import pandas as pd
import requests

from secrets import PLAYLIST_ID, RECOMMEND_CSV

# prep uri format for json post request
df = pd.read_csv(RECOMMEND_CSV)
df["track_id"] = 'spotify:track:' +  df["track_id"]
df = df.sample(frac=1) # shuffle the order of songs

csv_list = df["track_id"].to_list()

headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {token}".format(token = a.spotify_access_token)
        }

request_body = json.dumps({"uris": csv_list[0:100]}) # Spotify only accepts 100 songs at a time -_-

# In case I need to delete songs in the future
# https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-tracks-playlist
#delete_query="https://api.spotify.com/v1/playlists/{playlist_id}/tracks".format(playlist_id = PLAYLIST_ID)
#response_del = requests.delete(url=delete_query, headers = headers, data = request_body)
#print(response_del.status_code)

# Add items to playlist
# https://developer.spotify.com/documentation/web-api/reference/#/operations/add-tracks-to-playlist
post_query = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks".format(playlist_id = PLAYLIST_ID)

response = requests.post(url=post_query, headers=headers, data=request_body)
response_json = response.json()
print(response.status_code)