'''Test if I can successfully obtain token 
    for later usage'''


import requests 

def test_get_spotify_token():
    response = requests.post("https://accounts/spotify.com/api/token", {
        })
    assert response.status_code == 200 
    assert 'access_token' in response.json()
