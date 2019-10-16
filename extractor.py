import requests
from bs4 import BeautifulSoup

extraction_class = 'tileContent'
content_class = ['summary', 'url']
tag_class = ['link-category']
PAGES = 7


class SpeechContent:
    def __init__(self, title, href, tags, content=""):
        self.tags = tags
        self.href = href
        self.title = title
        self.content = content

    def __str__(self):
        return f"{self.title}"


def get_speech_content(speech):
    response = requests.get(speech.href)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = list(map(lambda p: p.get_text().replace('\xa0', ''), soup.find_all('p')))
    speech.content = " ".join(paragraphs)
    return speech


def get_speeches():
    speeches = []
    for i in range(0, PAGES):
        index = i * 30
        URL = f"https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/discursos?b_start:int={index}"
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
            speech = get_speech_content(speech)
            speeches.append(speech)
            print(speech.title)
    return speeches


def get_corpus():
    corpus = []
    for i in range(0, PAGES):
        index = i * 30
        URL = f"https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/discursos?b_start:int={index}"
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        div_contents = soup.find_all('div', extraction_class)
        for div_content in div_contents:
            speech, tags = None, []
            link_contents = div_content.find_all('a')
            for link_content in link_contents:
                if link_content.get('class') == content_class:
                    speech = SpeechContent(title=link_content.text, href=link_content.get('href'), tags=[])
            speech = get_speech_content(speech)
            corpus.append(speech.content)
    return corpus