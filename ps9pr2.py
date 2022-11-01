#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:27:45 2021

@author: marilynrisinger
"""

#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class
#  

from ps9pr1 import Board

# write your class below.
class Player:
    def __init__(self,checker):
        """constructs a new Player by initializing an attribute checker and
        an attribute num_moves"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
       
    def __repr__(self):
        """returns a string representing a Player object. the string returned
        should indicate which checker the Player object is using"""
        c = 'Player ' + self.checker
        return c
   
    def opponent_checker(self):
        """figures out the opponents checker by choosing the opposite checker"""
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'
       
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns the
        column where the player wants to make the next move"""
        while True:
            column = input('Enter a column: ')
            if column in "0123456":
                col_num = int(column)
                if b.can_add_to(col_num):
                    self.num_moves+=1
                    return col_num
            print('Try again!')

