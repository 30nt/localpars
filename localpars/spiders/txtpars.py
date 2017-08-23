import scrapy
from scrapy import Spider
import urllib.request as res
import csv


class SpiderClass(Spider):
    name = "txtpars"
    q = []
    with open(
            '/home/volodymyr/PycharmProjects/FirstMoney/localpars/Resurs/next.csv') as csvfile:  # считал из файла ссылки
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_q = "https://www.sec.gov" + row["next"]
            q.append(new_q)
    i = 1
    doc=[]
    for url in q:
        d='file:///home/volodymyr/PycharmProjects/FirstMoney/localpars/Resurs/{}myfile.txt'.format(i)
        doc.append(d)
        i += 1
    start_urls = doc

    def parse(self, response):
        print(response)