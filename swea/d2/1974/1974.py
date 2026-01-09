# [SWEA-D2] 1974. 스도쿠 검증

import sys

sys.stdin = open('input.txt')

# 총 테스트 케이스의 개수 T
T = int(input())

for tc in range(1, T + 1):


'''
Scenario
3 * 3 안과, 전체 행과 열에는 1~9의 숫자가 한 번씩만 들어갈 수 있음
겹치는 숫자가 없을 경우 정답으로 1을 출력
그렇지 않을 경우 0을 출력

1. 행 판별
2. 열 판별
3. 3 * 3 판별
'''