T = int(input())
for tc in range(1, T+1):
    # 총 방의 수 
    N = int(input())
    # 쌓여 있는 박스의 수
    boxes = list(map(int, input().split()))
    # 제일 큰 낙차를 담을 변수
    max_gravity = 0
    for n in range(N-1):
        gravity = 0
        for m in range(n+1, N):
            # 현재의 박스 높이가 다음 박스의 높이보다 높을 때, 낙차 1증가
            if boxes[n] > boxes[m]:
                gravity += 1
        # 최종적으로 구한 낙차가 제일 큰 낙차보다 크다면, max_gravity 갱신
        if gravity > max_gravity:
            max_gravity = gravity
    
    print('#{} {}'.format(tc, max_gravity))

# # 2
# T = int(input())

# for tc in range(1, T+1):
#     # 박스의 수
#     N = int(input())
#     box = list(map(int, input().split()))

#     ans = 0

#     # 모든 박스 비교
#     for i in range(N):
#         cnt = 0

#         # 나 다음부터 나보다 작은 값을 찾아 카운트
#         for j in range(i+1, N):
#             if box[i] > box[j]:
#                 cnt += 1

#         if ans < cnt:
#             ans = cnt
        
#     print('#{} {}'.format(tc, ans))