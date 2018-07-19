import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.archlinux.org/groups/x86_64/pro-audio/']

    def parse(self, response):
        table = response.xpath('//*[@id="content"]//table')
        for t in table.xpath('//tbody//tr'):
            request = response.follow(
                t.xpath(
                    'td[3]/a/@href').extract_first(), self.parse_package_page)
            td = {
                'Name': t.xpath('td[3]/a/text()').extract_first(),
                'Description': t.xpath('td[5]/text()').extract_first(),
            }
            request.meta['item'] = td

            yield request

    def parse_package_page(self, response):
        td = response.meta['item']
        td['ArchLink'] = response.url
        td['Link'] = response.xpath(
            '//td/a[@itemprop="url"]/text()').extract_first()

        yield td
