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
clauses_3 = []
solver_calls = 0

i = 0
M = []
while len(clauses) > 0:
    clauses_2 = clauses[:i]
    clauses_3 = clauses_2 + M
    
    with Minisat22(bootstrap_with=clauses_3) as m:
        solver_calls += 1
        if m.solve():
            i+=1
            model = m.get_model()
        else:
            clauses = clauses_2[:i-1]

            # if i is 0 it means that M is already unsatisfiable
            if i == 0:
                break

            M.append(clauses_2[i-1])
            i = 0
print 'solver calls', solver_calls
print 'MUS length', len(M)