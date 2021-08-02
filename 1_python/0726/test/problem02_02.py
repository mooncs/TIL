import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def title_length(movie):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 딕셔너리의 제목 key, title 값을 불러온다.
    title = movie.get('title')
    # 제목의 길이인 len(tilte)을 반환한다.
    return len(title)


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(title_length(movie)) 
    # 4