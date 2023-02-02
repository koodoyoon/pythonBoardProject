from django.test import TestCase

# Create your tests here.
import unittest
import datetime
import logging
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Crawling(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    # def test_naver_stock(self):
    #     codes = ['삼성전자', '005930', '현대차', '005380']
    #     for code in codes.keys():
    #         url = 'https://finance.naver.com/item/main.naver?code='
    #         url = url + str(codes[code])
    #
    #         response = requests.get(url)
    #         if 200 == response.status_code:
    #             html = response.text
    #             soup = BeautifulSoup(html, 'html.parser')
    #             price = soup.select_one('#chart_area div.rate_info div.today span.blind')
    #             print("today = {},{},{}".format(code, codes[code], price.getText()))
    #
    #         else:
    #             print('접속 오류')


    def call_slemdunk(self, url):
        response = requests.get(url)
        if 200 == response.status_code:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            score = soup.select('div.list_netizen_score em')
            review = soup.select('table tbody tr td.title')
            for i in range(0, len(score)):
                review_text = review[i].getText().split('\n')
                if len(review_text) > 2:
                    tmp_text = review_text[5]
                else:
                    tmp_text = review_text[0]

                print('평점, 감상평 = {}'.format(score[i].getText(), tmp_text))

        else:
            print('접속 오류')

    def test_slemdunk(self):
        url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=223800&target=after&page='
        for i in range(1, 4, 1):
            self.call_slemdunk(url + str(i))

    def test_cgv(self):
        # http://www.cgv.co.kr/movies/?lt=1&ft=0
        url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
        response = requests.get(url)
        print(response.status_code)
        if 200 == response.status_code:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.select('div.box-contents strong.title')
            reserve = soup.select('div.score strong.percent span')
            poster = soup.select('span.thumb-image img')

            for page in range(0, 7, 1):
                posterImg = poster[page]
                imgUrlPath = posterImg.get('src')
                print('title[page] = {}, 예매율 = {}, 이미지경로 = {}'
                      .format(title[page].getText(), reserve[page].getText(), imgUrlPath))

        else:
            print('접속 오류')

    @unittest.skip('테스트 연습')
    def test_weather(self):
        ''' 날씨 '''
        # https://weather.naver.com/today/09380114
        now = datetime.datetime.now()
        # yyyymmdd hh:mm
        newDate = now.strftime('%Y-%m-%d %H:%M:%S')
        print('-' * 35)
        print('newDate = {}'.format(newDate))
        print('-' * 35)

        naverWeatherUrl = 'https://weather.naver.com/today/09380114'
        html = urlopen(naverWeatherUrl)
        print(html)
        bsObject = BeautifulSoup(html, 'html.parser')
        tmpes = bsObject.find('strong', 'current')
        print('현재 은평구 진관동 = {}'.format(tmpes.getText()))
