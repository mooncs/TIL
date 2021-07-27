# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def rock_paper_scissors(data):
    win_a = 0
    win_b = 0

    for i in data:
        if i[0] - i[0] == 1 or i[0] - i[1] == -2:
            win_a += 1
        # elif:pass   
        #     win_b += 1

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(rock_paper_scissors([[0, 1], [1, 2], [2, 2]]))
    # B
    print(rock_paper_scissors([[0, 1], [1, 0]]))
    # draw