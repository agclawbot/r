import os, sys, json, re
sys.path.insert(0, '/home/jirif/github_tools/pirate')
from tools.corebay_scraper import CorebayScraper
from dotenv import load_dotenv

load_dotenv('/home/jirif/github_tools/pirate/.env')
scraper = CorebayScraper(os.environ['COREBAY_USER'], os.environ['COREBAY_PASS'])
scraper.login()
r = scraper.session.get('https://www.corebay.co/NON-SCENE-RELEASE-f175')
with open('debug_corebay.html', 'w') as f:
    f.write(r.text)
print("Saved HTML")
