import requests
import re

def info_pull():
# will make the people list come from a text file or something similar so that I can easily access it anywhere
    people = ['alpharad', 'saltydkdan', 'mattkc']
    # people = ['alpharad']

    # open a file to save the new info into
    new_info = open('new_info.txt', 'w')


    for item in people:
        channel = "https://www.youtube.com/@" + item

        html = requests.get(channel + "/videos").text
        # info = re.search('(?<={"label":").*?(?="})', html).group()
        info = re.search('(?<={"label":").*?(?=by)', html).group()

        url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()

        # print(html)
        new_info.write(item.capitalize() + '\n')
        new_info.write(info + '\n')
        new_info.write(url + '\n')
        print(item.capitalize())
        print(info)
        print(url)

    new_info.close()

info_pull()