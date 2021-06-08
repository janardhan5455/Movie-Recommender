import requests
import pandas as pd
import time
import pickle

API_KEY="33e9c9280301152615256845d01b0821"
def get_posters(movie):
  url=f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie}&page=1&include_adult=false"
  r = requests.get(url)
  d = r.json()
  path = d['results'][0]['poster_path']
  return f"https://www.themoviedb.org/t/p/w600_and_h900_bestv2{path}"


df=pd.read_csv('movie_dataset.csv')


with open("movies_poster.pkl",'rb') as f:
    movies_d=pickle.load(f)
print(movies_d)
# movies_poster_dir={}

# for movie in df['original_title']:
#     try:
#         poster = get_posters(movie)
#         movies_poster_dir[movie]=poster
#         print(poster)
#         time.sleep(0.1)
#     except BaseException as e:
#         print(e)


# with open("movies_poster.pkl",'wb') as f:
#     pickle.dump(movies_poster_dir,f)

# with open("movies_poster.pkl",'rb') as f:
#     d=pickle.load(f)

# print(d)

