import math
import os
import random
import re
import sys
import heapq

# Complete the climbingLeaderboard function below.


def climbingLeaderboard(scores, alice):
    aliceFinal = []
    scores = list(set(scores))
    heapq.heapify(scores)
    # for i in range(len(alice)):
    #     if alice[i] not in list(scores):
    #         heapq.heappush(scores,alice[i])
    #     aliceFinal.append(list(scores).index(alice[i])+1)

    print(list(scores))

    return aliceFinal


if __name__ == '__main__':
    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
