#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def scraper():
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results  = soup.find_all("h2", class_= "title is-5")

    for title in results:
        print(title.text.strip())

if __name__ == "__main__":
    scraper()