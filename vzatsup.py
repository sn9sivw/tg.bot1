import requests
from bs4 import BeautifulSoup

url = 'https://vkusvill.ru/media/journal/retsepty-supov-borshch-kharcho-lagman-i-drugie-pervye-blyuda-sogrevayushchie-v-kholoda.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36     (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Создаем объект BeautifulSoup для удобного парсинга HTML-кода
    soup = BeautifulSoup(response.text, 'html.parser')

    # Пример извлечения всех заголовков <h1> на странице
    h1_tags = soup.find_all('div', class_='VM_Container')
    for tag in h1_tags:
        print(tag.text.strip())
else:
    print(f'Ошибка: статус ответа {response.status_code}')
