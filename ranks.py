#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def single_rank(ranked, game):
    global_ranks = ranked + [game]
    global_ranks.sort(reverse=True)
    
    rank_index = 1
    rank_dict = {rank_index:global_ranks[0]}
    
    for elem in global_ranks:
        if elem in rank_dict.values():
            continue
        else:
            rank_index += 1
            rank_dict[rank_index] = elem
    
    return [k for k, v in rank_dict.items() if v == game]

def climbingLeaderboard(ranked, player):
    final_player_ranks = []
    for game in player:
        final_player_ranks = final_player_ranks + single_rank(ranked, game)
        
    return final_player_ranks


if __name__ == '__main__':
    ranked = [100, 90, 90, 75, 50]
    player = [25, 60, 80, 102]

    print(climbingLeaderboard(ranked, player), "5, 4, 3, 1")