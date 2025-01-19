import csv
from time import sleep
from bs4 import BeautifulSoup
import requests

def fetch_html_content(url):
    #fetches the html content of url
    try:
        response=requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return None

def news_info(news_block):
    headline=news_block.find('h4', class_='s-title fz-20 lh-m fw-500 ls-027 mt-8 mb-2')
    title=headline.find('a').get_text() if headline else 'No Title'
    

    s=news_block.find('span', class_='s-source fw-l')
    source=s.get_text() if s else 'No Source'

    p=news_block.find('span', class_='s-time fz-14 lh-18 fc-dustygray fl-l mr-4')
    posted=p.get_text() if p else 'No Time'

    l=news_block.find('a')
    link=l.get('href') if l else None

    d =news_block.find('p', class_='s-desc fz-14 lh-1_45x fc-444444')
    description=d.get_text() if d else 'No Description'

    return(title,source,posted,link,description)

def next_page(soup):
    next_page=soup.find('a', class_='next')
    if next_page:
        next_page_url=next_page.get('href') if next_page else None
        return 'https://news.search.yahoo.com/serach'+next_page_url if not next_page_url.startswith('http') else next_page_url
    return None

def save_data_to_csv(news_data, filename='scraped_news.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Source', 'Posted', 'Link', 'Description'])
        writer.writerows(news_data)

def scrape_news(search):
    url='https://news.search.yahoo.com/search?p={}'.format(search.replace(" ", "+"))
    all_articles=[]
    while url:
        page_content = fetch_html_content(url)
        if not page_content:
            break
        soup=BeautifulSoup(page_content,'html.parser')
        
        #extracting news items from current page
        news_blocks=soup.find_all("div", id="web")
        if not news_blocks:
            print("No news articles found on the page.")
            break
        for news_block in news_blocks:
            news=news_info(news_block)
            all_articles.append(news)
        
        #for next page
        url=next_page(soup)
        sleep(1)
    
    #saving the collected data to csv
    save_data_to_csv(all_articles)
    return all_articles

        


news_data=scrape_news('los angeles fire')
print("Scraped",len(news_data),"articles.")