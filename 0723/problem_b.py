import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.
    genre_ids = movie.get('genre_ids')
    genre_names = []
    for i in range(len(genre_ids)):
        for genre in genres:
            if genre_ids[i] == genre.get('id'):
                genre_names.append(genre.get('name'))

    result = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_names' : genre_names
    }
    
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('c:/Users/csmoo/OneDrive/바탕 화면/python/SSAFY/0723/data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('c:/Users/csmoo/OneDrive/바탕 화면/python/SSAFY/0723/data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))