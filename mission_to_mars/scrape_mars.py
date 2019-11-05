#!/usr/bin/env python
# coding: utf-8

# In[275]:


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np


# In[276]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[277]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)


# In[278]:


news = browser.find_by_css('div.content_title').first.value
print(news)


# In[279]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[280]:


browser.click_link_by_id('full_image')


# In[281]:


featured_image_url = browser.find_by_css('img.fancybox-image')['src']
print(featured_image_url)


# In[282]:


url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)


# In[283]:


mars_weather = browser.find_by_css('p.TweetTextSize.TweetTextSize--normal.js-tweet-text.tweet-text').text
print(mars_weather)


# In[284]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

url = "https://space-facts.com/mars/"
browser.visit(url)

mars_info = pd.read_html("https://space-facts.com/mars/")[0]
mars_df = pd.DataFrame(mars_info)
mars_df.set_index("Mars - Earth Comparison", inplace = True)
mars_df


# In[285]:


url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# In[286]:


html = browser.html
hemisphere_soup = BeautifulSoup(html, 'html.parser')


# In[287]:


hemisphere_titles = []

hemisphere_links = hemisphere_soup.find_all('h3')

for hemisphere in hemisphere_links:
    hemisphere_titles.append(hemisphere.text)

print(hemisphere_titles)


# In[288]:


hemisphere_image_urls = []

for hemisphere in hemisphere_titles:
    browser.click_link_by_partial_text(hemisphere)
    hemisphere_image = browser.find_by_text('Sample')['href']
    hemisphere_image_urls.append({"Title" : hemisphere, "img_url" : hemisphere_image})
    browser.back()
hemisphere_image_urls


# In[ ]:




