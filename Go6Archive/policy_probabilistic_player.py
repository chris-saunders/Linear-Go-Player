#!/usr/bin/python3
from mcts import MCTS
from gtp_connection import GtpConnection
import argparse
import numpy as np
import random

parser = argparse.ArgumentParser(description='Process Arguments for number of simulation')
parser.add_argument('-s', '--sim', type=int, nargs='?', default = 200, help='define number of simulations for each legal move, #playout --> sim*num_of_legal_moves')
args = parser.parse_args()
num_simulation = args.sim

class Go6Player():
    def __init__(self, num_simulation = 200, limit=100, exploration = 0.01):
        """
        Player that selects a move based on MCTS from the set of legal moves

        Parameters
        ----------
        name : str
            name of the player (used by the GTP interface).
        version : float
            version number (used by the GTP interface).
        """
        self.name = "Policy Probabilistic Player"
        self.version = 0.1
        self.MCTS= MCTS()
        self.rate = 0.1
        self.num_simulation = num_simulation
        self.limit = limit
        self.exploration = exploration 
        
    def policy(self,board,color):
        return GoBoardUtil.generate_move_with_filter(board,pattern,check_selfatari)

    def run(self, board, color, print_info=False):
        self.MCTS.exploration = self.exploration
        self.MCTS.limit = self.limit
        self.MCTS.toplay = color
        self.MCTS.pattern = True
        self.MCTS.selfatari = True

        for n in range(self.num_simulation):
            board_copy = board.copy()
            self.MCTS._playout(board_copy, color)

        if print_info:
            self.MCTS.good_print(board, self.MCTS._root, color,self.num_nodes)
    
    def reset(self):
        self.MCTS = MCTS()

    def update(self, move):
        self.MCTS.update_with_move(move)

    def verify_weights(self, distribution):
        epsilon = 0.000000001 # allow small numerical error
        sum = 0.0
        for i in range(len(distribution)):
            sum += distribution[i][0]
        assert abs(sum - 1.0) < epsilon

    def random_select(self, distribution):
        r = random.random();
        sum = 0.0
        for i in range(len(distribution)):
            sum += distribution[i][0]
            if sum > r:
                return distribution[i][1]
        return distribution[-1] # some numerical error, return last element
    
    def get_move(self, board, color):
        from feature import Features_weight, Feature
        moves = board.get_empty_points()
        gammas = []
        gammasum = 0
        for move in moves:
            if board.check_legal(move, board.current_player) and not board.is_eye(move, board.current_player):
                features = Feature.find_move_feature(board, move)
                gamma = Feature.compute_move_gamma(Features_weight, features)
                gammasum += gamma
                gammas.append([gamma,move])
        gammas.sort(reverse = True)
        answer = []
        for item in gammas:
            sum = (item[0]/gammasum)
            answer.append((sum,item[1]))
        self.verify_weights(answer)
        item = self.random_select(answer)
        return item




if __name__=='__main__':
    c = GtpConnection(Go6Player(num_simulation))
    c.start_connection()

