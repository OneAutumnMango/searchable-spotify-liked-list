import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope='user-library-read'
))

results = sp.current_user_saved_tracks()
liked_songs = []

for item in results['items']:
    track = item['track']
    liked_songs.append(f"{track['artists'][0]['name']} – {track['name']}")

with open('liked_songs.txt', 'w') as file:
    for song in liked_songs:
        file.write(f"{song}\n")
        print(song)
