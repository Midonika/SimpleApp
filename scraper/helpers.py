from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


class Helper:

    @staticmethod
    def get_html_and_meta_tags(url):
        html = urlopen(url)
        parsed_html = BeautifulSoup(html, 'html')
        meta = parsed_html.head.find('meta', attrs={"name": "keywords"})

        return parsed_html, meta

    @staticmethod
    def get_keywords(meta):
        keywords = []
        if meta is not None:
            for tag in meta.attrs:
                if tag == 'content':
                    keywords = (meta.attrs[tag].replace(" ", "")).split(",")

        return keywords

    @staticmethod
    def count_keywords_in_html(html, keywords):
        result = {}
        html_to_str = html.body.__str__()
        for keyword in keywords:
            words = [m.start() for m in re.finditer(keyword, html_to_str, re.IGNORECASE)]
            result[keyword] = len(words)

        return result
