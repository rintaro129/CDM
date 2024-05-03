import sympy
class Lab5:
    def functionEvaluator(m : int, b : int, x : int) -> int:
        return m * x + b
    
        
    def domainAndRange(s : set):
        dom = set()
        ran = set()
        for (a, b) in s:
            dom.add(a)
            ran.add(b)
        return dom, ran
    
    def evenOdd(s : list) -> str:
        s = set(s)
        ifEven = True
        ifOdd = True
        for (a, b) in s:
            if(ifEven):
                if((-a, b) not in s):
                    ifEven = False
            if(ifOdd):
                if((-a, -b) not in s):
                    ifOdd = False
            if(not ifOdd and not ifEven):
                break
        if(ifEven):
            return "Even"
        if(ifOdd):
            return "Odd"
        return "Neither"
    
    
    def injectiveFunctionValidator(s : set) -> bool:
        res = True
        ran = set()
        for (_, b) in s:
            if(b in ran):
                res = False
                break
            else:
                ran.add(b)
        return res
    
    def surjectiveFunctionValidator(s : set, c : set) -> bool:
        ran = set()
        for (_, b) in s:
            ran.add(b)
        if(ran == c):
            return True
        else:
            return False

    def funcCombTool(func1 : str, func2 : str, operation : str, value) -> int:
        x = sympy.Symbol('x')
        func1 = eval(func1.replace('^', ' ** '))
        func2 = eval(func2.replace('^', ' ** '))
        res1 = func1.subs(x, value)
        res2 = func2.subs(x, value)
        if(operation == "Addition"):
            return res1 + res2
        elif(operation == "Substraction"):
            return res1 - res2
        elif(operation == "Multiplication"):
            return res1 * res2
        elif(operation == "Division"):
            return res1 / res2
        else:
            print("Unsupported operation")
            return 0
        
    
    def graphInformationExtractor(s : list):
        s = sorted(s)
        xintercepts = set()
        yintercepts = set()
        maxima = set()
        minima = set() 
        for (a, b) in s:
            if(a == 0):
                xintercepts.add(b)
            if(b == 0):
                yintercepts.add(a)
        d = 0
        if(s[1][1] - s[0][1] != 0):
            d = (s[1][1] - s[0][1]) / abs(s[1][1] - s[0][1])
        for i in range(2, len(s)):
            d1 = 0
            if(s[i][1] - s[i-1][1] != 0):
                d1 = (s[i][1] - s[i-1][1]) / abs(s[i][1] - s[i-1][1])
            if(d == 0):
                d = d1
                continue
            if(d == 1 and d1 == -1):
                d = -1
                maxima.add(s[i-1])
            if(d == -1 and d1 == 1):
                d = 1
                minima.add(s[i-1])
        print(f"x-intercepts: {xintercepts}")
        print(f"y-intercepts: {yintercepts}")
        print(f"Maxima: {maxima}")
        print(f"Minima: {minima}")
        return xintercepts, yintercepts, maxima, minima

print(Lab5.functionEvaluator(m=2, b=3, x=4))
dom, ran = Lab5.domainAndRange({(1, 2), (3, 6), (4, 8)})
print(f"Domain: {dom}\nRange: {ran}")
print(Lab5.evenOdd([(-1,1), (0,0), (1,1)]))
print(Lab5.injectiveFunctionValidator({(2, 4), (3, 6), (4, 8)}))
print(Lab5.surjectiveFunctionValidator({(1, 2), (2, 3), (3, 4)}, {2, 3, 4}))
print(Lab5.funcCombTool("x ^ 2", "2*x+1", "Addition", 3))
Lab5.graphInformationExtractor([(-2, -4), (-1, -1), (0, 0), (1, 1), (2, 4)])
        

