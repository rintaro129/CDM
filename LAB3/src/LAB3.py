import re
from tabulate import tabulate

class BooleanOperations:
    @staticmethod
    def expressionEvaluator(expression : str, dictionary : dict) -> bool:        
        expression = re.sub('AND', 'and', expression, flags=re.IGNORECASE)
        expression = re.sub('OR', 'or', expression, flags=re.IGNORECASE)
        expression = re.sub('NOT', 'not', expression, flags=re.IGNORECASE)
        expression = re.sub('XOR', '^', expression, flags=re.IGNORECASE)

        for i in dictionary:
            expression = re.sub(i, str(dictionary[i]), expression)

        return eval(expression)
    
    @staticmethod
    def truthTableGenerator(expression : str) -> str:
        expression2 = expression.replace('(', ' ')
        expression2 = expression2.replace(')', ' ')
        words = expression2.split()
        
        headers = []
        for word in words:
            if word.upper() not in {'AND', 'OR', 'NOT', 'XOR'}:
                headers.append(word)
        
        headers.sort()
        headers.append(expression)

        data = []
        for bitmask in range(2 ** (len(headers) - 1)):
            temp = bitmask
            row = [False] * len(headers)
            for i in range(len(headers) - 1 - 1, -1, -1):
                row[i] = bool(temp % 2)
                temp = temp // 2
            
            dictionary = dict()
            for i in range(len(headers) - 1):
                dictionary[headers[i]] = row[i]
            
            row[-1] = BooleanOperations.expressionEvaluator(expression, dictionary)
            data.append(row)

        table = tabulate(data, headers, tablefmt="github")

        return table
        
print(BooleanOperations.expressionEvaluator("(A AND B) OR NOT C", {"A": True, "B": False, "C": True}))
print(BooleanOperations.truthTableGenerator("(A AND B) OR C"))
