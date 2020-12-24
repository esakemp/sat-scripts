from pysat.solvers import Minisat22
import sys

filepath = sys.argv[1]

f = open(filepath)

rows = f.readlines()
rows = rows[1:]

clauses = []
for row in rows:
    nums = row.split()
    clauses.append([int(num) for num in nums[:len(nums)-1]])
    
clauses_2 = []
solver_calls = 0


i = 0
while i < len(clauses):
    clauses_2 = clauses[:i] + clauses[(i+1):]
    with Minisat22(bootstrap_with=clauses_2) as m:
        solver_calls += 1
        if m.solve():
            i+=1
        else:
            clauses = clauses_2

print 'solver calls', solver_calls
print 'MUS length', len(clauses)


