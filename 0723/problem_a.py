import json
from pprint import pprint


def movie_info(movie):
    # 여기에 코드를 작성합니다.    
    result = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids')
    }
    
    return result



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('c:/Users/csmoo/OneDrive/바탕 화면/python/SSAFY/0723/data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))