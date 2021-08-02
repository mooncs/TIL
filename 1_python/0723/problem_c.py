import json
from pprint import pprint


def movie_info(movies, genres):
    # 여기에 코드를 작성합니다.
    movies_info = []
    for movie in movies:
        genre_ids = movie.get('genre_ids')
        for i in range(len(genre_ids)):
            genre_names = [genre.get('name') for genre in genres if genre_ids[i] == genre.get('id')]

        result = {
            'id' : movie.get('id'),
            'title' : movie.get('title'),
            'poster_path' : movie.get('poster_path'),
            'vote_average' : movie.get('vote_average'),
            'overview' : movie.get('overview'),
            'genre_ids' : genre_names
        }
        movies_info.append(result)
    
    return movies_info  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('c:/Users/csmoo/OneDrive/바탕 화면/python/SSAFY/0723/data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('c:/Users/csmoo/OneDrive/바탕 화면/python/SSAFY/0723/data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))