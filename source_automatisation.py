import klembord
import datetime
from bs4 import BeautifulSoup
import urllib.request as urllib

klembord.init()
url = ""

date = input("Enter date string (jour mois année) (leave blank for today): ")
if date == "":
    # Get today's date
    currDay = datetime.datetime.now().day
    currMonth = datetime.datetime.now().month
    currYear = datetime.datetime.now().year
    # Translate month number to french month name
    if currMonth == 1:
        month = "janvier"
    elif currMonth == 2:
        month = "février"
    elif currMonth == 3:
        month = "mars"
    elif currMonth == 4:
        month = "avril"
    elif currMonth == 5:
        month = "mai"
    elif currMonth == 6:
        month = "juin"
    elif currMonth == 7:
        month = "juillet"
    elif currMonth == 8:
        month = "août"
    elif currMonth == 9:
        month = "septembre"
    elif currMonth == 10:
        month = "octobre"
    elif currMonth == 11:
        month = "novembre"
    elif currMonth == 12:
        month = "décembre"
    else:
        month = "mois invalide"

    date = str(currDay) + " " + month + " " + str(currYear)

while url != "exit" or url != "stop" or url != "quit":
    url = input("\nEnter site link : ")

    if url != "exit" or url != "stop" or url != "quit":
        url2 = urllib.Request(url, headers={"User-Agent": "Mozilla/5.0"})

        soup = BeautifulSoup(urllib.urlopen(url2), "lxml")

        title = "No title"
        if soup.title is not None:
            title = soup.title.string

        author = "s.a."
        if soup.find("meta", {"name": "author"}) is not None:
            author = soup.find("meta", {"name": "author"})["content"]
            author = author.split(" ")[1].upper() + ", " + author.split(" ")[0].capitalize()

        first_part = ". (Page consultée le " + date + "). "
        second_part = ", [En ligne]. Adresse URL : " + url

        # Set HTML formatted clipboard
        klembord.set_with_rich_text(author + first_part + title + second_part, author + first_part + '<i>' + title + '</i>' + second_part)

        print(author + first_part + title + second_part)

exit()
