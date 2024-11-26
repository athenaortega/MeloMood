import spotipy
from dotenv import load_dotenv
from flask import Flask, redirect, session, url_for
from spotipy.oauth2 import SpotifyOAuth
from spotipy import cache_handler
import os

app = Flask(__name__)

load_dotenv()

# Set your Spotify API credentials as environment variables, it will pick by spotipy API
client_id = os.getenv("CLIENT_ID")
if client_id is not None:
    os.environ["SPOTIPY_CLIENT_ID"] = client_id
else:
    print("CLIENT_ID environment variable is not set.")

client_secret = os.getenv("CLIENT_SECRET")
if client_secret is not None:
    os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret
else:
    print("CLIENT_SECRET environment variable is not set.")

# Set your redirect URI
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:3000/callback"

# Define the required OAuth scope
oAuthscope = "playlist-read-private"

# Initialize the cache handler and auth manager for Spotipy
Sp_Cache = cache_handler.CacheFileHandler()
auth_manager = spotipy.SpotifyOAuth(scope=oAuthscope, cache_handler=Sp_Cache)
sp_oauth = spotipy.Spotify(auth_manager=auth_manager)

# Ensure the Flask application has a secret key for secure sessions
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return redirect(url_for('get_playlists'))

@app.route('/get_playlists')
def get_playlists():
    playlists = sp_oauth.current_user_playlists()
    playlists_info = [(pl['name'], pl['external_urls']['spotify']) for pl in playlists['items']]
    playlists_html = '<br>'.join([f'{name}: {url}' for name, url in playlists_info])
    return playlists_html

@app.route('/logout')
def logout():
    # Clearing the Flask session for logging out
    session.clear()
    return redirect(url_for('home'))

# run flask app when file is run
if __name__ == '__main__':
    app.run(debug=True)
