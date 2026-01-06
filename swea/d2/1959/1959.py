# [SWEA-D2] 1959. 두 개의 숫자열

import sys

sys.stdin = open('input.txt')

# 테스트 케이스의 개수
T = int(input())

for tc in range(1, T + 1):
    # 숫자열 A의 길이 N, 숫자열 B의 길이 M
    N, M = list(map(int, input().split()))

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = float('-inf')

    # 1. N = M인 경우
    # 두 숫자열의 길이가 동일한 경우
    if N == M:
        number_sum = 0

        for i in range(N):
            number_sum += A[i] * B[i]

        result = number_sum

    # 2. N != M인 경우
    else:
        if N > M:
            long_str = A
            short_str = B

        else:
            long_str = B
            short_str = A

        for i in range(len(long_str) - len(short_str) + 1):
            number_sum = 0

            for j in range(len(short_str)):
                number_sum += long_str[i + j] * short_str[j]

            result = max(result, number_sum)

        print(f'#{tc} {result}')