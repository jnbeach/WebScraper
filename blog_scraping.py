import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
htmlObject = BeautifulSoup(response.text, "html.parser")
articles = htmlObject.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])
    for article in articles:
        anchor_tag = article.find("a")
        title = anchor_tag.get_text()
        url = anchor_tag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])

