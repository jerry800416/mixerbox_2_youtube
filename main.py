# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import json


# read mixerbox backup playlist
with open('./mixerbox_library.txt','r') as file:
    result = json.loads(file.read())


for i in result:
    # read my list
    if i['key'] == 'my_playlist':
        for playlist in i['content']:
            # this is playlist title
            playlist_name = (playlist['name'])
            with open('./'+playlist_name+'.txt','a') as f : 
                for playlist_music in playlist['content']:
                    # playlist content is url code
                    url = 'https://www.youtube.com/watch?v='+playlist_music
                    # pyquery
                    doc = pq(url=url,encoding='utf-8')
                    # get youtube title
                    title = doc('html head title').text()
                    try_again = 0
                    # can't catch youtube title 
                    while title == 'YouTube':
                        try_again += 1
                        if try_again <= 3 :
                            doc = pq(url=url)
                            title = doc('html head title').text()
                        else :
                            break
                    if title != 'YouTube':
                        # write youtube title to playlist txt
                        f.write(title[:-10]+'\r\n')               
    else :
        pass
