import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_password_number_case(data):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 딕셔너리에 들어있는 password의 value 값을 불러온다.
    password = data.get('password')
    # password 문자열을 이루고 있는 하나의 문자를 word로 불러와 비교한다.
    for word in password:
        # 비밀번호에 포함된 글자가 숫자이면
        # 용도에 따라 isdigit(), isdecimal(), isnumeric() 선택 사용가능
        if word.isdigit():
        # if word.isdecimal():
        # if word.isnumeric():
            # True를 반환
            return True
    # 비밀번호를 다 돌았는데도 True를 반환하지 못했다면,
    # 즉, 숫자가 없다면 False를 반환
    return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    user_data = open('problem03_data.json', encoding='UTF8')
    user_data = json.load(user_data)
    print(check_password_number_case(user_data))
    # True