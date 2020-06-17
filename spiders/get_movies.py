# -*- coding: utf-8 -*-
import scrapy


class GetMoviesSpider(scrapy.Spider):
    name = 'get_movies'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/list/ls020043828/' ]

    def parse(self, response):
        movies = response.xpath('//div[@class="lister-item-content"]')
        for movie in movies:
            title = movie.xpath('.//h3/a/text()').get()
            year = movie.xpath('.//h3/span[@class="lister-item-year text-muted unbold"]/text()').get()

            yield{
                "Movie Name" : title,
                "Year" : year
            }

        link = response.xpath('//a[@class="flat-button lister-page-next next-page"]/@href').get()
        next_page = response.urljoin(link)

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

