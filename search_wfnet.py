import os, sys, json, re
sys.path.insert(0, '/home/jirif/github_tools/pirate')
from tools.wfnet_scraper import _playwright_login, _cookies_to_session, BASE
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import asyncio

async def main():
    load_dotenv('/home/jirif/github_tools/pirate/.env')
    cookies = await _playwright_login(os.environ['WFNET_USER'], os.environ['WFNET_PASS'])
    session = _cookies_to_session(cookies)
    r = session.get(f'{BASE}/index.php?action=search2', data={'search': 'Ekeaze', 'submit': 'Vyhledat'})
    # Actually SMF search requires a POST to a specific endpoint with session ID, maybe we can just search the downloaded DB!
    
main()
