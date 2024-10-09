from pytube import YouTube
import re
import os

def get_mp4(url):
    ## Create yt object
    yt = YouTube(url)

    ## Get video title and replace non-alphanumeric characters
    video_title = yt.title
    video_title = re.sub('[^\w\s\\u4e00-\\u9fff]+', ' ', video_title).strip('- \t')
    video_title = re.sub('\s+', ' ', video_title)
    print('Title: {}'.format(video_title))

    ## Download video
    print('Downloading {}'.format(url))
    yt.streams.filter().get_highest_resolution().download(filename=video_title+".mp4")

if __name__ == '__main__':
    ## Get urls of videos
    with open('list.txt', 'r') as f:
        urls = []
        for url in f:
            url = url.strip(' \t\n\r')
            if url != '':
                urls.append(url)

    ## Get videos
    fail_urls = []
    url_count = len(urls)
    for i in range(url_count):
        print("({}/{})".format(i+1, url_count))
        url = urls[i]
        try:
            get_mp4(url)
        except Exception as err:
            print(err)
            fail_urls.append(url)

    ## Record fail urls
    with open('fail_urls.txt', 'w') as f:
        for url in fail_urls:
            f.write(url + '\n')

