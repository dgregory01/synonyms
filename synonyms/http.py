import requests
from bs4 import BeautifulSoup


def http_get(url: str) -> str:
    """
    Get the HTML at a given url.
    """
    url = requests.get(url)
    html = url.text
    return html


def to_soup(html_str: str):
    """
    Extract the text from a given html path.
    """
    soup = BeautifulSoup(html_str, 'html.parser')
    return soup


def find_meanings(word: str):
    url = 'https://www.thesaurus.com/browse/' + word
    text = http_get(url)
    soup = to_soup(text)
    meanings = soup.find(id='meanings')
    return list(map(lambda meaning: meaning.text, meanings.find_all('a')))
