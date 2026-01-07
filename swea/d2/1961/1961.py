# [SWEA-D2] 1961. 숫자 배열 회전

import sys

sys.stdin = open('input.txt')

# 테스트 케이스의 개수 T
T = int(input())

for tc in range(1, T + 1):
    # 행렬의 크기 N
    N = int(input())

    arr = []

    for _ in range(N):
        input_arr = list(map(int, input().split()))
        arr.append(input_arr)

    # 90도 회전
    arr_90 = list(zip(*arr[::-1]))

    # 180도 회전
    arr_180 = list(zip(*arr_90[::-1]))

    # 270도 회전
    arr_270 = list(zip(*arr_180[::-1]))

    print(f'#{tc}')
    for i in range(N):
        # 90도, 180도, 270도 하나씩
        print(''.join(map(str, arr_90[i])), ''.join(map(str, arr_180[i])), ''.join(map(str, arr_270[i])))