import requests
from bs4 import BeautifulSoup


index = 0
URL = f"https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/discursos?b_start:int={index}"
extraction_class = 'tileContent'
content_class = ['summary', 'url']
tag_class = ['link-category']
PAGES = 7


class SpeechContent:
    def __init__(self, title, href, tags):
        self.tags = tags
        self.href = href
        self.title = title

    def __str__(self):
        return f"{self.title}"


def get_speeches():
    speeches = []
    for i in range(0, PAGES):
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        div_contents = soup.find_all('div', extraction_class)
        for div_content in div_contents:
            speech, tags = None, []
            link_contents = div_content.find_all('a')
            for link_content in link_contents:
                if link_content.get('class') == content_class:
                    speech = SpeechContent(title=link_content.text, href=link_content.get('href'), tags=[])
                if link_content.get('class') == tag_class:
                    tags.append(link_content.text)
            speech.tags = tags
            speeches.append(speech)
        index = i * 30
    return speeches

print(get_speeches())
