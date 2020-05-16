# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:59:23 2019

@author: Taylor
"""

from naiveBayesDensity import *
import pprint
d = Classifier("haberman.txt", ("num\tnum\tnum\tclass"))
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
print(d.classify([],[30, 50, 3]))