import lyricsgenius
import json
import os

ARTISTS = [
  "Eagles",
  "The Beatles",
  "The Who",
  "The Rolling Stones",
  "The Monkees",
  "The Doors",
  "Electric Light Orchestra",
  "Led Zeppelin",
  "Bob Dylan",
  "Jethro Tull",
  "The Doobie Brothers",
  "Fleetwood Mac",
  "Paul Simon and Art Garfunkel",
  "Pink Floyd",
  "Grateful Dead",
  "Jefferson Airplane",
  "David Bowie",
  "Ramones",
  "Lynyrd Skynyrd",
  "Rush",
  "ZZ Top",
  "Guns N' Roses",
  "Cream",
  "Aerosmith",
  "AC/DC",
  "The Clash",
  "The Kinks",
  "Creedence Clearwater Revival",
  "Bruce Springsteen",
  "Van Halen",
]

with open("secrets.json", "r") as fh:
    secrets = json.load(fh)

genius = lyricsgenius.Genius(secrets['genius']['access_token'])

LYRICS_DIR = "lyrics"


def download_artist(artist_name):
    try:
        artist = genius.search_artist(artist_name, max_songs=50, sort="popularity")
        for song in artist.songs:
            filename = f"{song.title} - {artist.name}.txt".replace("/", "")
            with open(f"{LYRICS_DIR}/{filename}", "w") as fh:
                fh.write(song.lyrics)
    except TypeError:  # lyricsgenius throws a TypeError if there's a network problem smh
        download_artist(artist_name)  # just retry...


if __name__ == "__main__":
    if not os.path.exists(LYRICS_DIR):
        os.makedirs(LYRICS_DIR)

    for artist_name in ARTISTS:
        download_artist(artist_name)
