class MySet():
    @staticmethod
    def cartesianProduct(setA : set, setB : set) -> set:
        returnSet = set()
        for i in setA:
            for j in setB:
                returnSet.add((i, j))
        return returnSet
    
    @staticmethod
    def isRelationValid(relation : set, setA : set, setB : set) -> bool:
        cartesian = MySet.cartesianProduct(setA, setB)
        returnBool = True
        for i in relation:
            if (i not in cartesian):
                returnBool = False
                break
        return returnBool
    
    @staticmethod
    def findRelations(setA : set, relationFunc : callable) -> set:
        returnSet = set()
        for i in setA:
            for j in setA:
                if(relationFunc(i, j)):
                    returnSet.add((i, j))
        return returnSet
    
    @staticmethod
    def filteredCartesianProduct(setA : set, setB : set, filterFunc : callable) -> set:
        cartesian = MySet.cartesianProduct(setA, setB)
        returnSet = set()
        for (a, b) in cartesian:
            if(filterFunc(a, b)):
                returnSet.add((a, b))
        return returnSet
    
    @staticmethod
    def minAndMax(setA : set, setB : set):
        return min(setA), max(setB)
    
isDivisible = lambda a, b : a % b == 0 and a != b
lessThan = lambda a, b : a < b
lessThanOrEqualTo = lambda a, b : a <= b
biggerThan = lambda a, b : a > b
biggerThanOrEqualTo = lambda a, b : a >= b
equal = lambda a, b : a == b
equalModulo3 = lambda a, b : a % 3 == b % 3

#print(MySet.cartesianProduct(setA={1, 2}, setB={'a', 'b'}))
#print(MySet.isRelationValid(relation={(1, 'a'), (2, 'b')}, setA={1, 2}, setB={'a', 'b'}))
#print(MySet.findRelations(setA={1, 2, 3, 4, 5, 6}, relationFunc=isDivisible))
#print(MySet.filteredCartesianProduct(setA={1, 2, 3}, setB={3, 4, 5}, filterFunc=lessThan))
print(MySet.minAndMax(setA={3, 1, 2}, setB={6, 2, 3}))


      
                    