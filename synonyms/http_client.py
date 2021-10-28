import requests


def get_html(url: str) -> str:
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return 'Failed with reason: ' + response.reason + ' (status code: ' + str(response.status_code) + ').'

    # success!
    html = response.text
    return html
