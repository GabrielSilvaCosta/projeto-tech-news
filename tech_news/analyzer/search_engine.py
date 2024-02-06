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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
