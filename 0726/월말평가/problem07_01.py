# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 이동한 위치를 담을 new_position을 0으로 둔다.
    new_position = 0
    # 캐릭터가 위로 움직인다면 현위치의 x좌표를 -1해서 위로 한 칸 움직인다.
    if M == 0:
        new_position = position[0]-1
    # 캐릭터가 아래로 움직인다면 현위치의 x좌표를 +1해서 아래로 한 칸 움직인다.
    elif M == 1:
        new_position = position[0]+1
    # 캐릭터가 좌로 움직인다면 현위치의 y좌표를 -1해서 좌로 한 칸 움직인다.
    elif M == 2:
        new_position = position[1]-1
    # 캐릭터가 우로 움직인다면 현위치의 y좌표를 +1해서 우로 한 칸 움직인다.
    elif M == 3:
        new_position = position[1]+1
    # 상하 또는 좌우를 한 번만 움직이기 때문에 상하나 좌우 둘 중 하나가
    # 2차원 평면의 범위인(N*N)을 벗어나거나,
    # 최소 범위인 0을 벗어날 경우 False를 반환
    if new_position>N or new_position<0:
        return False
    # 그렇지 않으면 True를 반환
    return True


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 0, (0, 0)))
    # False