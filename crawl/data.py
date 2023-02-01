import requests
import datetime
import random
import time
from bs4 import BeautifulSoup
from datetime import date


class Crawler:

    def __init__(self):
        self.start_url = "https://www.iloom.com/product/item.do?categoryNo=607&pageNo="
        self.visited_list = set()
        self.to_visit = set()

    def parse_html(self, url):
        if url in self.visited_list:
            return

        soup = None
        try:
            response = requests.get(url)

            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, "html.parser")
                self.visited_list.add(url)
            else:
                print('response.status_code:{}'.format(response.status_code))
                print("url을 확인 하세요")
        except Exception as e:
            print("*" * 40)
            print("parse_html Exception: {}".format(e))
            print("*" * 40)

        return soup

    def find_product_list(self, soup):
        if soup:
            pro_list = soup.select("div.pro_list>div>ul.proUl>li")
            product_cd_list = []
            for product in pro_list:
                product_cd = product.get("data-product-cd")
                product_cd_list.append(product_cd)
            return product_cd_list

    def product_info_parse(self, product_cd):
        url = "https://www.iloom.com/product/detail.do?productCd=" + product_cd
        product_detail = self.parse_html(url)

        # 상품 상세 정보 박스 --------------------------------
        box_product_info = product_detail.select_one("div.box_productInfo")
        # 상품명
        product_name = box_product_info.select_one("div.productNm").text.strip()

        # 상품 가격
        product_price_txt = box_product_info.select_one("div.price").text.strip()[:-1]
        product_price = int(product_price_txt.replace(",", ""))

        # 상품 색깔 옵션
        select_color = box_product_info.select("select.select_color > option")
        colors = []
        for product in select_color:
            color = product.get("data-product-col")
            if color:
                colors.append(color)
        # 상품 상세 정보 박스 END --------------------------------

        # 상품 이미지 박스 -----------------------------
        box_product_gal = product_detail.select_one("ul.box_productGalery_S")
        img_src_list = box_product_gal.select("li>img")
        img_url_list = []
        for img_src in img_src_list:
            file_num = str(random.randint(1, 100000))
            while len(file_num) < 5:
                file_num = "0" + file_num
            file_name = product_cd + "_" + file_num + "_" + str(round(time.time())) + ".png"
            img_url = img_src.get("src")
            if img_url:
                # img_url_list.append(img_url)
                f = open('/Users/koodoyoon/Desktop/crawl_image/{}'.format(file_name), 'wb')
                f.write(requests.get(img_url).content)
                f.close()

        print()
        print("-" * 40)
        print(product_name + " " + str(product_price) + " " + str(colors))
        # print(img_url_list)

    def find_url_to_visit(self, soup):
        # print(soup.select("div.list_cnt > ul.list_cnt_ul > li"))
        print(soup.select("div.list_cnt"))

    def investigate_page(self, url, page_no):
        # 페이지 정보 가져오기
        soup = self.parse_html(url + str(page_no))
        if not soup:
            return

        # 현재 페이지 속에 있는 상품 코드들
        product_cd_list = self.find_product_list(soup)
        if not product_cd_list:
            return
        print(product_cd_list)

        # 코드들로 상품 상세 페이지로 가서 상세 정보 가져오기
        for product_cd in product_cd_list:
            self.product_info_parse(product_cd)

        # 현재 페이지에서 방문해야될 url 찾기
        self.investigate_page(url, page_no + 1)

    def run(self):
        self.investigate_page(self.start_url, 1)


def main():
    if __name__ == "__main__":
        crawler = Crawler()
        crawler.run()


main()
