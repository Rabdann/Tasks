import requests
from bs4 import BeautifulSoup


def html_parser() -> str:
    url = "https://greenatom.ru/"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.4951.67 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    response = requests.get(url, headers=headers)
    page_content = response.content

    soup = BeautifulSoup(page_content, "html.parser")

    tags = soup.find_all()

    total_tag_count = len(tags)

    tag_with_attr = 0
    for tag in tags:
        if tag.attrs:
            tag_with_attr += 1
    return f'Всего HTML-тегов на главной странице: {total_tag_count}'f'\nКоличество HTML-тегов с аттрибутами: {tag_with_attr}'


if __name__ == '__main__':
    print(html_parser())
