# -*- coding: utf-8 -*-
import scrapy
from wikipedia_daily.items import articles

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']

    


    def parse(self, response):

        host = self.allowed_domains[0]

        for link in response.css(".featured_article_metadata > a"):
            yield articles(
                title = link.attrib.get("title"),
                link = f"https://{host}{link.attrib.get('href')}"
            )