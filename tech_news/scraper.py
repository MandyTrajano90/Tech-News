import time
import requests
from parsel import Selector
from .database import create_news


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
    selector = Selector(text=html_content)
    next_page = selector.css(".next::attr(href)").get()
    print(f"O link da próxima página é: {next_page}")
    return next_page


# Requisito 4
def scrape_news(html_content):
    infos = {}
    selector = Selector(text=html_content)

    infos["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    infos["title"] = selector.css(".entry-title::text").get().strip()
    infos["timestamp"] = selector.css(".meta-date::text").get()
    infos["writer"] = selector.css(".author a::text").get()
    infos["reading_time"] = int(
        selector.css(".meta-reading-time::text").get().split()[0])
    infos["summary"] = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    infos["category"] = selector.css(".category-style .label::text").get()

    return infos


# Requisito 5
def get_tech_news(amount):
    news = []
    url = 'https://blog.betrybe.com'

    while len(news) < amount:
        html = fetch(url)
        news_urls = scrape_updates(html)
        for news_url in news_urls:
            news_html = fetch(news_url)
            news.append(scrape_news(news_html))
            if len(news) == amount:
                break
        url = scrape_next_page_link(html)
    create_news(news)

    return news
