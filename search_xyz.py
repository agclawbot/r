import os, sys, json, re
sys.path.insert(0, '/home/jirif/github_tools/pirate')
from tools.wfxyz_scraper import WFXYZScraper
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv('/home/jirif/github_tools/pirate/.env')
scraper = WFXYZScraper(os.environ['WFXYZ_USER'], os.environ['WFXYZ_PASS'])
if scraper.login():
    r = scraper.session.get('http://www.warforum.xyz/viewforum.php?f=48') # music/mluvene slovo usually
    print("Ekeaze in wfxyz?", "Ekeaze" in r.text)
    
