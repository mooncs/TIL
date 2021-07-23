import json


# def dec_movies(movies):
#     # 여기에 코드를 작성합니다.
#     m_same_month = []
#     for movie in movies:
#         movie_id = movie.get('id')
#         m_json = open(f'c:/Users/csmoo/OneDrive/바탕 화면/python/SSAFY/0723/data/movies/{movie_id}.json', encoding='UTF8')
#         m_info = json.load(m_json)
#         if m_info.get('release_date')[5:7] == '12' :
#             m_same_month.append(m_info.get('title'))
            
#     return m_same_month

def dec_movies(movies):
    # 여기에 코드를 작성합니다.
    m_same_month = []
    for movie in movies:
        movie_id = movie.get('id')
        m_json = open(f'c:/Users/csmoo/OneDrive/바탕 화면/python/SSAFY/0723/data/movies/{movie_id}.json', encoding='UTF8')
        m_info = json.load(m_json)
        if m_info.get('release_date').split('-')[1] == '12' :
            m_same_month.append(m_info.get('title'))
            
    return m_same_month
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('c:/Users/csmoo/OneDrive/바탕 화면/python/SSAFY/0723/data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))