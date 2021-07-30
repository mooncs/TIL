'''
api_keys = '83b326269660ac3171fddfc110d21cc7'

https://api.themoviedb.org/3
/movie/76341?api_key=83b326269660ac3171fddfc110d21cc7
&language=ko
&region=KR

[검색]
https://api.themoviedb.org/3
/search/movie
?api_key=83b326269660ac3171fddfc110d21cc7
&query=Jack+Reacher
&language=ko
&region=KR

[인기작]
https://api.themoviedb.org/3
/movie/popular
?api_key=83b326269660ac3171fddfc110d21cc7
&language=ko
&region=KR

[추천작] # 75780, Jack+Reacher
https://api.themoviedb.org/3
/movie/{movie_id}/recommendations
?api_key=83b326269660ac3171fddfc110d21cc7
&language=ko

[제작진]
https://api.themoviedb.org/3
/movie/{movie_id}/credits
?api_key=83b326269660ac3171fddfc110d21cc7
&language=ko
'''

'''
[검색] 496243
https://api.themoviedb.org/3
/search/movie
?api_key=83b326269660ac3171fddfc110d21cc7
&query=기생충
&language=ko
&region=KR

[추천작] # 496243, 기생충
https://api.themoviedb.org/3
/movie/496243/recommendations
?api_key=83b326269660ac3171fddfc110d21cc7
&language=ko

[제작진]
https://api.themoviedb.org/3
/movie/496243/credits
?api_key=83b326269660ac3171fddfc110d21cc7
&language=ko
'''

import requests
from pprint import pprint

class TMDBHelper:
    
    def __init__(self, api_key=None):
        self.api_key = api_key

    # /movie/popular, 인기작 검색을 기본값으로 제공
    def get_request_url(self, method='/movie/popular', **kwargs):
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'
        # 여기까지가 필수 해당 부분
        # print(kwargs)
        for key, value in kwargs.items():
            request_url += f'&{key}={value}'

        return request_url

    # 제목으로 영화 검색 후, 검색결과에서 영화 id를 return
    def get_movie_id(self, title):
        
        search = self.get_request_url('/search/movie', query=title, language='ko', region='KR')
        search_data = requests.get(search).json()
        # pprint(search_result)

        # 없는 영화를 검색하면 results 안이 비어서 나온다.
        # 'results'가 없는 경우를 대비해서 get 사용
        search_result = search_data.get('results')

        # search_result가 있다면
        if search_result:
            # 검색결과가 여러개 나와도 첫번째로 나오는 것이 대부분 가장 정확한 것이기 때문에 [0]으로 고정
            movie_id = search_result[0]['id']
            return movie_id
    
        else:
            return 0


# tmdb_helper = TMDBHelper('83b326269660ac3171fddfc110d21cc7')
# print(tmdb_helper.get_request_url(language='ko', region='KR'))
# print(tmdb_helper.get_movie_id('기생충'))
# print(tmdb_helper.get_movie_id('충생기'))


def recommendation(title):
    th = TMDBHelper('key')
    movie_id = th.get_movie_id

    th.get_request_url(f'')

def popular_count():
    tmdb_helper = TMDBHelper('83b326269660ac3171fddfc110d21cc7')
    url = tmdb_helper.get_request_url(language='ko', region='KR')
    data = requests.get(url)
    # pprint(data.json())
    popular_data = data.json()

    return len(popular_data['results'])


print(popular_count())