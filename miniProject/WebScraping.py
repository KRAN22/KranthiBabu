from bs4 import BeautifulSoup
import requests
import os

URL = "https://www.imdb.com/chart/top/"
page = requests.get(URL)
text = page.content
soup = BeautifulSoup(text,"html.parser")
movies = soup.find("tbody",class_="lister-list").find_all("tr")

html ="<center>"
html +="<h1>"+"Movie Table"+"</h1>"
html += f'<table border={1}">'
html += "<tr>"
html += "<th>" + "Movie Rank" +"</th>"
html += "<th>" + "Movie Name" + "</th>"
html += "<th>" + "Year of releasing" + "</th>"
html += "<th>" + "Rating of movie" + "</th>"
html += "</tr>"
html += "<tr>"
for movie in movies:
    name = movie.find("td",class_="titleColumn").a.text
    rank = movie.find("td",class_="titleColumn").get_text(strip=True).split(".")[0]
    year = movie.find("td",class_="titleColumn").span.text.strip("()")
    rating = movie.find("td",class_="ratingColumn imdbRating").strong.text
    # print(rank,name, year ,rating)
    html += "<td>" + rank + "</td>"
    html += "<td>" + name + "</td>"
    html += "<td>" + year + "</td>"
    html += "<td>" + rating + "</td>"
    html += "</tr>"
html += "</table>"
html +="</center>"

with open("outpt.html", "w", encoding='utf-8') as file:
    file.write(html)

os.startfile('outpt.html')
