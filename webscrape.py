
#refernece: http://stackoverflow.com/questions/36360606/stuck-on-web-scraping-code
# reference:
# https://www.reddit.com/r/learnpython/comments/4eaz7v/error_503_when_trying_to_get_info_off_amazon/


import requests, os, bs4
from bs4 import BeautifulSoup
#from urlparse import urljoin
url = 'http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/'

res = requests.get(url)


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()

#check for error?
#res.raise_for_status()

#scrape
#soup = bs4.BeautifulSoup(res.content)
#quiet version with arguement "lxml"
soup_txt = bs4.BeautifulSoup(res.content, "lxml")
#soup_txt = bs4.BeautifulSoup(res.text, 'html.parser')
#elems = soup_txt.select('#newOfferAccordionRow .header-price')

soup_txt = bs4.BeautifulSoup(res.text)
           

#if you know exactly what you want
#insert CSS object path
css_element_path_of_interest = '#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price'

elems = soup_txt.select(css_element_path_of_interest)
#results
elems[0].text.strip()



