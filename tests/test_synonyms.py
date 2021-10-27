import pkgutil

from doubles import allow

from synonyms.find_synonyms import FindSynonyms
from synonyms.find_synonyms import http_client as mock_http_client


def _read_resource_to_str(resource: str):
    return pkgutil.get_data(__name__, 'resources/' + resource)


def test_list_synonyms_happy_path():
    allow(mock_http_client).get_html.and_return(_read_resource_to_str('synonyms.html'))

    soup = FindSynonyms('any url')
    synonyms = soup.get_synonyms('happy')

    assert len(synonyms) == 48
    assert synonyms[0] == 'cheerful'
    assert synonyms[47] == 'walking on air'
