import os, sys, json, re
sys.path.insert(0, '/home/jirif/github_tools/pirate')
from tools.corebay_scraper import CorebayScraper
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv('/home/jirif/github_tools/pirate/.env')
scraper = CorebayScraper(os.environ['COREBAY_USER'], os.environ['COREBAY_PASS'])
if scraper.login():
    print("Logged in!")
    r = scraper.session.get('https://www.corebay.co/NON-SCENE-RELEASE-f175')
    
    print("Ekeaze in raw HTML?", "Ekeaze" in r.text)
    print("Azinaya in raw HTML?", "Azinaya" in r.text)
    
    soup = BeautifulSoup(r.text, 'lxml')
    links = soup.find_all('a', string=re.compile('Ekeaze', re.I))
    for link in links:
        print("Found link:", link.get('href'), link.text)
else:
    print("Login failed")
