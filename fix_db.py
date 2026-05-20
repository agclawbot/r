import os, sys, json, re
from datetime import datetime
sys.path.insert(0, '/home/jirif/github_tools/pirate')
from tools.corebay_scraper import CorebayScraper
from dotenv import load_dotenv

load_dotenv('/home/jirif/github_tools/pirate/.env')
scraper = CorebayScraper(os.environ['COREBAY_USER'], os.environ['COREBAY_PASS'])
cutoff = datetime.strptime("30-11-2025", "%d-%m-%Y")

if scraper.login():
    topics = scraper._get_topics()
    new_topics = [t for t in topics if t['last_post'] and t['last_post'] > cutoff]
    print(f"Total new topics after cutoff: {len(new_topics)}")
    
    # Check what is already in books.json
    db_path = '/home/jirif/github_tools/pirate/audioknihy-reports/books.json'
    with open(db_path, 'r') as f:
        books = json.load(f)
        
    existing_urls = set(b.get('topic_url') for b in books)
    
    missing = [t for t in new_topics if t['url'] not in existing_urls]
    print(f"Missing topics to scrape: {len(missing)}")
    
    # We could scrape them but doing it directly here is slow. Let's just run run_cron in background.
