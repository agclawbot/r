import os, sys, json, re, asyncio
sys.path.insert(0, '/home/jirif/github_tools/pirate')
from tools.wfnet_scraper import _playwright_login, _cookies_to_session, BASE, FORUM_URL
from bs4 import BeautifulSoup
from dotenv import load_dotenv

async def main():
    load_dotenv('/home/jirif/github_tools/pirate/.env')
    cookies = await _playwright_login(os.environ['WFN_EMAIL'], os.environ['WFN_PASS'])
    session = _cookies_to_session(cookies)
    
    # We will fetch the first 3 pages of War-forum
    for i in range(0, 60, 30):
        url = f'{BASE}/music-mluvene-slovo/{i}/' if i > 0 else f'{BASE}/music-mluvene-slovo/'
        r = session.get(url)
        print(f"Page {i} -> Ekeaze in html? {'Ekeaze' in r.text}")

asyncio.run(main())
