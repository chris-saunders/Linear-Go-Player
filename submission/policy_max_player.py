#!/usr/bin/python3
from mcts import MCTS
from gtp_connection import GtpConnection
import argparse
import numpy as np

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
        self.name = "Policy Max Player"
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
        i = 0
        return gammas[0][1]


if __name__=='__main__':
    c = GtpConnection(Go6Player(num_simulation))
    c.start_connection()

