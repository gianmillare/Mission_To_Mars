from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np
import time


def scrape():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    
    mars_data = {"Title" : scrape_news(browser),
                 "Featured Image" : scrape_featured_url(browser),
                 "Weather" : scrape_weather(browser),
                 "Comparison" : scrape_marsvearth(browser),
                 "Hemispheres" : scrape_hemispheres(browser)}
    
    browser.quit()
    return mars_data

def scrape_news():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)
    news = browser.find_by_css('div.content_title').first.value
    
    return news

def scrape_featured_url():
    browser = init_browser()
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    
    browser.click_link_by_id('full_image')
    featured_image_url = browser.find_by_css('img.fancybox-image')['src']
    
    featured_image_url_data = {"Mars Image URL" : featured_image_url}
    
    return featured_image_url_data




def scrape_weather():
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(1)
    mars_weather = browser.find_by_css('p.TweetTextSize.TweetTextSize--normal.js-tweet-text.tweet-text').text
    weather_data = {'Mars Weather' : mars_weather}
    
    return weather_data



def scrape_marsvearth():
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    url = "https://space-facts.com/mars/"
    browser.visit(url)
    
    mars_info = pd.read_html("https://space-facts.com/mars/")[1]
    mars_df = pd.DataFrame(mars_info)
    mars_df.set_index("Mars - Earth Comparison", inplace = True)
    mars_df
                 
    return mars_df


def scrape_hemispheres():
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
    
    return hemisphere_image_urls
    







