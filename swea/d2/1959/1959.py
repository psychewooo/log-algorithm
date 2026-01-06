# [SWEA-D2] 1959. 두 개의 숫자열

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0

    # 1. N = M인 경우 (두 숫자열의 길이가 동일한 경우)
    if N == M:
        for i in range(N):
            result += A[i] * B[i]

    # 2. N != M인 경우, 길이 비교 후 기준 판단
    if N > M:
        long_str = A
        short_str = B

    else:
        long_str = B
        short_str = A

    for i in range(len(long_str) - len(short_str) + 1):
        number_sum = 0

        for j in range(len(long_str) - len(short_str) + 1):
            number_sum += long_str[i + j] * short_str[j]
            print(number_sum)

            # if number_sum > result:
            #     number_sum = result
            #     print(number_sum)

    # print(f'#{tc} {result}')