import requests as mock_requests
from doubles import allow

import synonyms.http_client as http_client


def test_get_html_happy_path():
    # set up
    mock_response = mock_requests.Response()

    allow(mock_requests).get.with_args('https://www.thesaurus.com/browse/happy') \
        .and_return(mock_response)

    # do nothing - there is no exception to raise
    allow(mock_response).raise_for_status.and_return(None)

    mock_html_response = '<!DOCTYPE html><html><body>' \
                         '<h1>My First Heading</h1><p>My first paragraph.</p>' \
                         '</body></html>'
    allow(mock_response).text.and_return(
        mock_html_response)

    # unit under test
    assert http_client.get_html('https://www.thesaurus.com/browse/happy') == mock_html_response


def test_get_html_throws_exception():
    url = 'https://www.my-favourite-thesauris.com/happy'

    # set up mock
    mock_response = mock_requests.Response()
    mock_response.url = url
    mock_response.reason = 'Internal Server Error'
    mock_response.status_code = 500

    allow(mock_requests).get.with_args(url).and_return(mock_response)

    # unit under test
    response_str = http_client.get_html(url)
    print(response_str)
    assert response_str.startswith('Failed with reason: Internal Server Error (status code: 500).')
