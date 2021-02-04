#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
import time


# In[56]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ## NASA Mars News

# In[57]:


# NASA news url 
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[58]:


# Parse with Beautiful Soup
html = browser.html
soup = bs(html, 'html.parser')


# In[63]:


# collect the latest News Title and Paragraph Text. Assign the text 
# to the variables that you can reference later. 
news_title = soup.find('div', class_='content_title').text
news_p = soup.find('div', class_='article_teaser_body').text
print(f"Title: {news_title}")
print(f"Paragraph: {news_p}")


# ## JPL Mars Space Images

# In[64]:


# JPL url
jpl_image_url = "https://webcache.googleusercontent.com/search?q=cache:gFCwbhsgFQsJ:https://www.jpl.nasa.gov/images/+&cd=1&hl=en&ct=clnk&gl=us"
browser.visit(jpl_image_url)


# In[65]:


# parse with bs
jpl_html = browser.html
jpl_soup = bs(jpl_html, 'html.parser')
#print(jpl_soup.prettify())


# In[66]:


image_url = jpl_soup.find('img)
print(image_url)
                          
# the original url is not working and a cache link was provided, but it is not providing the output of images.


# ## Mars Facts

# In[74]:


# visit the Mars Facts url and use Pandas to scrape the table containing
# facts about the planet including Diameter, Mass, etc. 
mars_url = 'https://space-facts.com/mars/'
browser.visit(mars_url)

mars_facts_table = pd.read_html(mars_url)[0]
print(mars_facts_table)


# ## Mars Hemispheres

# In[108]:


# Visit url to scrape
usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(usgs_url)
usgs_html = browser.html
soup = bs(usgs_html,'html.parser')


# In[109]:


# Parse hemispheres w BS and create empty list for image urls 
hemispheres = soup.find('div',class_='collapsible results')
items = hemispheres.find_all('div',class_= 'item')
hemi_images = []


# In[112]:


# Store the main url
base_url = 'https://astrogeology.usgs.gov'

# Iterate through each item in hemispheres
for i in items:
    try:
        # Store title
        hemisphere = i.find('div',class_= 'description')
        title = i.h3.text
        
        # Store the image url amd visit url
        hs_url = i.a['href']
        browser.visit(f'{base_url}{hs_url}')
        
        # HTML object of the individual hemisphere info
        html = browser.html
        
        # Parse w BS
        soup = bs(html,'html.parser')
        
        # Retrieve full image source
        image_url = soup.find('li').a['href']
        
        # if url has title and image, then print results
        if (title and image_url):
            print('-------------------------------------')
            print(title)
            print(image_url)
            
        # Create dictionary for title and url
        hemis_dict={
            'title':title,
            'image_url':image_url
        }
        hemi_images.append(hemis_dict)
        
    except Exception as e:
        print(e)


# In[ ]:




