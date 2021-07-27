import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_id_length(data):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 딕셔너리에 들어있는 id의 value 값을 불러온다.
    id = data.get('id')
    # id의 길이, len(id)가 4이상이고 16이하이면
    if len(id)>=4 and len(id) <=16:
        # True를 반환
        return True
    # 그렇지 않으면 False를 반환
    return False
    

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    user_data = open('problem03_data.json', encoding='UTF8')
    user_data = json.load(user_data)
    print(check_id_length(user_data))
    # True