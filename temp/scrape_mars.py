# Dependencies and Setup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

# Scrape Mars News
def scrape_mars_info():
	browser = init_browser()
	
	# NASA news url 
	url = "https://mars.nasa.gov/news/"
	browser.visit(url)

	# Parse with Beautiful Soup
	html = browser.html
	soup = bs(html, 'html.parser')
		
	# Scrape the latest News Title and Paragraph Text
	news_title = soup.find('ul', class_='item_list')
	news_title = news_title.find('div', class_='content_title').text
	news_p = soup.find('div', class_='article_teaser_body').text

	# browser.quit()

	# return news_title, news_p

# JPL Mars Space Images
# def scape_jpl_image():

	# browser = init_browser()
	time.sleep(2)

	# JPL url
	jpl_image_url = "https://webcache.googleusercontent.com/search?q=cache:gFCwbhsgFQsJ:https://www.jpl.nasa.gov/images/+&cd=1&hl=en&ct=clnk&gl=us"
	browser.visit(jpl_image_url)
	
	# parse with bs
	jpl_html = browser.html
	jpl_soup = bs(jpl_html, "html.parser")

	# Find jpl image url to the full size
	jpl_soup = jpl_soup.find('div', class_='sm:object-cover object-cover')
	featured_image_url = jpl_soup.find('img').get('src')
	time.sleep(2)
	# browser.quit()
	
	# return featured_image_url

# Mars Facts ****** ended 2/9/21 at 12:47 am *********
# def scrape_mars_facts():

	# browser = init_browser()
	
	# Visit the Mars Facts url and use Pandas to scrape the table
	mars_url = 'https://space-facts.com/mars/'
	browser.visit(mars_url)

	# Use Pandas pd.read_html - to scrape table data from url
	mars_facts_table = pd.read_html(mars_url)[0]
	
	# Find the mars facts DataFrame in the list
	mars_df = mars_facts[0]

	# Create columns named Description and Value
	mars_df.columns = ["Description", "Value"]

	# Set index to Description
	mars_df.set_index("Description", inplace=True)

	# Save html code
	html_table = mars_df.to_html()

	# Strip unwanted newlines to clean up the table
	html_table.replace("\n", '')

	# browser.quit() 

	# return html_table

# Mars Hemispheres
# def scrape_mars_hemis():

	# browser = init_browser()
	time.sleep(2)
	# Visit url to scrape
	usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
	browser.visit(usgs_url)
	soup = bs(usgs_url, "html.parser")
	
	# Parse hemispheres 
	hemispheres = browser.find_by_tag('h3')

	# Store the main url
	main_url = usgs_url

	hemi_urls = []

	# Loop through the list of all hemispheres information
for i in range(len(hemispheres)):

	hemi = {}
	browser.find_by_css('h3')[i].click()

# Store title
	hemi['title'] = browser.find_by_css('h2.title').text

# Store the image url amd visit url
	hemi['img'] = browser.links.find_by_text('Sample')['href']

	hemi_urls.append(hemi)
	browser.back()
		
	mars_dict = {
		"news_title": news_title,
		"news_p": news_p,
		"featured_image_url": featured_image_url,
		"html_table": html_table,
		"hemi_urls": hemi_urls
	}

	#Close the browser after scraping

	browser.quit()

	return mars_dict