import os, sys, json, re
sys.path.insert(0, '/home/jirif/github_tools/pirate')
from tools.corebay_scraper import CorebayScraper
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv('/home/jirif/github_tools/pirate/.env')
scraper = CorebayScraper(os.environ['COREBAY_USER'], os.environ['COREBAY_PASS'])
if scraper.login():
    data = {
        'keywords': 'Ekeaze',
        'terms': 'exact',
        'name_search': '',
        'forum': '-1',
        'search_in': 'all',
        'sort_by': '0',
        'sort_dir': 'DESC',
        'show_results': 'topics',
        'submit': 'Search'
    }
    r = scraper.session.post('https://www.corebay.co/search.php', data=data)
    soup = BeautifulSoup(r.text, 'lxml')
    links = soup.find_all('a', class_='topictitle')
    if links:
        for link in links:
            print("Found:", link.get('href'), link.text)
    else:
        print("No exact match. Trying Azinaya.")
        data['keywords'] = 'Azinaya'
        r = scraper.session.post('https://www.corebay.co/search.php', data=data)
        soup = BeautifulSoup(r.text, 'lxml')
        for link in soup.find_all('a', class_='topictitle'):
            print("Found:", link.get('href'), link.text)
