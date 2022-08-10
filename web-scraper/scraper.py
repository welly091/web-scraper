#https://en.wikipedia.org/wiki/American_Civil_War
import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    """
    Return the count of "citation needed" paragraphs.
    :param url: The website that is going to be scraped.
    :return: int
    """
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    all_p = soup.find_all("p")

    count = 0
    for p in all_p:
        for i in p.find_all("a", title="Wikipedia:Citation needed"):
            count +=1
    return count

def get_citations_needed_report(url):
    """
    Return a report string of each "citation needed" paragraph.
    :param url: The website that is going to be scraped.
    :return: string
    """
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    all_p = soup.find_all("p")

    spec_p = []
    for p in all_p:
        if p.find("a", title="Wikipedia:Citation needed"):
            for i in p.find_all("sup"):
                i.decompose()
            spec_p.append(p.text)

    report = ""
    for p in spec_p:
        report += f"{p}\n"
    return report

if __name__ == '__main__':
    URL = "https://en.wikipedia.org/wiki/Rome"
    print("There are",get_citations_needed_count(URL), "cititations needed.\n")
    print(get_citations_needed_report(URL))

