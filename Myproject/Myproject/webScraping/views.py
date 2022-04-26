from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def Home(request):
    html =""
    if request.method == 'POST':
        URL = request.POST["YourUrl"]
        if URL != None:
            page = requests.get(URL)
            text = page.content
            soup = BeautifulSoup(text, "html.parser")
            movies = soup.find("tbody", class_="lister-list").find_all("tr")
            html += "<center>"
            html += "<h1 style='color: #17202A;font-size:40px'>" + "<u>Movie Table</u>" + "</h1>"
            html += f'<table border={1} style="background-color:#E8F8F5  ;font-size:20px">'
            html += "<tr>"
            html += "<th style='color: red'>" + "Movie Rank" + "</th>"
            html += "<th style='color: red'>" + "Movie Name" + "</th>"
            html += "<th style='color: red'>" + "Year of releasing" + "</th>"
            html += "<th style='color: red'>" + "Rating of movie" + "</th>"
            html += "</tr>"
            html += "<tr>"
            for movie in movies:
                name = movie.find("td", class_="titleColumn").a.text
                rank = movie.find("td", class_="titleColumn").get_text(strip=True).split(".")[0]
                year = movie.find("td", class_="titleColumn").span.text.strip("()")
                rating = movie.find("td", class_="ratingColumn imdbRating").strong.text
                # print(rank,name, year ,rating)
                html += "<td>" + rank + "</td>"
                html += "<td>" + name + "</td>"
                html += "<td>" + year + "</td>"
                html += "<td>" + rating + "</td>"
                html += "</tr>"
            html += "</table>"
            html += "</center>"
       
    return render(request,'index.html',{"html": html})

