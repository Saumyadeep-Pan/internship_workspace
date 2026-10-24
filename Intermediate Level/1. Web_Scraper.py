import scrapy
from scrapy.crawler import CrawlerProcess


class QuoteSpider(scrapy.Spider):
    name = "quote_scraper"
    start_urls = ["https://toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


if __name__ == "__main__":
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "quotes_output.json": {
                    "format": "json",
                    "encoding": "utf8",
                    "indent": 4,
                },
            },
            "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "ROBOTSTXT_OBEY": True,
            "CONCURRENT_REQUESTS": 16,
            "DOWNLOAD_DELAY": 1,
        }
    )

    process.crawl(QuoteSpider)
    process.start()
