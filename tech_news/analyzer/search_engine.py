from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news_list = db.news.find({"title": {"$regex": title, "$options": "i"}})
    results = [(new["title"], new["url"]) for new in news_list]
    return results


# Requisito 8
def search_by_date(date):
    try:
        date_iso = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    new_date = date_iso.strftime("%d/%m/%Y")
    news_list = db.news.find({"timestamp": new_date})
    results = [(new["title"], new["url"]) for new in news_list]
    return results


# Requisito 9
def search_by_category(category):
    results = []
    news_list = db.news.find(
        {"category": {"$regex": category, "$options": "i"}}
        )
    for new in news_list:
        results.append((new["title"], new["url"]))
    return results
