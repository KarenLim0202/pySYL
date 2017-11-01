import scrapy

class SpiderGit(scrapy.Spider):
    name="shiyanlougithub"

    @property
    def start_urls(self):
        url_tmpl="https://github.com/shiyanlou?page={}&tab=repositories"
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        lname=response.css('div.mb-1 a::text').extract()
        ltime=response.css('div.mt-2 relative-time::attr(datetime)').extract()
        print(lname[0],ltime[0])
        for n,t in zip(lname,ltime):
                yield{"name":n.strip(),"updata_time":t}

