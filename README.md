# Spotify API Test Automation

This project automates testing of key Spotify API functionalities such as fetching playlists, retrieving track details, and searching for songs.

## Features
- Search for songs, albums, and artists using Spotify API.
- Fetch details of a specific track or playlist.
- Validate Spotify API authentication using OAuth.

## Requirements
- Python 3.11
- `requests` library

## Setup

1. Clone this repository.
2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain an access token from Spotify API and add it to your environment.

4. Run the automated tests:

    ```bash
    pytest test_spotify.py
    ```

## License
MIT
