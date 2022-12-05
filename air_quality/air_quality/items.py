# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AirQualityItem(scrapy.Item):
    # define the fields for your item here like:
    Rank = scrapy.Field()
    City = scrapy.Field()
    Year_2021 = scrapy.Field()
    Jan = scrapy.Field()
    Feb = scrapy.Field()
    Mar = scrapy.Field()
    Apr = scrapy.Field()
    May = scrapy.Field()
    Jun = scrapy.Field()
    Jul = scrapy.Field()
    Aug = scrapy.Field()
    Sep = scrapy.Field()
    Oct = scrapy.Field()
    Nov = scrapy.Field()
    Dec = scrapy.Field()
    Year_2020 = scrapy.Field()
    Year_2019 = scrapy.Field()
    Year_2018 = scrapy.Field()
    Year_2017 = scrapy.Field()
    pass
