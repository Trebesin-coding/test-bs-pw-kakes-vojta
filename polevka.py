from bs4 import BeautifulSoup
import requests
import json

# from recept import *


def main():

    response = requests.get("https://souhrada.github.io/bsoup-exam/")

    soup = BeautifulSoup(response.content, "html.parser")
    ingredience = soup.select("h2")
    i = (
        ingredience[0].text,
        ingredience[1].text,
        ingredience[2].text,
        ingredience[3].text,
    )  # co je toto za syntax??
    print(i)

    json.load("recept.js")  # tohle načítá z jsonu - načítáte něco z jsonu?
    json.dump(i, "recept.js", indent=4)  # chybí syntax s with open


if __name__ == "__main__":
    main()
