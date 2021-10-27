import pkgutil

import pytest
from doubles import allow

from synonyms.find_synonyms import FindSynonyms
from synonyms.find_synonyms import http_client as mock_http_client


# Test set up functions #

def _read_resource_to_str(resource: str):
    return pkgutil.get_data(__name__, 'resources/' + resource)


@pytest.fixture
def synonyms_html() -> str:
    """
    :return: stubbed HTML response from synonyms URL.
    :rtype Str
    """
    return _read_resource_to_str('synonyms.html')


# Unit tests below #

def test_list_synonyms_happy_path(synonyms_html):
    allow(mock_http_client).get_html.and_return(synonyms_html)

    soup = FindSynonyms('any url')
    synonyms = soup.get_synonyms('happy')

    assert len(synonyms) == 48
    assert synonyms[0] == 'cheerful'
    assert synonyms[47] == 'walking on air'


def test_list_synonyms_happy_path_with_top_n():
    allow(mock_http_client).get_html.and_return(_read_resource_to_str('synonyms.html'))

    soup = FindSynonyms('any url')
    synonyms = soup.get_synonyms('happy', 10)

    assert len(synonyms) == 10
    assert synonyms[0] == 'cheerful'
    assert synonyms[9] == 'lively'
