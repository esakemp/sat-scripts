from pysat.solvers import Minisat22
from pysat.formula import CNF
import sys

filepath = sys.argv[1]
f1 = CNF(from_file=filepath)

models = []
with Minisat22(bootstrap_with=f1.clauses) as s:
    while(s.solve()):
        if (len(models) % 5 == 0):
            print 'working on ' + filepath + ', ' + str(len(models)) + ' models found so far. . .'
        model = s.get_model()
        model.sort(reverse=True)
        clause = []
        mdl = []
        for i in range(0, len(model)):
            if model[i] > 0:
                mdl.append(model[i])
                clause.append(model[i]*-1)
            else :
                model = model[i:]
                break
        s.add_clause(clause)
        if (s.solve(assumptions=model) == False):
            models.append(mdl)

print len(models), ' minimal models'


