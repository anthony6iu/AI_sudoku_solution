For arc, backtrack and genetic, three different algorithms:
I produce 3 different puzzles, which known slots less and less:
1.
1 - - 3 - 6
2 5 - 6 - -
- - 4 - 1 2
4 - - 2 - 5
- 2 6 - - -
- 3 - 4 2 1

grid = "1..3.625.6....4.124..2.5.26....3.421"

2.
1 - - 3 - -
2 - - - - -
- - 4 - 1 -
4 - - 2 - -
- 2 6 - - -
- - - - 2 1

grid = "1..3..2.......4.1.4..2...26.......21"

3.
- - - 3 - -
2 - - - - -
- - 4 - - -
- - - 2 - 5
- 2 6 - - -
- - - - - -

grid = "...3..2.......4......2.5.26........."

compute each puzzle by each algorithm.


:::::::::::::::::::::::::::::RESULTS::::::::::::::::::::::::::::::;


#ARC#


Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /Users/hongchiliu/Desktop/arc.py =================
Puzzle is:
1 - |- 3 |- 6 
2 5 |- 6 |- - 
- - |4 - |1 2 
----+----+----
4 - |- 2 |- 5 
- 2 |6 - |- - 
- 3 |- 4 |2 1 
----+----+----
After reduced 84 arc constraints:
and visited 5 nodes(backtrack step):
An Arc consistency solultion for puzzle above is: 
1 4 |2 3 |5 6 
2 5 |1 6 |3 4 
3 6 |4 5 |1 2 
----+----+----
4 1 |3 2 |6 5 
5 2 |6 1 |4 3 
6 3 |5 4 |2 1 
----+----+----
>>> 
================= RESTART: /Users/hongchiliu/Desktop/arc.py =================
Puzzle is:
1 - |- 3 |- - 
2 - |- - |- - 
- - |4 - |1 - 
----+----+----
4 - |- 2 |- - 
- 2 |6 - |- - 
- - |- - |2 1 
----+----+----
After reduced 75 arc constraints:
and visited 35 nodes(backtrack step):
An Arc consistency solultion for puzzle above is: 
1 4 |2 3 |5 6 
2 5 |1 6 |3 4 
3 6 |4 5 |1 2 
----+----+----
4 1 |3 2 |6 5 
5 2 |6 1 |4 3 
6 3 |5 4 |2 1 
----+----+----
>>> 
================= RESTART: /Users/hongchiliu/Desktop/arc.py =================
Puzzle is:
- - |- 3 |- - 
2 - |- - |- - 
- - |4 - |- - 
----+----+----
- - |- 2 |- 5 
- 2 |6 - |- - 
- - |- - |- - 
----+----+----
After reduced 62 arc constraints:
and visited 38 nodes(backtrack step):
An Arc consistency solultion for puzzle above is: 
1 4 |2 3 |5 6 
2 3 |5 6 |1 4 
5 6 |4 1 |2 3 
----+----+----
4 1 |3 2 |6 5 
3 2 |6 5 |4 1 
6 5 |1 4 |3 2 
----+----+----
>>> 




#BACKTRACK#


Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: /Users/hongchiliu/Desktop/backtrack.py ==============
Puzzle is:
1 - |- 3 |- 6 
2 5 |- 6 |- - 
- - |4 - |1 2 
----+----+----
4 - |- 2 |- 5 
- 2 |6 - |- - 
- 3 |- 4 |2 1 
----+----+----
After visit 17 nodes:
A backtrack solultion for puzzle above is: 
1 4 |2 3 |5 6 
2 5 |1 6 |3 4 
3 6 |4 5 |1 2 
----+----+----
4 1 |3 2 |6 5 
5 2 |6 1 |4 3 
6 3 |5 4 |2 1 
----+----+----
>>> 
============== RESTART: /Users/hongchiliu/Desktop/backtrack.py ==============
Puzzle is:
1 - |- 3 |- - 
2 - |- - |- - 
- - |4 - |1 - 
----+----+----
4 - |- 2 |- - 
- 2 |6 - |- - 
- - |- - |2 1 
----+----+----
After visit 35 nodes:
A backtrack solultion for puzzle above is: 
1 4 |2 3 |5 6 
2 5 |1 6 |3 4 
3 6 |4 5 |1 2 
----+----+----
4 1 |3 2 |6 5 
5 2 |6 1 |4 3 
6 3 |5 4 |2 1 
----+----+----
>>> 
============== RESTART: /Users/hongchiliu/Desktop/backtrack.py ==============
Puzzle is:
- - |- 3 |- - 
2 - |- - |- - 
- - |4 - |- - 
----+----+----
- - |- 2 |- 5 
- 2 |6 - |- - 
- - |- - |- - 
----+----+----
After visit 38 nodes:
A backtrack solultion for puzzle above is: 
1 4 |2 3 |5 6 
2 3 |5 6 |1 4 
5 6 |4 1 |2 3 
----+----+----
4 1 |3 2 |6 5 
3 2 |6 5 |4 1 
6 5 |1 4 |3 2 
----+----+----
>>> 



#GENETIC#


Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

=============== RESTART: /Users/hongchiliu/Desktop/genetic.py ===============
Sudoku puzzle is:
1 - |- 3 |- 6 
2 5 |- 6 |- - 
- - |4 - |1 2 
----+----+----
4 - |- 2 |- 5 
- 2 |6 - |- - 
- 3 |- 4 |2 1 
----+----+----
Total generate times: 41
One solution is:
1 4 |2 3 |5 6 
2 5 |1 6 |4 3 
3 6 |4 5 |1 2 
----+----+----
4 1 |3 2 |6 5 
5 2 |6 1 |3 4 
6 3 |5 4 |2 1 
----+----+----
>>> 
=============== RESTART: /Users/hongchiliu/Desktop/genetic.py ===============
Sudoku puzzle is:
1 - |- 3 |- - 
2 - |- - |- - 
- - |4 - |1 - 
----+----+----
4 - |- 2 |- - 
- 2 |6 - |- - 
- - |- - |2 1 
----+----+----
failed to get a solution in 50 times
>>> 
=============== RESTART: /Users/hongchiliu/Desktop/genetic.py ===============
Sudoku puzzle is:
- - |- 3 |- - 
2 - |- - |- - 
- - |4 - |- - 
----+----+----
- - |- 2 |- 5 
- 2 |6 - |- - 
- - |- - |- - 
----+----+----
failed to get a solution in 50 times
>>> 


::::::::::::::::::::::::::::CONCLUSION:::::::::::::::::::::::::::::::::::
The best way I think to solve Sudoku problem is to use arc consistency to reduce the domain first, then use backtrack (DFS) to generate a solution.


Hongchi
Mar 19 2018