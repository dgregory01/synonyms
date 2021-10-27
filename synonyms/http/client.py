import requests


def get_html(url: str) -> str:
    response = requests.get(url)
    html = response.text
    return html
