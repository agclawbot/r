import os, sys, json, re
sys.path.insert(0, '/home/jirif/github_tools/pirate')
from tools.wfxyz_scraper import WFXYZScraper
from dotenv import load_dotenv

load_dotenv('/home/jirif/github_tools/pirate/.env')
scraper = WFXYZScraper(os.environ['WFXYZ_USER'], os.environ['WFXYZ_PASS'])
if scraper.login():
    print("Logged in xyz")
    data = {'keywords': 'Azinaya', 'terms': 'all', 'submit': 'Search'}
    r = scraper.session.post('http://www.warforum.xyz/search.php', data=data)
    print("Azinaya in xyz?", "Azinaya" in r.text)
    
    data = {'keywords': 'Ekeaze', 'terms': 'all', 'submit': 'Search'}
    r = scraper.session.post('http://www.warforum.xyz/search.php', data=data)
    print("Ekeaze in xyz?", "Ekeaze" in r.text)
