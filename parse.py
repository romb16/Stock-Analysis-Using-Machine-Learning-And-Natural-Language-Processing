from bs4 import BeautifulSoup
import requests


# This class serves to provide methods for parsing url data and processing
class URLParser:

    # This method parses the given url into text for processing
    @staticmethod
    def parseurl(url):
        html_page = requests.get(url)
        html_parse = BeautifulSoup(html_page.text, "html.parser")

        for paragraph in html_parse.select("p"):
            print(paragraph.getText())
            print()
