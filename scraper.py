#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def scraper():
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    job_element  = soup.find(id="ResultsContainer")

    for job_element in job_element:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip(), end="\n"*2)

if __name__ == "__main__":
    scraper()