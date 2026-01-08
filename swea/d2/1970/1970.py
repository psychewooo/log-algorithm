# [SWEA-D2] 1970. 쉬운 거스름돈
    '''
    Scenario
    1. 주어진 N을 돈의 종류로 나누기
    2-1. 나눌 수 없으면 count = 0
    2-2. 나눌 수 있으면 count = 몫
    3. 나머지를 다시 돈의 종류로 나누기
    반복
    '''

import sys

sys.stdin = open('input.txt')

# 테스트 케이스의 개수 T
T = int(input())

for tc in range(1, T + 1):
    # 손님에게 거슬러 주어야 할 금액 N
    N = int(input())

    # 마켓에서 사용하는 돈의 종류
    # 높은 돈을 우선적으로 계산하기 위해 큰 금액을 리스트의 앞에 둔다.
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    # 필요한 돈의 개수
    count = [0] * 8

    i = 0

    while i < 8:
        # 몫이 0인 경우, 다음 종류로 넘어가기
        if N // money[i] == 0:
            i += 1

        else:
            count[i] = N // money[i]
            # 다음 계산을 위해 N 값 갱신
            N = N % money[i]
            i += 1

    # 형식에 맞게 출력
    print(f'#{tc}')
    print(*count)