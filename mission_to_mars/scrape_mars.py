from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np
import time


def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape_news():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)
    news = browser.find_by_css('div.content_title').first.value
    news_data = {'Mars News' : news}
    
    browser.quit()
    return news_data

def scrape_featured_url():
    browser = init_browser()
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    
    browser.click_link_by_id('full_image')
    featured_image_url = browser.find_by_css('img.fancybox-image')['src']
    
    featured_image_url_dict = {"Mars Image URL" : featured_image_url}
    
    browser.quit()
    return featured_image_url




def
url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)





mars_weather = browser.find_by_css('p.TweetTextSize.TweetTextSize--normal.js-tweet-text.tweet-text').text
print(mars_weather)





html = browser.html
soup = BeautifulSoup(html, 'html.parser')

url = "https://space-facts.com/mars/"
browser.visit(url)

mars_info = pd.read_html("https://space-facts.com/mars/")[1]
mars_df = pd.DataFrame(mars_info)
mars_df.set_index("Mars - Earth Comparison", inplace = True)
mars_df



url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)





html = browser.html
hemisphere_soup = BeautifulSoup(html, 'html.parser')




hemisphere_titles = []

hemisphere_links = hemisphere_soup.find_all('h3')

for hemisphere in hemisphere_links:
    hemisphere_titles.append(hemisphere.text)

print(hemisphere_titles)





hemisphere_image_urls = []

for hemisphere in hemisphere_titles:
    browser.click_link_by_partial_text(hemisphere)
    hemisphere_image = browser.find_by_text('Sample')['href']
    hemisphere_image_urls.append({"Title" : hemisphere, "img_url" : hemisphere_image})
    browser.back()
hemisphere_image_urls







