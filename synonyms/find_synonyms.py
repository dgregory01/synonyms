from bs4 import BeautifulSoup
from more_itertools import take

import synonyms.http.client as http_client

THESAURUS_BASE_URL = 'https://www.thesaurus.com/browse/'


class FindSynonyms:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_synonyms(self, word, n: int = 100):
        url = FindSynonyms._construct_url(self.base_url, word)
        html_text = http_client.get_html(url)

        soup = FindSynonyms._to_soup(html_text)

        meanings = soup.find(id='meanings')
        synonyms = map(lambda node: str.strip(node.text), meanings.find_all('a'))
        top_n_synonyms = take(n, synonyms)
        return list(top_n_synonyms)

    @staticmethod
    def _construct_url(base_url, word):
        return base_url + word

    @staticmethod
    def _to_soup(html_text: str):
        return BeautifulSoup(html_text, 'html.parser')
