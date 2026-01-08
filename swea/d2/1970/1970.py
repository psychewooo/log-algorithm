# [SWEA-D2] 1970. 쉬운 거스름돈

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

    # 주어진 N을 돈의 종류로 나누기
    # 나눌 수 없으면 count = 0
    # 나눌 수 있으면 그 몫을 넣고
    # 나머지를 다시 돈의 종류로 나누는 계산 반복

    i = 0

    while i < 8:
        # 몫이 0인 경우에는
        if N // money[i] == 0:
            i += 1

        # N // money[i] != 0
        else:
            count[i] = N // money[i]
            # N 값 갱신
            N = N % money[i]
            i += 1

    print(f'#{tc}')
    print(*count)