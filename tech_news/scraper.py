import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.RequestException as exception:
        print(f"Erro ao fazer requisição: {exception}")
        return None
    
    finally:
        time.sleep(1)


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news = selector.css(".cs-overlay a::attr(href)").getall()
    print(f"As novidades são: {news}")
    if news and len(news) > 0:
        return news
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
