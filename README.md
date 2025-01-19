# Yahoo News Scraper
A simple Python-based web scraper that extracts news articles from Yahoo News using BeautifulSoup and requests. This scraper collects information about news articles such as the headline, source, time of posting, article description, and link, then saves this data into a CSV file for easy analysis.

# Features

* Scrapes headlines, sources, posting time, descriptions, and article links from Yahoo News.
* Automatically handles pagination to scrape multiple pages of results.
* Saves the collected data into a CSV file.

# Requirements

* **Python 3.x**
* **requests library**
* **BeautifulSoup (from bs4)**

# Usage
To use the scraper, simply run the Python script with your desired search term.
**python yahoo-news-scrapper.py**
Example:
news_data = scrape_news('los angeles fire')

# Screenshot of Yahoo News
Here is what the Yahoo News website looks like when running the scraper:

![CSV Screenshot](https://github.com/vanshika-ahuja1/YahooScraping-With-BeautifulSoup/blob/main/YahooHomepage.png?raw=true)

# Output
The scraper will create a CSV file named scraped_news.csv with the following columns:

* Title: The headline of the news article.
* Source: The source of the article.
* Posted: The time the article was posted.
* Link: The URL to the full article.
* Description: A brief description of the article.

# Example CSV output:

![CSV Screenshot](https://github.com/vanshika-ahuja1/YahooScraping-With-BeautifulSoup/blob/main/YahooScraping_Results.png?raw=true)



