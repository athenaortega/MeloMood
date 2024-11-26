
"""
First, import the relevant packages needed for this project.
My project relies upon spotipy, which is a python library for the Spotify Web API.
Import all the relevant packages in order to run Flask.
Import SpotifyOAuth, which creates an access token that allows authenticated calls to the Spotify API


Second, import Firebase_admin to access Firebase API for journal entries to be saved in a secure database.
"""
import spotipy
from flask import app, redirect, request, render_template, Flask
from spotipy.oauth2 import SpotifyOAuth

import firebase_admin
from firebase_admin import credentials, firestore



"""
Create an instance of the Flask app
Initialize a spotipy object which has access to the Spotify Web API.
Ensure authentication by using SpotifyOAuth.
"""
app = Flask(__name__)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="0b6e6578e5e543b299468a540559e166",
                                               client_secret="976090293a504f5f8b328f89dbf61b76", #NEED TO CONCEAL INFO?
                                               redirect_uri="http://localhost:5000/callback",    #IN SEPARATE FILE?
                                               scope="user-library-read"))

"""
Create Flask web app route for what occurs when user reaches the /login URL of MeloMood
"""

#Sources:
#https://stackoverflow.com/questions/78440381/spotipy-accessing-users-playlist-access-to-localhost-was-denied-http-error-4
#https://stackoverflow.com/questions/25711711/spotipy-authorization-code-flow
@app.route("/login")
def login():
    auth_url = sp.auth_manager.get_authorize_url()
    return redirect(auth_url)

"""
Create Flask web app route for what occurs when user reaches the /callback URL of MeloMood
Verify that access token has been obtained.
Verify that user information has been obtained.
Obtain 10 of the user's recently played tracks and display name of song, name of artist, and time played.
Notify user whether authentication has failed or not.

"""


@app.route("/callback")
def callback():
    access_token = None
    token_info = spotipy.get_cached_token()

    if token_info:
        print("Found cached token!")
        access_token = token_info['access_token']
    else:
        code = request.args.get('code')
        if code:
            print("Found auth code! Attempting to get a valid access token...")
            token_info = sp.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print("Access token available! Attempting to get user information...")
        sp = spotipy.Spotify(auth=access_token)


        results = sp.current_user_recently_played(limit=10)
        print("Recently played tracks: ", results)


        tracks = [
            {
                "name": item['track']['name'],
                "artist": item['track']['artists'][0]['name'],
                "played_at": item['played_at']
            }
            for item in results.get('items', [])
        ]
        return render_template('listening.html', tracks=tracks)

    return "Access token not found. Authorization failed."

"""
Create Flask web app route for the root URL. 
This route will render the template of the homepage.

"""
@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)






"""
Setting up Firebase API 

"""

cred = credentials.Certificate("/Users/athenaortega/Documents/HCDE310/Final-Project/venv/melomood-260d9-firebase-adminsdk-qu73i-bf63f51df9.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/")
def index():
    return "Firebase Flask App is Running"

"""
NEXT STEPS:

    1. For each track that is displayed:
        -> Create a text input box beside the information of track.
        -> Allow the user to save their journal reflection.
    2. Save Reflections to Firebase:
        -> Create function to capture user's reflection text and the song information (title, artist, time played)
        -> Send POST request to Firebase (send it to endpoint that contains captured data)
    3. Retrieve Reflections from Firebase:
        -> When displaying list of songs, must send GET request to Firebase to retrieve saved reflections
        -> If there are already reflections that exist for a song, allow for the reflection to be displayed next to track
            as read only text.
        
 
"""
