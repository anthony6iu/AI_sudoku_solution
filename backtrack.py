rows = 'ABCDEF'
cols = '123456'
digits = '123456'
# nodes visited # initialized with 0
count = 0

def cross(a,b):
    return [s+t for s in a for t in b]
boxes = cross(rows,cols)
# row, column, square units
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF') for cs in ('12','34','56')]
unitlist = row_units + column_units + square_units
# unit
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
# each unit's peer
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
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
#Input: sudoku string.
#Output: sudoku dict.
def grid_to_dict(grid):
    chars = []
    for char in grid:
        if char == '.':
            chars.append(digits)
        if char in digits:
            chars.append(char)
    assert len(chars) == 36
    return dict(zip(boxes,chars))
"""
--------------------------------------------------------------------------------
Preparation part finished.
--------------------------------------------------------------------------------
"""
"""
--------------------------------------------------------------------------------
Backtrack part.
--------------------------------------------------------------------------------
"""
#Input: sudoku dict.
#Output: a solution.
def backtrack(dic,flag,count):
    save = dic
    temp = dic
    target = choose(dic)
    for var in save[target]:
        temp[target] = var
        if check(temp) == True and finish_choose(temp) == True:
            return temp,True,count
        if check(temp) == False:
            continue
        if check(temp) == True and finish_choose(temp) == False:
            flag2 = True
            count += 1
            save,flag2,count = backtrack(temp,flag2,count)
            if flag2 == False:
                continue
            else:
                return temp,True,count
    save[target] = '123456'
    return save,False,count
           
    
def choose(dic):
    for key in dic.keys():
        if len(dic[key]) > 1:
            break
    return key
#Input: partical finished p_sdict.
#Output: consistency : True ; violated : False.
def check(p_sdict):
    for key in p_sdict.keys():
        if len(p_sdict[key]) == 1:
            for peer in peers[key]:
                if len(p_sdict[peer]) == 1 and p_sdict[key] == p_sdict[peer]:
                    return False
    return True

#Input: p_sdict
#Output: no undecided slot : True ; still undecided slot : False
def finish_choose(p_sdict):
    for key in p_sdict.keys():
        if len(p_sdict[key]) > 1:
            return False
    return True
"""
--------------------------------------------------------------------------------
Backtrack part finished.
--------------------------------------------------------------------------------
"""
"""
--------------------------------------------------------------------------------
Run part.
--------------------------------------------------------------------------------
"""
#grid = "1..3.625.6....4.124..2.5.26....3.421"
#grid = "1..3..2.......4.1.4..2...26.......21"
grid = "...3..2.......4......2.5.26........."
print("Puzzle is:")
display(grid_values(grid))
s_dict = grid_to_dict(grid)
flag = False
(solu,flag,count) = backtrack(s_dict,flag,count)
print("After visit "+str(count)+" nodes:")
print("A backtrack solultion for puzzle above is: ")
display(solu)










































