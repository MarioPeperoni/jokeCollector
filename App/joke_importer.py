import requests
from bs4 import BeautifulSoup


def import_jokes(fr, to):
    with open('jokes.joke', 'w') as file:
        counter = 0
        for i in range(fr, to):
            url = "https://smieszne-kawaly.pl/kawal/" + str(i)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.find("div", {"class": "entry clear"})
            if text is not None:
                text = text.get_text()
                file.write(text + "|")
                counter += 1
                print(str(i) + ". Added to dictionary")
            else:
                print(str(i) + ". Skipped")
        print("Imported " + str(counter) + " jokes.joke")


if __name__ == "__main__":
    import_jokes(0, 800)
