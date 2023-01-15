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
    months = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    month = months[currMonth]
    # Concacenate everything
    date = str(currDay) + " " + month + " " + str(currYear)

while url != "exit" and url != "stop" and url != "quit":
    url = input("\nEnter site link : ")

    if url != "exit" and url != "stop" and url != "quit":
        try:
            url2 = urllib.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(urllib.urlopen(url2), "lxml")

            # Get title
            title = "No title"
            if soup.title is not None:
                title = soup.title.string

            # Get author
            author = "s.a."
            if soup.find("meta", {"name": "author"}) is not None:
                author = soup.find("meta", {"name": "author"})["content"]
                author = author.split(" ")[1].upper() + ", " + author.split(" ")[0].capitalize()

            first_part = ". (Page consultée le " + date + "). "
            second_part = ", [En ligne]. Adresse URL : " + url

            # Set HTML formatted clipboard
            klembord.set_with_rich_text(author + first_part + title + second_part, author + first_part + '<i>' + title + '</i>' + second_part)
            print(author + first_part + title + second_part)
            
        except:
            print("Invalid URL, type 'stop', 'exit', or 'quit' to stop the program")

        
exit()
