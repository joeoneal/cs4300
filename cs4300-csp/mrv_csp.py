from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple, Callable, Iterable, Optional
import operator

Val = int
Assignment = Dict[str, Val]

@dataclass
class CSP:
    domains: Dict[str, List[Val]]
    constraints: List["Constraint"]

@dataclass
class Constraint:
    scope: Tuple[str, ...]
    pred: Callable[[Assignment], bool]
    pretty: str

# ---------- Constraint builders ----------
def c_alldiff(vars: List[str]) -> Constraint:
    def pred(a: Assignment) -> bool:
        vals = [a[v] for v in vars if v in a]
        return len(vals) == len(set(vals))
    return Constraint(tuple(vars), pred, f"alldiff({','.join(vars)})")

def c_bin(op: Callable[[int,int], bool], x: str, y: str, opname: str) -> Constraint:
    def pred(a: Assignment) -> bool:
        if x in a and y in a:
            return op(a[x], a[y])
        return True
    return Constraint((x,y), pred, f"{opname}({x},{y})")

def c_in(x: str, allowed: List[int]) -> Constraint:
    def pred(a: Assignment) -> bool:
        return (x not in a) or (a[x] in allowed)
    return Constraint((x,), pred, f"in({x},{allowed})")

def c_sum(vars: List[str], opstr: str, k: int) -> Constraint:
    opmap = {"==": operator.eq, "!=": operator.ne, "<=": operator.le,
             "<": operator.lt, ">=": operator.ge, ">": operator.gt}
    if opstr not in opmap: raise ValueError(f"bad sum op {opstr}")
    opf = opmap[opstr]
    def pred(a: Assignment) -> bool:
        # Accept partial assignments; only check when fully assigned
        if not all(v in a for v in vars):
            return True
        return opf(sum(a[v] for v in vars), k)
    return Constraint(tuple(vars), pred, f"sum({vars}) {opstr} {k}")

def c_table(vars: List[str], allowed: List[Tuple[int, ...]]) -> Constraint:
    allowed_set = set(tuple(t) for t in allowed)
    def pred(a: Assignment) -> bool:
        if all(v in a for v in vars):
            tup = tuple(a[v] for v in vars)
            return tup in allowed_set
        return True
    return Constraint(tuple(vars), pred, f"table({vars}) allowed {allowed}")

def c_add10(x: str, y: str, cin: str, z: str, cout: str) -> Constraint:
    """Digit-wise base-10 addition: x + y + cin = 10*cout + z, where cin, cout in {0,1} and x,y,z in 0..9.
       Partial assignments are allowed; we only enforce when all involved vars are assigned.
    """
    scope = (x, y, cin, z, cout)
    def pred(a: Assignment) -> bool:
        if all(v in a for v in scope):
            return (a[x] + a[y] + a[cin]) == 10 * a[cout] + a[z]
        return True
    return Constraint(scope, pred, f"add10({x},{y},{cin}->{z},{cout})")

############################# MRV heuristic #########################################################################


def mrv(csp, assignment, current_domains):
    best_var = None
    min_domain_size = float('inf')

    for var in csp.domains:
        if var not in assignment:
            domain_size = len(current_domains[var])
            
            if domain_size < min_domain_size:
                min_domain_size = domain_size
                best_var = var
                
    return best_var


#####################################################################################################################

# ---------- Simple solver (BT + forward checking) ----------
def solve_backtracking(csp: CSP, stats: Dict[str, int]) -> Iterable[Assignment]:
    stats["steps"] = 0
    domains = {v: list(ds) for v, ds in csp.domains.items()}
    cons_by_var: Dict[str, List[Constraint]] = {v: [] for v in domains}
    for c in csp.constraints:
        for v in c.scope:
            if v in cons_by_var:
                cons_by_var[v].append(c)

    assignment: Assignment = {}

    def consistent_with_local(v: str, a: Assignment) -> bool:
        for c in cons_by_var[v]:
            if not c.pred(a):
                return False
        return True
    
    def backtrack():
        if len(assignment) == len(csp.domains):
            yield dict(assignment)
            return

        v = mrv(csp, assignment, domains)

        for val in list(domains[v]):
            assignment[v] = val
            stats["steps"] += 1
            
            if consistent_with_local(v, assignment):
                pruned = []
                ok = True

                unassigned_vars = [var for var in csp.domains if var not in assignment]
                
                for w in unassigned_vars:
                    removed = []

                    for vv in list(domains[w]):
                        assignment[w] = vv
                        if not consistent_with_local(w, assignment):
                            domains[w].remove(vv)
                            removed.append(vv)
                        del assignment[w]
                    
                    if removed:
                        pruned.append((w, removed))
                    
                    if not domains[w]:
                        ok = False
                        break
                
                if ok:
                    yield from backtrack()
                
                for w, removed in pruned:
                    domains[w].extend(removed)
            
            del assignment[v]

    yield from backtrack()



