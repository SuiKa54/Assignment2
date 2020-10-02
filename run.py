
from lib204 import wff, semantic_interface

try:
    from config import *
except:
    try:
        from .config import *
    except:
        print("\n\tYou must download your config.py file first. See the assignment details in OnQ.\n")
        exit(1)



# First step: run this file (python run.py), and see the output.
print('\nFormulae for Question 1:')
print(" s1: %s" % s1)
print(" s2: %s" % s2)
print(" s3: %s" % s3)
print(" s4: %s" % s4)

print('\nFormulae for Question 2:')
print(" s5: %s" % s5)
print(" s6: %s" % s6)

################################################################################
# Question 1
#  Given the following logical sentences,
#   (a) write the truth table for each of them,
#   (b) determine which ones are equivalent (i.e., have the same truth table),
#   (c) find a model satisfied by one formula, but none of the others


# (a) Put the truth tables (text file, written on paper + picture, whatever)
#     into the Q1a folder

# (b) Variable q1b should be a list of lists that group together the equivalent
#     theories. These are two wrong answers, but they give you an idea of how
#     to write your response.

q1b = [ [s1],[s4],[s2,s3] ] # they are all equivalent.
#q1b = [ [s1], [s2], [s3], [s4] ] # they are all different
#q1b = ??? # the right answer please!

# (c) Variable q1c should be a dictionary mapping variables to True or False.
#     Use only what you need of P, Q, R, S, T. An example (almost certainly
#     incorrect) answer is given as an example.
q1c = {
    P: True,
    R: True,
    S: True
}



################################################################################
# Question 2
# Given the following logical sentences,
#  (a) [optional, but recommended] write the parse tree for each of them
#  (b) convert them to negation normal form
#  (c) convert them to CNF using distribution and de Morgan's rules
#  (d) encode them using the Tseitin encoding

print("\n\nCopy these two lines for Question 2:")
print("s5 = %s" % s5.dump('python'))
print("s6 = %s" % s6.dump('python'))

# replace the following two lines with what the above code prints
s5 = ((~R>>(Q&~P))|~(~R|P))
s6 = ((P>>R)>>(Q|(~P&R)))

# (a) Put the parse trees inside folder Q2a. You can do it on paper and take a
#     photo, or use drawing software. This will not be marked unless requested,
#     but the quiz will ask a similar question that /will/ be marked.

# (b) Copy s5 and s6 formulae into the first steps below, and show the steps to
#     convert to negation normal form. An example is given, but it is the wrong
#     starting formula. You /must/ provide an explanation for each step. Possible
#     explanations might include (exact wording is not required)...
#      - starting formula
#      - de Morgans
#      - distribution
#      - replace implications
#      - double negation
#      - etc.

s5nnf = [
    [(~R>>(Q&~P))|~(~R|P), 'starting formula'],
    [(~R>>(Q&~P))|(R&~P), 'right side: de Morgans, double negation elimination.'],
    [R|(Q&~P)|(R&~P), ' Left side: replace implication, double negation elimination']
]

s6nnf = [
    [(P>>R)>>(Q|(~P&R)), 'starting formula'],
    [~(P>>R)|(Q|(~P&R)),'replace implication'],
    [~(~P|R)|(Q|(~P&R)),'replace implication'],
    [(P&~R)|Q|(~P&R),'de Morgans, double negation elimination']
]


# (c) Copy s5 and s6 formulae into the first steps below, and show the steps to
#     convert to CNF using distribution, de Morgan's, implication removal, etc.
#     An example is given, but it is for the wrong formula. You /must/ provide
#     an explanation for each step. Possible explanations are listed above.

s5cnf = [
    [(R|(Q&~P))|(R&~P), 'negation normal form'],
    [((Q|R)&(~P|R))|(R&P), 'distribution'],
    [((R&~P)|(R|Q))&((R&~P)|(R|~P)),'distirbution'],
    [(R|Q|R)&(R|Q|~P)&(R|~P|R),'distribution'],
    [(Q|R)&(R|Q|~P)&(~P|R),'remove relicates'],
    [(Q|R)&(~P|R),'middle part is redundant']
]

s6cnf = [
    [(P&~R)|Q|(~P&R), 'negation normal form'],
    [((Q|P)&(Q|~R))|(~P&R), 'distribution'],
    [(Q|P|(~P&R))&(Q|~R|(~P&R)),'distribution'],
    [(Q|((P|~P)&(P|R)))&(Q|((~R|~P)&(~R|R))),'distribution on both side'],
    [(Q|P|R)&(Q|~R|~P),'replace(~R|R),(P|~P) with true first, then distribution']
]


# (d) Build the Tseitin encoding of both s5 and s6 using the semantic_interface
#     library to create auxiliary variables as necessary. Examples for different
#     formulae are given. There is a limit of one operator per auxiliary variable,
#     and you may re-use auxiliary variables as necessary.

# s5 = ((~R>>(Q&~P))|~(~R|P))
s5tseitin = semantic_interface.Encoding()
# first argument is the formula; second is the variable name.
x1 = s5tseitin.tseitin(~R, 'x1')
x2 = s5tseitin.tseitin(~P, 'x2')
x3 = s5tseitin.tseitin(x1|P, 'x3')
x4 = s5tseitin.tseitin(x2&Q, 'x4')
x5 = s5tseitin.tseitin(x1>>x4, 'x5')
x6 = s5tseitin.tseitin(~x3, 'x6')
x7 = s5tseitin.tseitin(x5|x6, 'x7')
# This final step is required -- use your last variable, corresponding to the top
#  of the parse tree, to finalize your Tseitin encoding.
s5tseitin.finalize(x7)

# s6 = ((P>>R)>>(Q|(~P&R)))
s6tseitin = semantic_interface.Encoding()
x1 = s6tseitin.tseitin(~P, 'x1')
x2 = s6tseitin.tseitin(x1&R, 'x2')
x3 = s6tseitin.tseitin(Q|x2, 'x3')
x4 = s6tseitin.tseitin(P>>R, 'x4')
x5 = s6tseitin.tseitin(x4>>x3, 'x5')
s6tseitin.finalize(x5)



print()
