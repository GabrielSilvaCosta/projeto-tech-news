from datetime import datetime
from tech_news.database import db


# Requisito 7
def search_by_title(title):
    title_lower = title.lower()
    result = []

    for news in db["news"].find():
        news_title_lower = news["title"].lower()
        if title_lower in news_title_lower:
            result.append((news["title"], news["url"]))

    return result


# Requisito 8
def search_by_date(date):
    try:
        search_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    result = []

    for news in db["news"].find():
        news_date = datetime.strptime(news["timestamp"], "%d/%m/%Y").strftime(
            "%d/%m/%Y"
        )
        if news_date == search_date:
            result.append((news["title"], news["url"]))

    return result


# Requisito 9
def search_by_category(category):
    result = []

    for news in db["news"].find():
        if category.lower() == news["category"].lower():
            result.append((news["title"], news["url"]))

    return result
