# dimibob-py
한국디지털미디어고등학교 급식 데이터 크롤러

## 설치
```bash
$ pip install dimibob
```

## 사용법
```python
>>> from pprint import pprint
>>> from dimibob import Dimibob
>>> pprint(Dimibob(year=1234).fetch(15)[0])
{'added': '2018-01-26',
 'breakfast': '소고기무국/쌀밥/비엔나볶음/새우크런치/미역줄기볶음/포기김치/파인애플/한국야쿠르트',
 'date': '1234-04-08',
 'dinner': '오삼불고기덮밥/상추채/배추된장국/부추전/호박느타리버섯/콩나물무침/포기김치/오렌지',
 'lunch': '치즈돈가스/김치볶음밥/양송이스프/감자볼/꼬들단무지/후르츠샐러드/포기김치/바나나',
 'snack': '초코머핀/딸기우유'}
```
