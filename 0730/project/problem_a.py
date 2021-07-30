import requests
from tmdb import TMDBHelper


def popular_count():
    """
    popular 영화목록의 개수 출력.
    """
    # TMDBHelper class 인스턴스 생성.
    # key값을 별도로 넣지 않으면, default값인 None이 들어가기 때문에 개인의 key값을 넣어준다.
    tmdb_helper = TMDBHelper('83b326269660ac3171fddfc110d21cc7')

    # 원하는 url을 가져오기 위해 인스턴스 메서드인 get_request_url이용
    # method의 default값이 '/movie/popular'이기 때문에, 추가적인 language='ko', region='KR'만 입력
    url = tmdb_helper.get_request_url(language='ko', region='KR')
    
    # 완성된 url을 가지고 필요한 정보를 불러오고, 
    # 불러온 정보의 형태가 궁금하다면 print하거나 url에 들어가서 형태를 확인하고 사용
    data = requests.get(url)
    popular_data = data.json()

    return len(popular_data['results'])
    


if __name__ == '__main__':
    print(popular_count())
