# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def get_final_position(N, mat, moves):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    down = 0
    up = 0
    left = 0
    right = 0
    for M in moves:
        if M == 0:
            down += 1
        elif M == 1:
            up += 1
        elif M == 2:
            left += 1
        elif M == 3:
            right +=1


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    N = 3
    mat = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ] 
    moves1 = [1, 1, 3]
    print(get_final_position(N, mat, moves1))
    # [1, 2]
    
    moves2 = [1, 3, 3]
    print(get_final_position(N, mat, moves2))
    # [2, 1]