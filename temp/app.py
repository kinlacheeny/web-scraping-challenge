from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# mongo = PyMongo(app, uri=‘mongodb://localhost:27017/mars_app’)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = mission_to_mars.scrape_mars_info()
   mars.update({}, mars_data, upsert=True)
   return "Scraping successful!"

if __name__ == "__main__":
   app.run()    
