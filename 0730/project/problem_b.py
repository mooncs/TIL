import requests
from tmdb import TMDBHelper
from pprint import pprint


def vote_average_movies():
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    tmdb_helper = TMDBHelper('83b326269660ac3171fddfc110d21cc7')
    url = tmdb_helper.get_request_url(language='ko', region='KR')
    data = requests.get(url)
    popular_data = data.json()
    # pprint(popular_data)

    # 인기작 영화 전체의 정보를 popular_lst로 정의
    popular_lst = popular_data.get('results')

    # 필요한 정보를 찾기 위해 빈리스트와 반복문 활용
    result = []
    for i in range(len(popular_lst)):
        # 추천작의 평점이 8점 이상인 영화의 정보를 결과 리스트에 추가
        if popular_lst[i].get('vote_average') >= 8:
            result.append(popular_lst[i])

    # 평점이 8점 이상인 영화의 정보가 담긴 리스트 반환
    return result


if __name__ == '__main__':
    pprint(vote_average_movies())
