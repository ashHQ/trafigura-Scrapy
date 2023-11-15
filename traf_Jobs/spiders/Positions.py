from typing import Iterable
import scrapy
from scrapy.http import Request
from scrapy_playwright.page import PageMethod


class PositionsSpider(scrapy.Spider):
    name = "Positions"
    allowed_domains = ["traf.com"]
    start_urls = ["https://careers.trafigura.com/TrafiguraCareerSite/search"]

    def start_requests(self):
        yield scrapy.Request(
            self.start_urls[0],
            meta=dict(
                playwright=True,
                playwright_page_methods =[
                    PageMethod("wait_for_selector", 'section#results div[role="list"]')
                ]
            )
        )


    async def parse(self, response):
        for job in response.css('section#results div[role="list"] div[role="listitem"]'):
            yield{
                'title': job.css('a::text').get()
            }
