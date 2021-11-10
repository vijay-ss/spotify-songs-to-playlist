# Spotify-Songs-to-Playlist
A script which uploads recommended songs to a user playlist.

# Use Case
This script is part of a larger project, which pulls my daily listening history and generates song recommendations using a decision tree ML model. This is the final step, which is to upload those recommended songs to a playlist. This script can be automated to run daily, along with the existing ETL job.

This script leverages the official Spotify API which sends each song's track id within a post request.

Links to the existing projects:
- Spotify ETL job: https://github.com/vijay-ss/spotify-ETL
- Spotify recommender ML model: https://github.com/vijay-ss/spotify-recommender

# Instructions
1. Setup a Spotify token and user id.
2. Import tracks from the recommender model into a list format.
3. Submit the track id list within the post request.

# End Result

![](playlist.png)

# Limitations
- A limit of 100 tracks can be sent for any given post request
- No official way to delete all songs within a playlist using the API
