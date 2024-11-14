import requests
from bs4 import BeautifulSoup
import json
import os

# URL сайта для сбора данных
BASE_URL = "http://quotes.toscrape.com"


def fetch_quotes(url):
    """
    Функция для отправки запроса к странице и извлечения цитат
    """
    response = requests.get(url)
    response.raise_for_status()  # Проверяем успешность запроса
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    return quotes


def scrape_all_quotes():
    """
    Основная функция для сбора всех цитат с сайта (через пагинацию)
    """
    all_quotes = []
    url = BASE_URL
    while url:
        quotes = fetch_quotes(url)
        all_quotes.extend(quotes)
        # Проверка на следующую страницу
        next_button = BeautifulSoup(requests.get(url).text, 'html.parser').find('li', class_='next')
        url = BASE_URL + next_button.find('a')['href'] if next_button else None

    return all_quotes


def save_to_json(data, filename='data/quotes.json'):
    """
    Сохраняем данные в JSON файл
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    quotes = scrape_all_quotes()
    save_to_json(quotes)
    print("Данные успешно сохранены в data/quotes.json")
