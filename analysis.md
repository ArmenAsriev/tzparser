# Анализ задачи: Сбор данных с quotes.toscrape.com

## Что было сделано
- Разработан скрипт для сбора цитат с сайта `http://quotes.toscrape.com`.
- Данные собираются в формате JSON с информацией о цитате, авторе и тегах.

## Источник данных
- Данные извлекаются с каждой страницы сайта с цитатами. Сайт имеет несколько страниц с цитатами, которые связаны через ссылки на следующую страницу.

## Как осуществлялся сбор данных
- Использовались библиотеки `requests` для отправки HTTP-запросов и `BeautifulSoup` из `bs4` для парсинга HTML-кода страниц и извлечения данных.
- Для обработки страниц добавлена функция `fetch_quotes`, которая извлекает цитаты с текущей страницы.
- Переход по страницам реализован через пагинацию, где каждая следующая страница проверяется на наличие ссылки "next".

## Выбор методов и инструментов
- `requests`: используется для отправки HTTP-запросов, так как позволяет легко работать с REST API и веб-страницами.
- `BeautifulSoup`: был выбран для парсинга HTML, так как HTML на сайте имеет простую структуру, и `BeautifulSoup` хорошо справляется с такой задачей.