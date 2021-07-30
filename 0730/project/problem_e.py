import requests
from tmdb import TMDBHelper
from pprint import pprint


def credits(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록과 목록을 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    # 배우와 제작진의 정보를 불러오는 url을 완성하기 위해서는 영화의 id가 필요하다.
    # problem_d와 같은 과정을 통해 영화의 id를 우선적으로 가져온다.
    tmdb_helper = TMDBHelper('83b326269660ac3171fddfc110d21cc7')
    movie_title = tmdb_helper.get_movie_id(title)

    # 마찬가지로 영화의 id가 None이면 None을 반환
    if movie_title == None:
        return movie_title

    # 영화의 id가 있으면 get_request_url와 f-string을 활용하여 url을 가져온다.
    else:
        url = tmdb_helper.get_request_url(f'/movie/{movie_title}/credits')
        data = requests.get(url)
        credit_data = data.json()
        # 데이터의 형태를 잘 확인하고 필요한 정보를 가져온다.
        # 이전까지는 'results'를 통해 영화 정보에 접근했지만, 배우의 정보는 'cast'에 제작진의 정보는 'crew'를 통해 접근가능하다.
        cast_lst = credit_data.get('cast')
        crew_lst = credit_data.get('crew')

        # 조건에 맞는 배우와 제작진을 담을 빈리스트와 최종결과를 담을 빈 딕셔너리를 생성하고, 
        # 반복문을 통해 해당 정보를 모아서 반환한다.
        act = []
        direct = []
        result = {}
        # 배우 목록에서 cast_id 값이 10보다 작은 배우의 이름을 리스트에 저장
        for i in range(len(cast_lst)):
            if cast_lst[i].get('cast_id') < 10:
                    act.append(cast_lst[i].get('name'))
        
        # 제작진 목록에서 department 값이 Directing인 감독의 이름을 리스트에 저장
        for i in range(len(crew_lst)):
            if crew_lst[i].get('department') == 'Directing':
                direct.append(crew_lst[i].get('name'))

        # cast와 crew를 key로 가지고, 각각 배우 리스트와 제작진 리스트를 value값으로 가지는 딕셔너리 생성 및 반환
        result['cast'] = act
        result['crew'] = direct

        return result

if __name__ == '__main__':
    pprint(credits('기생충'))
    pprint(credits('검색할 수 없는 영화'))
