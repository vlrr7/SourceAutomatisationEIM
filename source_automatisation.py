import klembord
from bs4 import BeautifulSoup
import urllib.request as urllib

klembord.init()
url = ""

date = input("Enter date : ")

while (url != "stop"):
    url = input("\nEnter site link : ")

    if (url != "stop"):
        url2 = urllib.Request(url, headers={"User-Agent": "Mozilla/5.0"})

        soup = BeautifulSoup(urllib.urlopen(url2), features="lxml")

        title = "No title"
        if (soup.title != None):
            title = soup.title.string

        first_part = ". (Page consultée le " + date + "). "
        second_part = ", [En ligne]. Adresse URL : " + url

        # Set HTML formatted clipboard
        klembord.set_with_rich_text('', first_part+'<i>'+title+'</i>'+second_part)

        print(title)

exit()
