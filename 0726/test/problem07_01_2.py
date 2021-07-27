# 동옥's
# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    x, y = position
    if M == 0:
        if (0 < x <= N) and (0 <= y <= N-1):
            return True
        return False
    
    elif M == 1:
        if (0 < x <=N) and (1 < y <= N):
            return True
        return False

    elif M == 2:
        if (0 < x <= N) and (0 < y <= N):
            return True
        return False
    
    else:
        if (0 <= x <= N-1) and (0 < y <= N):
            return True
        return False

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 0, (0, 0)))
    # False