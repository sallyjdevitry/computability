###############################################
# module: cnfg.py
# description: Chomsky Normal Form Grammar
# bugs to vladimir kulyukin via canvas
###############################################

class CNFG:
    
    def __init__(self, startSymbol = "S", productions = dict()):
        self._productions = productions
        self._startSymbol = startSymbol

    def __str__(self):
        productions = list()
        for lhs in self._productions:
            for rhs in self._productions[lhs]:
                 productions.append(lhs + " -> " + str(rhs))
        return "\n".join(productions)

    def add_production(self, lhs, rhs1, rhs2 = None):
        if lhs in self._productions:
            rhs = self._productions.get(lhs)
            rhs.append(CNFProductionRHS(rhs1, rhs2))
        else:
            rhs = list()
            rhs.append(CNFProductionRHS(rhs1, rhs2))
            self._productions[lhs] = rhs

    def fetch_lhs(self, rhs1, rhs2 = None):
        lhs_list = set()    
        for lhs in self._productions:
            for prod_rhs in self._productions[lhs]:
                if rhs2 is None:
                    if prod_rhs.is_rhs1() and prod_rhs.is_rhs1_equal(rhs1):
                        lhs_list.add(lhs)                        
                else:
                    if prod_rhs.is_rhs2() and prod_rhs.is_rhs2_equal(rhs1, rhs2):
                        lhs_list.add(lhs)
            
        return lhs_list

    def clear_productions(self):
        self._productions.clear()

    def get_start_symbol(self):
        return self._startSymbol
        
    def display(self):
        print(str(self))


class CNFProductionRHS:
    def __init__(self, rhs1, rhs2 = None):
        if rhs2 is None:
            self._rhs_list = list(rhs1)
        else:
            self._rhs_list = list([rhs1, rhs2])

    def __str__(self):
        return "".join(self._rhs_list)

    def is_rhs1(self):
        return len(self._rhs_list) == 1

    def is_rhs2(self):
        return len(self._rhs_list) == 2

    def is_rhs1_equal(self, rhs):
        return self._rhs_list[0] == rhs

    def is_rhs2_equal(self, rhs1, rhs2):
        return self._rhs_list[0] == rhs1 and self._rhs_list[1] == rhs2

    def get_productions(self):
        if self.is_rhs1():
            return self._rhs_list[0]
        elif self.is_rhs2():
            return self._rhs_list[0], self._rhs_list[1]
        else:
            return None


