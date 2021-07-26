import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def history(movie):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 딕셔너리의 줄거리 key, overview값을 불러온다.
    overview = movie.get('overview')
    # '과거'라는 단어가 줄거리에 포함되어 있는지 확인
    if '과거' in overview:
        # 있다면 True를 반환
        return True
    # 없다면 False를 반환
    return False

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(history(movie)) 
    # False