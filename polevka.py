from bs4 import BeautifulSoup
import requests
import json
#from recept import *


def main():


    response = requests.get('https://souhrada.github.io/bsoup-exam/')

    soup = BeautifulSoup(response.content, "html.parser")
    ingredience = soup.select('h2')
    i = ingredience[0].text, ingredience[1].text, ingredience[2].text, ingredience[3].text
    print(i)

    json.load('recept.js')
    json.dump(i, 'recept.js', indent=4)
     


if __name__ == "__main__":
    main()