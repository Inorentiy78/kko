from flask import Flask, render_template, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique = True , nullable = False)

class GenreMovie(db.Model):
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'),nullable= True ,primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable= True ,primary_key=True)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)                                                                                          
    rating = db.Column(db.Float , default=1)
    description = db.Column(db.String)
    date = db.Column(db.Date, default=datetime.strptime("1990.01.01" , '%Y.%m.%d'), nullable = False )
    img = db.Column(db.String, nullable = False)
    genres = db.relationship("Genre", secondary = GenreMovie.__table__, lazy ="subquery", backref = db.backref("movies",lazy=True))
    backref = db.backref('movies', lazy = True)


    

@app.route("/")
def index():
    genres = Genre.query.all()
    movies = Movie.query.all()
    return render_template("index.html", genres=genres, movies=movies)
if __name__ == '__main__':
    app.run(debug=True)