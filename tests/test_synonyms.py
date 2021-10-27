from doubles import allow

# from synonyms.find_synonyms import FindSynonyms
from synonyms.find_synonyms import FindSynonyms


# from tests.utils import read_resource_to_str


def test_me():
    assert 5 == 5

# def test_list_synonyms_happy_path():
#     allow(mock_http_client).get.and_return(read_resource_to_str('synonyms.html'))
#
#     soup = FindSynonyms('any url')
#     synonyms = soup.get_synonyms('happy')
#
#     assert len(synonyms) == 48
#     assert synonyms[0] == 'cheerful'
#     assert synonyms[47] == 'walking on air'
