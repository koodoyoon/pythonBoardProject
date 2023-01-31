import requests
from bs4 import BeautifulSoup

web_site = requests.get("~")
web_html = BeautifulSoup(web_site.text, 'html.parser')


def main():
    pass


main()
