# code:utf-8

from bs4 import BeautifulSoup
import urlparse
import re
  
class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_full_urls = set()
        
        # /view/123456.html
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            
            new_full_urls.add(new_full_url)
        
        return new_full_urls
        
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        res_data['url'] = page_url
        
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

    
    def parse(self, page_url, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser', from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
