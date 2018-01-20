from bs4 import BeautifulSoup
import urllib2
import django

django.setup()

from weather_stat_service.db.weather_stat.models import WeatherInfo, Month

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


def make_the_db_entries(country, factor, year, data):
    weather_info_object = WeatherInfo.objects.create(country=country,
                                                     year=year,
                                                     factor=factor)
    month_values_objects = weather_info_object.month_values.all().order_by('id')
    for index, month in enumerate(month_values_objects):
        month.value = data[index]
        month.save()
    print "entry made for ", country, factor, year


def populate_data(file_links):
    for url in file_links:
        req = urllib2.Request(url, headers=hdr)
        response = list(urllib2.urlopen(req))[8:]
        country = url.split('/')[-1].split('.')[0]
        factory = url.split('/')[-3]
        for entry in response:
            list_of_values = map(lambda x: x.lstrip().rstrip(), entry.split('   '))
            year = list_of_values[0]
            make_the_db_entries(country, factory, year, list_of_values[1:-2])


if __name__ == "__main__":
    file_links = get_the_file_urls()
    print file_links
    populate_data(file_links)
