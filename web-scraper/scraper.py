#https://en.wikipedia.org/wiki/American_Civil_War
import requests
from bs4 import BeautifulSoup

def handle_citations_needed(url):
    """
    Takes in an URL to scrape.
    :param url: The website that is going to be scraped.
    :return: list, index 0 represents the count of "citation needed".
    """
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    all_p = soup.find_all("p")

    spec_p = []
    spec_p.append(0)
    for p in all_p:
        if p.find("a", title="Wikipedia:Citation needed"):
            spec_p[0] = spec_p[0] + 1
            for i in p.find_all("sup"):
                i.decompose()
            spec_p.append(p.text)

    return spec_p

def get_citations_needed_count(url):
    """
    Return the count of "citation needed" paragraphs.
    :param url: The website that is going to be scraped.
    :return: int
    """
    spec_p = handle_citations_needed(url)
    return spec_p[0]


def get_citations_needed_report(url):
    """
    Return a report string of each "citation needed" paragraph.
    :param url: The website that is going to be scraped.
    :return: string
    """
    spec_p = handle_citations_needed(url)
    report = ""
    for p in spec_p[1:]:
        report += f"{p}\n"
    return report

if __name__ == '__main__':
    URL = "https://en.wikipedia.org/wiki/American_Civil_War"
    print("There are",get_citations_needed_count(URL), "cititations needed.\n")
    print(get_citations_needed_report(URL))

