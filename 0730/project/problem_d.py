import requests
from tmdb import TMDBHelper
from pprint import pprint


def recommendation(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록을 출력.
    추천 영화가 없을 경우 [] 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    tmdb_helper = TMDBHelper('83b326269660ac3171fddfc110d21cc7')
    # 추천작을 검색하는 url을 완성하기 위해서는 영화의 id가 필요하다.
    # get_movie_id를 이용하여 영화의 id를 우선적으로 가져온다.
    movie_title = tmdb_helper.get_movie_id(title)

    # 영화의 id가 None이면 None을 반환
    if movie_title == None:
        return movie_title

    # 영화의 id가 있으면 get_request_url와 f-string을 활용하여 url을 가져온다.
    else:
        url = tmdb_helper.get_request_url(f'/movie/{movie_title}/recommendations', language='ko')
        data = requests.get(url)
        reco_data = data.json()
        reco_lst = reco_data.get('results')

        # 추천작의 영화 제목을 담을 빈리스트를 생성하고, 반복문을 통해 추천작의 정보를 모아서 반환한다.
        reco_title = []
        for i in range( len(reco_lst) ):
            reco_title.append( reco_lst[i].get('title') )

        return reco_title



if __name__ == '__main__':
    pprint(recommendation('기생충'))
    pprint(recommendation('그래비티'))
    pprint(recommendation('검색할 수 없는 영화'))
