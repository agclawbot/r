import os, sys, re
sys.path.insert(0, '/home/jirif/github_tools/pirate')
from tools.corebay_scraper import CorebayScraper
from dotenv import load_dotenv
load_dotenv('/home/jirif/github_tools/pirate/.env')
scraper = CorebayScraper(os.environ['COREBAY_USER'], os.environ['COREBAY_PASS'])
if scraper.login():
    r = scraper.session.get('https://www.corebay.co/30-04-26KF-WS-TSR100PercentNIEMANDHZD-Niemand-Hzd-100Percent-Niemand-HZD-2026-WEB-FLAC-t1321300')
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, 'lxml')
    nav = soup.find('span', class_='nav')
    if nav:
        print(nav.get_text(separator=' -> '))
