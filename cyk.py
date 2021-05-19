###############################################
# module: cyk.py
# Sally Devitry
# A01980316
###############################################
import itertools

#returns list of sets of cartesian products of set1 and set2
def findCart(set1, set2):
    returnSet = []
    #turn them into lists to manipulate
    list1 = list(set1)
    list2 = list(set2)
    for element in itertools.product(list1, list2):
        if len(element) > 0:
            returnSet.append(element)
    return returnSet

#returns a list of characters from a given string.
def split(word):
    return [char for char in word]

class CYK(object):

    @staticmethod
    def is_in_cfl(test_string, cnfg):
        tableSize = len(test_string)
        # table is now a 2d array with width/height of tableSize
        table = [[[] for i in range(tableSize)] for j in range(tableSize)]

        #fill in the table
        testStringList = split(test_string)
        for k in range(tableSize):
            for i in range(tableSize):
                if k == 0:
                    subString = testStringList[:i+1]
                    for j in range(len(subString)):
                        ans = cnfg.fetch_lhs(subString[j])
                        table[k][i] = ans
                else:
                    n = k
                    m = 1
                    if i+n < tableSize:
                        newReachableNts = set()
                        while m < k+1 and n > 0:
                            #get the two cells that this substring relies on
                            previousNts = table[k-m][i]
                            secondPreviousNts = table[k-n][i+n]
                            n -= 1
                            m += 1
                            cartProd = findCart(previousNts, secondPreviousNts)
                            for aSet in cartProd:
                                listSet = list(aSet)
                                if len(listSet) > 1:
                                    reachable = cnfg.fetch_lhs(listSet[0], listSet[1])
                                    emptySet = set()
                                    if reachable != emptySet:
                                        for thing in reachable:
                                            newReachableNts.add(thing)
                                else:
                                    newReachableNts.add(cnfg.fetch_lhs(listSet[0]))

                        table[k][i] = newReachableNts

        #if the final cell contains a start state, return True
        if 'S' in table[tableSize-1][0]:
            return True
        else:
            return False


