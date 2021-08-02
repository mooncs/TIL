# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def rock_paper_scissors(data):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # A와 B의 승리 횟수를 세기 위한 변수 a, b를 0으로 둔다.
    a = 0
    b = 0
    # 여러 경기가 담겨있는 리스트 data를 불러와 d로 하나씩 인덱싱한다.
    for d in data:
        # A가 가위일때
        if d[0] == 0:
            # B가 바위면, B의 승리 카운트를 1 올려주고
            if d[1] == 1:
                b += 1
            # B가 보이면, A의 승리 카운트를 1 올려준다.
            elif d[1] == 2:
                a += 1
        # 위와 같이 A가 승리할 경우, A의 승리 카운트를
        # B가 승리할 경우, B의 승리 카운트를 올려준다.
        elif d[0] == 1:
            if d[1] == 0:
                a += 1
            elif d[1] == 2:
                b += 1
        elif d[0] == 2:
            if d[1] == 1:
                a += 1
            elif d[1] == 0:
                b += 1
    # 게임이 끝났을 때, A의 승리 카운트가 크면 'A'를 반환
    if a > b:
        return 'A'    
    # B의 승리 카운트가 크면 'B'를 반환
    elif b > a:
        return 'B'
    # 승리 카운트가 동일한 경우 'draw'를 반환한다.
    else:
        return 'draw'

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(rock_paper_scissors([[0, 1], [1, 2], [2, 2]]))
    # B
    print(rock_paper_scissors([[0, 1], [1, 0]]))
    # draw