import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import lyricsgenius

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
GENIUS_ACCESS_TOKEN = os.getenv('GENIUS_ACCESS_TOKEN')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope='user-library-read'
))
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

_next=True
offset=0
with open('lyrics.txt', 'a', encoding='utf-8') as f:
    while _next: 
        results = sp.current_user_saved_tracks(limit=50, offset=offset)
        offset+=50
        _next=results['next']
        
        for item in results['items']:
            track = item['track']
            artist = genius.search_song(track['name'], track['artists'][0]['name'])
    
            if artist:
                f.write(artist.lyrics + '\n\n---------------------------------------------------------------------\n')
            else:
                print(f"Lyrics not found for {track['name']} by {track['artists'][0]['name']}")
