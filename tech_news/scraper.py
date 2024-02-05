from datetime import datetime
import time
import requests
from parsel import Selector


def fetch(url):
    headers = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers=headers, timeout=3)
        time.sleep(1)

        if response.status_code == 200:
            return response.text
        else:
            return None

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news_urls = selector.css(".entry-title a::attr(href)").getall()

    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css(".next::attr(href)").get()

    return next_page_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    title = selector.css(".entry-title::text").get()
    title = title.strip() if title else None
    url = selector.css("link[rel='canonical']::attr(href)").get()
    timestamp_str = selector.css(".meta-date::text").get()
    writer = selector.css(".title-author a::text").get()
    writer = writer.strip() if writer else None
    reading_time_str = selector.css(".meta-reading-time::text").get()
    summary = selector.css(
        ".entry-content > p:nth-of-type(1) *::text"
    ).getall()
    category = selector.css(".label::text").get()

    # Convertendo timestamp para o formato desejado (dd/mm/AAAA)
    timestamp = (
        datetime.strptime(timestamp_str, "%d/%m/%Y").strftime("%d/%m/%Y")
        if timestamp_str
        else None
    )

    # Convertendo reading_time para um número inteiro
    reading_time = (
        int(reading_time_str.split()[0]) if reading_time_str else None
    )

    # Juntando o summary em uma string, removendo caracteres vazios no final
    summary = "".join(summary).strip() if summary else None

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
