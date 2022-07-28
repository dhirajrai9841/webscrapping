
from flask import Flask, request, render_template

import requests
from bs4 import BeautifulSoup
app= Flask(__name__)


@app.route('/')
def hello():
    return render_template('scrapingwithflask.html')


@app.route("/success", methods=['POST'])
def movies():
    movieNo = request.form['numberOfmovies']
    print(movieNo)
    Req = requests.get(
        "https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="+movieNo)
    source = BeautifulSoup(Req.content, "html.parser")
    return render_template("next.html", parsedMovieList=source, movieNo=movieNo)


if __name__ == '__main__':
    app.run(debug=True)