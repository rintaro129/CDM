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
    def truthTableGenerator(expression : str):
        expression2 = expression.replace('(', ' ')
        expression2 = expression2.replace(')', ' ')
        words = expression2.split()
        
        headers = []
        for word in words:
            if word.upper() not in {'AND', 'OR', 'NOT', 'XOR'}:
                headers.append(word)
        
        headers = list(set(headers))
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

        return table, headers, data
    
    def whenFalse(expression : str) -> str:
        _, headers, data = BooleanOperations.truthTableGenerator(expression)
        resultData = []
        for i in range(len(data)):
            if data[i][-1] == False:
                resultData.append(data[i])
        table = tabulate(resultData, headers, tablefmt="github")
        return table
        
           

print(BooleanOperations.whenFalse("NOT A OR B AND (A AND NOT C)"))
