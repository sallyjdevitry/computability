###############################################
# module: cyktest.py
# description: tests CYK in cyk.py
# bugs to vladimir kulyukin via canvas
###############################################

import unittest
import cyk
from cyk import CYK
from cnfg import CNFG

class TestCykAlgorithm(unittest.TestCase):
    _grammar = CNFG()
    
    def _use_grammar1(self):
        ## 1. S -> AB
        ## 2. S --> BC
        ## 3. A --> BA
        ## 4. A --> a
        ## 5. B --> CC
        ## 6. B --> b
        ## 7. C --> AB
        ## 8. C --> a
        self._grammar.clear_productions()
        self._grammar = CNFG()
        self._grammar.add_production("S", "A", "B")
        self._grammar.add_production("S", "B", "C")
        self._grammar.add_production("A", "B", "A")
        self._grammar.add_production("A", "a")
        self._grammar.add_production("B", "C", "C")
        self._grammar.add_production("B", "b")
        self._grammar.add_production("C", "A", "B")
        self._grammar.add_production("C", "a")

    def _use_grammar2(self):
        ## 1. S ->  AB
        ## 2. S --> BB
        ## 3. A --> CC
        ## 4. A --> AB
        ## 5. A --> a
        ## 6. B --> BB
        ## 7. B --> CA
        ## 8. B --> b
        ## 9. C --> BA
        ## 10. C --> AA
        ## 11. C --> b
        self._grammar.clear_productions()        
        self._grammar = CNFG();
        self._grammar.add_production("S", "A", "B")
        self._grammar.add_production("S", "B", "B")
        self._grammar.add_production("A", "C", "C")
        self._grammar.add_production("A", "A", "B")
        self._grammar.add_production("A", "a")
        self._grammar.add_production("B", "B", "B")
        self._grammar.add_production("B", "C", "A")
        self._grammar.add_production("B", "b")
        self._grammar.add_production("C", "B", "A")
        self._grammar.add_production("C", "A", "A")
        self._grammar.add_production("C", "b")

    def _use_grammar3(self):
        ## 1. S ->  AD1
        ## 2. D1 --> BC
        ## 3. C --> BD2
        ## 4. D2 --> AB
        ## 5. C --> c
        ## 6. B --> BB
        ## 7. B --> b
        ## 8. A --> a
        self._grammar._productions.clear()
        self._grammar = CNFG();
        self._grammar.add_production("S", "A", "D1")
        self._grammar.add_production("D1", "B", "C")
        self._grammar.add_production("C", "B", "D2")
        self._grammar.add_production("D2", "A", "B")
        self._grammar.add_production("C", "c")
        self._grammar.add_production("B", "B", "B")
        self._grammar.add_production("B", "b")
        self._grammar.add_production("A", "a")

    def test_ut0(self):
        print("===== Test 00 =====")        
        grammar = CNFG()
        grammar.clear_productions()
        grammar.add_production("S", "A", "B")
        grammar.add_production("S", "B", "C")
        grammar.add_production("A", "B", "A")
        grammar.add_production("A", "a")
        grammar.add_production("B", "C", "C")
        grammar.add_production("B", "b")
        grammar.add_production("C", "A", "B")
        grammar.add_production("C", "a")
        print("LHS for RHS AB is {}".format(grammar.fetch_lhs("A", "B")))
        
    ### ===================== Grammar 1 Tests #############################
    #
    def test1a(self):
        print("===== Test 1a =====")
        self._use_grammar1()
        #self._grammar.display()
        input_str = 'ab'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test1(self):
        print("===== Test 1 =====")
        self._use_grammar1()
        self._grammar.display()
        input_str = 'baaba'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))
        
    def test2(self):
        print("===== Test 2 =====")
        self._use_grammar1()
        #self._grammar.display()
        input_str = 'baaa'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test3(self):
        print("===== Test 3 =====")
        self._use_grammar1()
        #self._grammar.display()
        input_str = 'baba'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test4(self):
        print("===== Test 4 =====")
        self._use_grammar1()
        #self._grammar.display()
        input_str = 'baaabab'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    ### ===================== Grammar 2 Tests #############################

    def test5(self):
        print("===== Test 5 =====")
        self._use_grammar2()
        #self._grammar.display()
        input_str = 'aabb'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test5a(self):
        print("===== Test 5a =====")
        self._use_grammar2()
        #self._grammar.display()
        input_str = 'bbb'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test5b(self):
        print("===== Test 5b =====")
        self._use_grammar2()
        #self._grammar.display()
        input_str = 'bbb'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test5c(self):
        print("===== Test 5c =====")
        self._use_grammar2()
        #self._grammar.display()
        input_str = 'cccccb'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test5d(self):
        print("===== Test 5d =====")
        self._use_grammar2()
        #self._grammar.display()
        input_str = 'bababaaa'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    ### ===================== Grammar 3 Tests #############################

    def test6(self):
        print("===== Test 6 =====")
        self._use_grammar3()
        input_str = 'abc'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test7(self):
        print("===== Test 7 =====")
        self._use_grammar3()
        input_str = 'abbbabb'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test7(self):
        print("===== Test 8 =====")
        self._use_grammar3()
        input_str = 'abbc'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test8(self):
        print("===== Test 8 =====")
        self._use_grammar3()
        input_str = 'bbc'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test9(self):
        print("===== Test 9 =====")
        self._use_grammar3()
        input_str = 'aaabb'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

    def test10(self):
        print("===== Test 10 =====")
        self._use_grammar3()
        input_str = 'ab'
        print('Input string: ' + input_str)
        result = (CYK.is_in_cfl(input_str, self._grammar))
        print('Result = ' + str(result))

if __name__ == '__main__':
    unittest.main()
        















