import requests
import json
from dotenv import load_dotenv

import os

load_dotenv()

data =input("What category of news you want? ")


url = (f'https://newsapi.org/v2/everything?'
       f'q={data}&'
       f'from=25-03-10&'
       f'sortBy=popularity&'
       f'apiKey={os.getenv('NEWS_API_KEY')}')

response = requests.get(url)


#print(response.json())
news_data = response.json()


with open('person.json', 'w') as file:
    json.dump(response.json(), file,indent=4)

for i, article in enumerate(news_data.get('articles', [])[:5], 1):
    print(f"{i}. 📰 {article.get('title')}")
    print(f"   🏷️ Source: {article['source']['name']}")
    print(f"   📅 Published: {article.get('publishedAt')}")
    print(f"   🔗 URL: {article.get('url')}")
    print("-" * 60)

print("\n✅ JSON data has been saved in 'person.json'")

