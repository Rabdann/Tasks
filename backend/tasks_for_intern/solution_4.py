import requests


def return_ip() -> str:
    url = 'https://ifconfig.me'
    response = requests.get(url=url)
    return f"Ваш IP - {response.text}"


if __name__ == '__main__':
    print(return_ip())
