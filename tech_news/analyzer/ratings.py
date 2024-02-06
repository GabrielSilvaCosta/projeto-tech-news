from tech_news.database import db


def top_5_categories():
    categories_count = {}

    for news in db["news"].find():
        if news["category"] in categories_count:
            categories_count[news["category"]] += 1
        else:
            categories_count[news["category"]] = 1

    sorted_categories = sorted(
        categories_count.items(), key=lambda x: (-x[1], x[0])
    )[:5]

    return [category[0] for category in sorted_categories]
