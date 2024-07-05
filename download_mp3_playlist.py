from pytube import Playlist
from download_mp3 import get_mp3

with open('list.txt', 'r') as f:
    for playlist_url in f:
        if playlist_url.strip(' \t\n\r') != '':
            ## Get urls of videos
            urls = Playlist(playlist_url)

            ## Get videos and convert to audios
            url_count = len(urls)
            for i in range(url_count):
                print("({}/{})".format(i+1, url_count))
                url = urls[i].strip(' \t\n\r')
                get_mp3(url)

