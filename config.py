
# DO NOT EDIT

# Assignment for 18cg11

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')
s1 = ((~P|~R)|~S)
s2 = ((~P|~R)&(~R|P))
s3 = ((S|~R)&(~S|~R))
s4 = ((R|P)|S)

s5 = ((~R>>(Q&~P))|~(~R|P))
s6 = ((P>>R)>>(Q|(~P&R)))
