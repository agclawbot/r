import os, sys, json, re
sys.path.insert(0, '/home/jirif/github_tools/pirate')
from tools.corebay_scraper import CorebayScraper
from dotenv import load_dotenv

load_dotenv('/home/jirif/github_tools/pirate/.env')
scraper = CorebayScraper(os.environ['COREBAY_USER'], os.environ['COREBAY_PASS'])
if scraper.login():
    print("Logged in!")
    topics = scraper._get_topics()
    print(f"Total topics found across all pages: {len(topics)}")
    
    ekeaze = [t['title'] for t in topics if 'Ekeaze' in t['title']]
    print("Ekeaze found:", ekeaze)
    
    azinaya = [t['title'] for t in topics if 'Azinaya' in t['title']]
    print("Azinaya found:", azinaya)
