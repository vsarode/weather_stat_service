from bs4 import BeautifulSoup
import urllib2
import re

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
site = "https://www.metoffice.gov.uk/climate/uk/summaries/datasets#yearOrdered"


def get_the_file_urls():
    req = urllib2.Request(site, headers=hdr)
    html_page = urllib2.urlopen(req)
    soup = BeautifulSoup(html_page)
    file_links = []
    for link in soup.findAll('a'):
        if '.txt' in str(link.get('href')) and (str(link.get('href'))).split('/')[-2:-1][0] == 'date':
            file_links.append(link.get('href'))
    return file_links


def populate_data(file_links):
    for url in file_links:
        response = urllib2.urlopen(url)
        html = response.read()
        print html
    