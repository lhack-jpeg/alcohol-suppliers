import scrapy


class SuppliersSpider(scrapy.Spider):
    name = 'suppliers'
    
    start_urls = ['http://www.drinksguide.com.au/Suppliers/']

    def parse(self, response):
        urls =  response.xpath("//div[@id='Suppliers']/table/tbody/tr/td/a/@href").extract()
        for url in urls:
        	new_url = response.urljoin(url)
        	yield scrapy.Request(new_url, callback = self.parse_supplier)

    def parse_supplier(self, response):
    	products = response.xpath('//div[@class="section-content"]/ul/li/a/text()').extract()
    	brand_name = response.xpath("//div[@class='section-header']/h2/text()").extract_first()
    	street_address = response.xpath('//div[@class="section-content"]/div[@class="address left"]/fieldset/div[2]/text()').extract()
    	suburb = response.xpath('//div[@class="section-content"]/div[@class="address left"]/fieldset/div[3]/text()').extract()
    	telephone = response.xpath('//div[@class="section-content"]/div[@class="tels right"]/div/text()').extract_first()
    	yield{
    	"Brand Name": brand_name,
    	"products" : products,
    	"Street Address" : street_address,
    	"Suburb" : suburb
    	}

