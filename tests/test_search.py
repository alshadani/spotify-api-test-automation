'''Test if can search for a song with spotify API'''

from dotenv import load_dotenv
import requests

import os

# Load environment variables from .env file
load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
access_token = os.getenv("SPOTIFY_ACCESS_TOKEN")

def test_search_song():
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get("https://api.spotify.com/v1/search", headers=headers, params={
        "q": "Coldplay",
        "type": "track"
    })
    assert response.status_code == 200
    results = response.json()
    assert 'tracks' in results
    assert len(results['tracks']['items']) > 0