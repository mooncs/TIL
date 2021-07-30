import requests
from tmdb import TMDBHelper
from pprint import pprint


def ranking():
    """
    popular 영화목록을 정렬하여 평점순으로 5개 출력.
    """
    tmdb_helper = TMDBHelper('83b326269660ac3171fddfc110d21cc7')
    url = tmdb_helper.get_request_url(language='ko', region='KR')
    data = requests.get(url)
    popular_data = data.json()
    popular_lst = popular_data.get('results')

    vote_average = []
    for i in range(len(popular_lst)):
        vote_average.append(popular_lst[i].get('vote_average'))
    vote_sorted = sorted(vote_average, reverse=True)[:5]
    
    high_avg_movie = []
    for i in range(len(popular_lst)):
        if popular_lst[i].get('vote_average') in vote_sorted:
            high_avg_movie.append(popular_lst[i])

    return high_avg_movie



if __name__ == '__main__':
    pprint(ranking())

