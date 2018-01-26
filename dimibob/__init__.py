from re import match, sub
from datetime import datetime
from requests import get
from bs4 import BeautifulSoup as bs

URL = 'http://dimigo.hs.kr/index.php?mid=school_cafeteria&page='
KEYS = {'조': 'breakfast', '중': 'lunch', '석': 'dinner', '간': 'snack'}


class Dimibob:
    def __init__(self, year=datetime.now().year):
        self.cache = {}
        self.year = year

    def get(self, url, cache_disabled=False):
        if cache_disabled or url not in self.cache:
            self.cache[url] = bs(get(url).text, 'html.parser')

        return self.cache[url]

    def get_articles(self, page):
        soup = self.get(URL + str(page), cache_disabled=True)
        return soup.select('#dimigo_post_cell_2 .title a')

    def get_date(self, article):
        m = match(r'(\d\d?)월 (\d\d?)일 식단입니다', article.get_text())
        return m and datetime(self.year, int(m.group(1)), int(m.group(2)))

    def strip(self, str):
        return sub(r'\s*/\s*|\*', '/', str)

    def get_meals(self, article):
        ps = self.get(article.get('href')).select('#siDoc .xe_content p')
        ms = [match(r'^([조중석간])식 ?: ?(.*)$', p.get_text()) for p in ps]
        return {KEYS[m.group(1)]: self.strip(m.group(2)) for m in ms if m}

    def parse(self, article):
        d = self.get_date(article)
        return d and dict(self.get_meals(article), date=d.strftime('%Y-%m-%d'))

    def fetch(self, page=1):
        return list(filter(None, map(self.parse, self.get_articles(page))))


if __name__ == '__main__':
    print(Dimibob().fetch())
