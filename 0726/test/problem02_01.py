import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def over(movie):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 평점을 비교하기 위해 딕셔너리의 평점key, user_rating의 value 값을 불러와 8이상인지 비교한다.
    if movie.get('user_rating') >= 8:
        # 8이상이라면 True를 반환하고
        return True
    # 8미만이라면 False를 반환한다.
    # (else구문 생략)
    return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(over(movie)) 
    # True