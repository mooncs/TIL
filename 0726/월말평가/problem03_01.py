import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_password_verified(data):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 딕셔너리에 들어있는 password와 password_confirm의 value 값을 불러온다.
    password = data.get('password')
    confirm = data.get('password_confirm')
    # password와 password_confirm 값을 비교
    if password == confirm:
        # 두 변수가 같다면, True 반환
        return True
    # 그렇지 않다면, False 반환
    return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    user_data = open('problem03_data.json', encoding='UTF8')
    user_data = json.load(user_data)
    print(is_password_verified(user_data))
    # True
    