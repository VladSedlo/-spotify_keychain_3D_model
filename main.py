import utils
import requests


URL = "https://www.spotifycodes.com/downloadCode.php?uri=jpeg%2F000000%2Fwhite%2F640%2Fspotify%3Aalbum%3A4m2880jivSbbyEGAKfITCa"

if __name__ == '__main__':

    share_link = input("Enter link of song, album, artist or user: ")

    data = utils.get_link_data(share_link)

    if len(data) != 2:
        print("Something went wrong. Probably your fault.")
        exit(-1)

    code_URL = "https://www.spotifycodes.com/downloadCode.php?uri=jpeg%2F000000%2Fwhite%2F640%2Fspotify%3A" + data[0] + "%3A" + data[1]

    r = requests.get(code_URL)

    if not r.ok or not r.content:
        print("Something went wrong. Probably your fault.")
        exit(-1)

    with open(data[1]+".png", "wb") as fp:
        fp.write(r.content)


