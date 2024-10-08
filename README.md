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

## Setup

1. Create a `.env` file in the root of your project:

    ```bash
    touch .env
    ```

2. Add your Spotify credentials to the `.env` file:

    ```plaintext
    SPOTIFY_CLIENT_ID=your_client_id
    SPOTIFY_CLIENT_SECRET=your_client_secret
    SPOTIFY_ACCESS_TOKEN=your_access_token
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the project:

    ```bash
    pytest tests/
    ```

## License
MIT
