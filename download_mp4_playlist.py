from pytube import Playlist
from download_mp4 import get_mp4

with open('list.txt', 'r') as f:
    fail_urls = []
    for playlist_url in f:
        if playlist_url.strip(' \t\n\r') != '':
            ## Get urls of videos
            urls = Playlist(playlist_url)

            ## Get videos and convert to audios
            url_count = len(urls)
            for i in range(url_count):
                print("({}/{})".format(i+1, url_count))
                url = urls[i].strip(' \t\n\r')
                try:
                    get_mp4(url)
                except Exception as err:
                    print(err)
                    fail_urls.append(url)

## Record fail urls
with open('fail_urls.txt', 'w') as f:
    for url in fail_urls:
        f.write(url + '\n')

