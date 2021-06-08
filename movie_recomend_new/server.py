from flask import Flask, request ,jsonify, render_template
from  movie_recomend import *

app = Flask(__name__)



@app.route('/api')
def api():
    movie = request.args.get('movie')
    movies=get_movies(movie)
    return jsonify(movies)


@app.route('/mov', methods=['POST','GET'])
def mov():
    movie = request.form['movie']
    if len(movie) != 0:
        movies=get_movies(movie)
    else:
        movies=None
    
    return render_template('./index.html',movies=movies)


@app.route('/')
def main():
    return render_template('./index.html',movies=None)


if __name__ == '__main__':
    app.run(debug=True)