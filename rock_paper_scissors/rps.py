#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scisors']
    pos_plays = [None] * (n^3)
    
    def rps(game, game_number):
        for i in range(len(plays)):
            game.append(plays[i])
            if game_number == n:
                pos_plays.append([i for i in game])
            else:
                rps(game, game_number + 1)
            game.pop()
    
    rps([], 1)
    return pos_plays
    
print(rock_paper_scissors(6))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
