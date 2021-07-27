def get_final_position(N, mat, moves):
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                y = i
                x = j

    for M in moves:
        if M == 0:      # 위로 이동하는 경우
            y -= 1      # y의 인덱스가 작아짐으로 -1
        
        elif M == 1:    # 아래로 이동하는 경우
            y += 1      # y의 인덱스가 커짐으로 +1
        
        elif M == 2:    # 좌로 이동하는 경우
            x -= 1      # x의 인덱스가 작아짐으로 -1

        elif M == 3:           # 우로 이동하는 경우
            x += 1      # x의 인덱스가 커짐으로 +1

    return [x, y]

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