import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 전체의 합을 담을 total이라는 변수를 0이라고 선언해둔다.
    total = 0
    # scores 리스트에 담겨있는 값을 score로 하나씩 불러온다.
    for score in scores:
        # 불러온 score의 값을 total에 더해준다.
        total += score
    # 전체 합을 구한 total을 scores리스트의 길이(개수)를 의미하는 len(scores)로 나눠 평균 값을 구한다.
    avg = total / len(scores)
    # 계산한 avg값을 반환해준다.
    return avg


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json')
    scores = json.load(scores_json)
    print(average(scores)) 
    # 82.5