#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        self.checker = checker
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        super().__init__(checker)

    def __repr__(self):
        hi ='Player ' + str(self.checker) + ' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
        return hi
    
    def max_score_column(self, scores):
        """takes a loist of scores and gives the column with the max score"""
        max_scores_list = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_scores_list += [i]
        if self.tiebreak == 'LEFT':
            return max_scores_list[0]
        if self.tiebreak == 'RIGHT':
            return max_scores_list[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(max_scores_list)
        
        def scores_for(self, board):
            scores = [50,50,50,50,50,50,50]
            count = 0
        
        
        
    def scores_for(self, board):
        ''' takes a Board and determines the called AIPlayer's
        scores for the columns in board
        '''
        scores = [50,50,50,50,50,50,50]

        for column in range(7):
            if board.can_add_to(column)==False:
                scores[column] = -1
            elif board.is_win_for(self.checker):
                scores[column] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[column] = 0
            elif self.lookahead == 0:
                scores[column] = 50
            else:
                board.add_checker(self.checker, column)
                other_player = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                other_scores = other_player.scores_for(board)
                if max(other_scores) == 0:
                    scores[column] = 100
                elif max(other_scores) == 100:
                    scores[column] = 0
                elif max(other_scores) == 50:
                    scores[column] = 50
                    
                board.remove_checker(column)
        return scores
    def next_move(self, board):
        ''' returns the  AIPlayer's judgement of its best possible move
        '''
        self.num_moves += 1
        scores = self.scores_for(board)
        return self.max_score_column(scores)
            
        
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        