import requests
from tmdb import TMDBHelper
from pprint import pprint
from operator import itemgetter


def ranking():
    """
    popular 영화목록을 정렬하여 평점순으로 5개 출력.
    """
    tmdb_helper = TMDBHelper('83b326269660ac3171fddfc110d21cc7')
    url = tmdb_helper.get_request_url(language='ko', region='KR')
    data = requests.get(url)
    popular_data = data.json()
    popular_lst = popular_data.get('results')
    # 가져온 리스트 형태의 데이터를 sorted()와 itemgetter를 통해 평점순으로 정렬한다.
    new_pop_lst = sorted(popular_lst, key=itemgetter('vote_average'), reverse=True)
    # new_pop_lst = sorted(popular_lst, key=lambda x: x['vote_average'], reverse=True)

    # 정렬된 리스트에서 처음부터 5번째까지의 영화 정보를 반환한다.
    return new_pop_lst[:5]


if __name__ == '__main__':
    pprint(ranking())

