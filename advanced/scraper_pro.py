import requests
from bs4 import BeautifulSoup
from fp import FP
from random import choice
import urllib3

class AdvancedScraper:
    def __init__(self):
        self.proxy_list = []
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...'
        ]
        self.current_proxy = None
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    def refresh_proxies(self):
        self.proxy_list = FP().get_proxy_list()
    
    def make_request(self, url):
        for _ in range(5):
            try:
                proxy = choice(self.proxy_list)
                response = requests.get(url,
                    proxies={'http': proxy, 'https': proxy},
                    headers={'User-Agent': choice(self.user_agents)},
                    timeout=10,
                    verify=False
                )
                if response.status_code == 200:
                    self.current_proxy = proxy
                    return BeautifulSoup(response.content, 'html.parser')
            except:
                continue
        raise ConnectionError("Failed after 5 attempts") 