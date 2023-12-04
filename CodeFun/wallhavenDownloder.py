import requests


QUERY = ''
CATEGORIES = '100'
PURITY = '100'
TOP_RANGE = '1M'
SORTING = 'toplist'
ORDER = 'desc'
API = ''

link = f'https://wallhaven.cc/api/v1/search?apikey={API}&q={QUERY}&categories={CATEGORIES}&purity={PURITY}$topRange={TOP_RANGE}&sorting={SORTING}&order={ORDER}&ai_art_filter=1'