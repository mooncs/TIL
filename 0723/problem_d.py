import json


def max_revenue(movies):
    # 여기에 코드를 작성합니다.
    revenue = ['', 0]
    for movie in movies:
        movie_id = movie.get('id')
        m_json = open(f'c:/Users/csmoo/OneDrive/바탕 화면/python/SSAFY/0723/data/movies/{movie_id}.json', encoding='UTF8')
        m_info = json.load(m_json)
        if m_info.get('revenue') > revenue[1]:
            revenue[0] = m_info.get('title')
            revenue[1] = m_info.get('revenue')
            
    return revenue[0]

# def max_revenue(movies):
#     # 여기에 코드를 작성합니다.
#     max_value = 0
#     result = ''
#     for movie in movies:
#         movie_id = movie.get('id')
#         m_json = open(f'c:/Users/csmoo/OneDrive/바탕 화면/python/SSAFY/0723/data/movies/{movie_id}.json', encoding='UTF8')
#         m_info = json.load(m_json)
#         if m_info.get('revenue') > max_value:
#             max_value = m_info['revenue']
#             result = m_info['title']
            
#     return result
        
 
if __name__ == '__main__':
    movies_json = open('c:/Users/csmoo/OneDrive/바탕 화면/python/SSAFY/0723/data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))