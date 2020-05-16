# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:59:23 2019

@author: Taylor
"""

from naiveBayesBasic import *
import pprint
d = Classifier("krkopt.txt", ("attr\tattr\tattr\tattr\tattr\tattr\tclass"))
pprint.pprint(d.prior)
# =============================================================================
# 7. Attribute Information:
#    1. White King file (column)
#    2. White King rank (row)
#    3. White Rook file
#    4. White Rook rank
#    5. Black King file
#    6. Black King rank
#    7. optimal depth-of-win for White in 0 to 16 moves, otherwise drawn
# 	{draw, zero, one, two, ..., sixteen}.
# =============================================================================
print("White King File Column: B, Rank: 2. White Rook File: A, rank: 7. Black King File: B, rank 7")
pprint.pprint("Predicted turns required to win: " + d.classify(["a", "1", "b", "2", "d", "7"]))