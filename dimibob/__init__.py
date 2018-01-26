#!/usr/bin/python3
# \(>__<)/ encoding: utf-8

from re import match, sub
from datetime import datetime
from requests import get
from bs4 import BeautifulSoup as bs

URL = 'https://www.dimigo.hs.kr/index.php?mid=school_cafeteria&page='
KEYS = {'조': 'breakfast', '중': 'lunch', '석': 'dinner', '간': 'snack'}


def strip(str):
    return sub(r'\s*[/*]\s*', '/', str)


def fmt(date):
    return date and date.strftime('%Y-%m-%d')


class Dimibob:
    def __init__(self, url=URL, year=datetime.now().year):
        self.cache = {}
        self.url = url
        self.year = year

    def soup(self, url, cache_disabled=False):
        if cache_disabled or url not in self.cache:
            self.cache[url] = bs(get(url).text, 'html.parser')

        return self.cache[url]

    def fetch(self, page=1):
        return list(filter(None, map(self.parse, self.list_articles(page))))

    def list_articles(self, page):
        soup = self.soup(self.url + str(page), True)
        return soup.select('#dimigo_post_cell_2 .title a')

    def parse(self, article):
        date = self.check_article_date(article)
        return date and self.write_dates(date, self.fetch_meals(article))

    def check_article_date(self, article):
        m = match(r'(\d\d?)월 (\d\d?)일 식단입니다', article.get_text())
        return m and datetime(self.year, int(m.group(1)), int(m.group(2)))

    def fetch_meals(self, article):
        ps = self.soup(article.get('href')).select('#siDoc .xe_content p')
        ms = [match(r'^([조중석간])식\s*:\s*(.*)$', p.get_text()) for p in ps]
        return {KEYS[m.group(1)]: strip(m.group(2)) for m in ms if m}

    def write_dates(self, date, meals):
        return dict(meals, **{'date': fmt(date), 'added': fmt(datetime.now())})


if __name__ == '__main__':
    print(Dimibob(year=2018).fetch(page=2))
