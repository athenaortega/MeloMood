from flask import Flask, render_template, request
import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import keys

app = Flask(__name__)

SPOTIFY_CLIENT_ID = keys.SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET = keys.SPOTIFY_CLIENT_SECRET


def get_spotify_client():
    client_credentials_manager = SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    )
    sp = Spotify(client_credentials_manager=client_credentials_manager)
    return sp

CAT_FACTS_API_URL = "https://catfact.ninja/fact"

def safe_get(url, params=None):
    try:
        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        print(f"Error occurred: {e}")
        return None



def get_cat_facts(limit=5):
    facts = []
    for _ in range(limit): #learned about for _ from https://stackoverflow.com/questions/66425508/what-is-the-meaning-of-for-in-range

        data = safe_get(CAT_FACTS_API_URL)
        if data and 'fact' in data:
            facts.append(data['fact'])
        else:
            print("No cat facts found.")
    return facts

@app.route('/', methods=['GET', 'POST'])
def index():
    cat_facts = get_cat_facts(limit=5)
    playlist_embed_url = None

    if request.method == 'POST':
        playlist_keyword = request.form.get('playlist')


        sp = get_spotify_client()
        result = sp.search(q=playlist_keyword, type="playlist", limit=1)

        if result['playlists']['items']:
            playlist = result['playlists']['items'][0]
            playlist_url = playlist['external_urls']['spotify']
            playlist_embed_url = f"https://open.spotify.com/embed/playlist/{playlist['id']}"


    return render_template('index.html', cat_facts=cat_facts, playlist_embed_url=playlist_embed_url)

if __name__ == '__main__':
    app.run(debug=True)



