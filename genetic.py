import random
import time

rows = 'ABCDEF'
cols = '123456'

"""
For each slot：
column = 5， row = 5， block = 2 total = 5+5+2 = 12
36 slots。
Max score is 12*36 = 432
"""
max_score = 432

"""
set var_rate
set quan
set times
"""
var_rate = 0.01
quan = 100
times = 50

"""
--------------------------------------------------------------------------------
Preparation part.
--------------------------------------------------------------------------------

"""
def cross(a, b):
    return [s+t for s in a for t in b]
# slot index
boxes = cross(rows, cols)
# row, column, square units
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF') for cs in ('12','34','56')]
unitlist = row_units + column_units + square_units
# unit
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
# each unit's peer
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
#arc consistency calc tims initalized by 0
#
#

"""
--------------------------------------------------------------------------------
Display part.
--------------------------------------------------------------------------------
"""

#Input: sudolu dict
#Output: display on screen
def display(values):
    width = 1 + 1
    line = '+'.join(['-' * (width * 2)] * 3)
    for r in rows: 
        print(''.join(str(values[r+c]).center(width) + ('|' if c in '24' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

#Input: sudoku string
#Output: sudoku dict
#        Keys: 'A1'
#        Values: '8' or "."
def grid_values(grid):
    chars = []
    digits = '123456'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append("-")
    assert len(chars) == 36
    return dict(zip(boxes, chars))
"""
--------------------------------------------------------------------------------
Display part finished.
--------------------------------------------------------------------------------
"""

"""
--------------------------------------------------------------------------------
Preparation part.
--------------------------------------------------------------------------------

"""
#Input: sudoku string
#Output: sudoku dict.
def combine_to_dict(combine):
    chars = []
    for c in combine:
            chars.append(c)
    assert len(chars) == 36
    return dict(zip(boxes, chars))

# input: puzzle string.
# output: a possibility string for empty slots.
def a_possibility(grid):
    row = 6
    col = 6
    poss = []
    sign_array = [0,0,0,0,0,0]
    for r in range(0,row):
        for c in range(0,col):
            # it is a known number.
            if grid[r*6+c] != '.':
                sign_array[int(grid[r*6+c],10)-1] = 1
        for count in range(0,col):
            if sign_array[count] == 0:
                poss.append(count+1)
        sign_array = [0,0,0,0,0,0]	
    return poss

# input: puzzle string.
# output: random string for empty slots.
def random_generate(grid):
    row = 6
    col = 6
    poss = []
    for r in range(0,row):
        for c in range(0,col):
            if grid[r*6+c] == ".":
                poss.append(random.randint(1,6))
    return poss

# input: puzzle string, a possibility string for empty slots.
# output: a complete string for this solution.(no '.', all are # from 1-6.)
def combination(grid, poss):
    combine = []
    poss_counter = 0
    for c in range(0,len(grid)):
        if grid[c] != '.':
            combine.append(int(grid[c]))
        else:
            combine.append(poss[poss_counter])
            poss_counter += 1
    return combine            

# function name: evaluation()
# input: combine dict.
# output: evaluation value.
def evaluation(dic):
    score = 0
    for elm in dic.keys():
        for peer in peers[elm]:
            if dic[elm] == dic[peer]:
                score += 1
    return score

# container for 100 members.
# inout: puzzle string(grid).
# output: generate 1st 100 poss members.
def population(grid):
    poss = []
    for c in range(0,quan):
        poss.append(random_generate(grid))
    return poss

"""
Preparation part finished.

"""
"""
--------------------------------------------------------------------------------
Generation part.
--------------------------------------------------------------------------------

"""
def choose_parents(p1,p2):
    finish = False
    while finish == False:
        rand_p1_number = random.randint(0,quan-1)
        p2_flag = False
        while p2_flag == False:
            temp = random.randint(0,quan-1)
            if temp != rand_p1_number:
                p2_flag = True
                finish = True
            #else:
                #print("repeat")
        rand_p2_number = temp
    p1 = rand_p1_number
    p2 = rand_p2_number
    #print(p1,p2)
    return p1,p2

# generate 2 sons that finished crossover and variation.
# input: 2 parents, p1, p2(poss)
# ouput: 2 sons, s1, s2(poss)
def generate(p1,p2,len):
    
    # choose crossover point.
    pos = random.randint(1,len)
    # crossover.
    var = 0
    for var in range(0,pos):
        temp_value = p1[var]
        p1[var] = p2[var]
        p2[var] = temp_value
    # new p1 and p2 before variation.
    # do variation for new p1 and p2
    var = 0
    for var in range(0,len):
        x1 = random.random()
        if x1 < var_rate:
            p1[var] = random.randint(1,6)
        x2 = random.random()
        if x2 < var_rate:
            p2[var] = random.randint(1,6)
    # variation finished.
    return p1,p2

#
#
#
def process(grid,poss,new_poss):
    score = []
    prob = []
    s1 = []
    s2 = []
    count = 0
    for each in poss: #from 0 to quan-1
        sco = evaluation(combine_to_dict(combination(grid,each)))
        #print(sco)
        score.append(sco)
        prob.append(round(sco/max_score,3))
        """
	now, we have poss_dict, score_dict, prob_dict
	"""
    #print(score)
    #print("Last generation, best result on violated constraints are "+ str(min(score)))
    while count < quan//2:
        flag = False
        while flag == False:
            p1 = 0
            p2 = 0
            (p1,p2) = choose_parents(p1,p2)
            #clone
            temp1 = poss[p1][:]
            temp2 = poss[p2][:]
            if prob[p1]*prob[p2] < random.random():
                (s1,s2) = generate(temp1,temp2,len(poss[p1]))
                count += 1
                flag = True
        new_poss.append(s1)
        new_poss.append(s2)
    """
    ### test.
    new_score = []
    for each in new_poss:
        sco = evaluation(combine_to_dict(combination(grid,each)))
        new_score.append(sco)
    print(new_score)
    ### test finished.
    """
    
    """
    choose smaller quan members from old and new, to evolve.
    """
    double_poss = []
    for each in poss:
        double_poss.append(each)
    for each in new_poss:
        double_poss.append(each)
    double_score = []
    for each in double_poss:
        sco = evaluation(combine_to_dict(combination(grid,each)))
        double_score.append(sco)
    #print(double_score)
    i = 0
    while i < quan:
        index = 0
        for each in double_score:
            if each == min(double_score):
                break
            else:
                index += 1
        double_score[index] = max_score
        poss[i] = double_poss[index]
        i += 1
    # old = new, new = []
    
    ### test.
    new_score = []
    for each in poss:
        sco = evaluation(combine_to_dict(combination(grid,each)))
        new_score.append(sco)
    #print(new_score)
    ### test finished.
    
    new_poss = []
    return poss,new_poss

#
#
#
def test(grid,poss):
    solution = []
    for each in poss:
        test_sco = evaluation(combine_to_dict(combination(grid,each)))
        if test_sco == 0:
            solution = each
            break
    if solution != []:
        return True,solution
    else:
        return False,solution

#
#
#
"""
--------------------------------------------------------------------------------
Generation part finished.
--------------------------------------------------------------------------------

"""
"""
--------------------------------------------------------------------------------
Run part.
--------------------------------------------------------------------------------

"""
def run(grid,time):
    solu = []
    it = 0
    poss = population(grid)
    new_poss = []
    flag = False
    while it < time:
        (poss,new_poss) = process(grid,poss,new_poss)
        (flag,solu) = test(grid,poss)
        #print(solu)
        if flag == True:
            break
        else:
            it += 1
    if it == time :
        print("failed to get a solution in "+str(time)+" times")
    else:
        print("Total generate times: "+str(it))
        print("One solution is:")
        display(combine_to_dict(combination(grid,solu)))
        

"""
--------------------------------------------------------------------------------
Run part finished.
--------------------------------------------------------------------------------
"""


"""
Main
"""

#grid = "1..3.625.6....4.124..2.5.26....3.421"
#grid = "1..3..2.......4.1.4..2...26.......21"
grid = "...3..2.......4......2.5.26........."

print("Sudoku puzzle is:")
display(grid_values(grid))
run(grid,times)

