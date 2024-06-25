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
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    
    new_date = date.strftime("%Y-%m-%d")
    news_list = db.news.find({"timestamp": {"$regex": new_date}})
    results = [(new["title"], new["url"]) for new in news_list]
    return results


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
