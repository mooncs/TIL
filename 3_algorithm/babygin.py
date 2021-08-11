# sample_imput불러오기
# import sys
# sys.stdin = open("sample_input.txt", "r")


for tc in range(int(input())):
    numbers=[int(number) for number in input().strip()]
    num_count = [0]*10
    # 입력받은 수에서 0~9의 횟수를 카운트한다.
    for number in numbers:
        num_count[number] += 1
    
    check = 0
    for i in range(8):
        # 한 가지 숫자가 6번 나온다면, triplet이 2개인 babygin이므로 반복문을 나가고 1출력
        if num_count[i] == 6:
            check += 2
            break
        # 한 가지 숫자가 3번보다 많이 나온다면, triplet이 1개->check에 1을 추가
        elif num_count[i] >= 3:
            num_count[i] -= 3
            check += 1
        # 연속하는 세 수를 비교하여 모두 2번씩 나온다면, run이 2개인 babygin이므로 반복문을 나가고 1출력
        if num_count[i] == 2 and num_count[i+1] == 2 and num_count[i+2] == 2:
            check += 2
            break
        # 연속하는 세 수를 비교하여 모두 1번 이상 나온다면 run이 1개->check에 1을 추가하고 count를 한번씩 제거한다.
        elif num_count[i] >= 1 and num_count[i+1] >= 1 and num_count[i+2] >= 1:
            num_count[i] -= 1
            num_count[i+1] -= 1
            num_count[i+2] -= 1
            check += 1
        
    # run과 triplet의 합이 2미만이면 babygin이 아니므로 0출력, 아니면 1출력
    if check < 2:
        print('#{} 0'.format(tc+1))
    else:
        print('#{} 1'.format(tc+1))




# 2
# def my_max(*args): #가장 큰 숫자 찾기
#     num=args[0]
#     for i in args:
#         if i>num:
#             num=i
#     return num
 
# T=int(input())
 
# for i in range(T):
#     cnt_run = 0 #새로운 케이스를 시작할때 초기화
#     cnt_triplet = 0
#     num_list=list(map(int,input().strip()))
#     max_num=my_max(*num_list)
#     count_list = [0] *(max_num+3) #0부터 max_num+2 의 크기인 리스트 만들기
#     for j in num_list: #해당하는 숫자의 인덱스에 들어가서 +1
#         count_list[j]+=1
#     for j in range(max_num+1): # max_num까지 순회
#         while 1: # 같은 자리에서 중복해서 run을 가질 수 있기 때문에 while문 순회
#             if count_list[j]>=1 and count_list[j+1]>=1 and count_list[j+2]>=1:
#                 cnt_run+=1
#                 count_list[j] -= 1
#                 count_list[j + 1] -= 1
#                 count_list[j + 2] -= 1
#             elif count_list[j]>=3:
#                 cnt_triplet+=1
#                 count_list[j]-=3
#             else: #triplet과 run 둘다 없을 경우 while문 탈출
#                 break
 
#     if cnt_triplet+cnt_run>=2:
#         print('#{} {}'.format(i+1,1))
#     else:
#         print('#{} {}'.format(i + 1, 0))



# 3
# def BabyGin(cards):
#     if cards[0]==cards[1]==cards[2]:
#         return True
#     elif cards[0]+2==cards[1]+1==cards[2]:
#         return True
#     else:
#         return False
 
# def BubbleSort(lst):
#     N = len(lst)
#     for n in range(N - 1, 0, -1):
#         for i in range(n):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#     return lst
 
# T = int(input())
# for tc in range(T):
#     cards = [int(i) for i in input().strip()]

#     sc = BubbleSort(cards)  # sc: sorted cards
#     card_1 = sc[0:3]
#     card_2 = sc[3:6]
 
#     result_1 = BabyGin(card_1)
#     result_2 = BabyGin(card_2)
 
#     print("#{} {}".format(tc+1, result_1*result_2))