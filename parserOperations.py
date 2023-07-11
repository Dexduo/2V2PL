#ESSE ARQUIVO TRATA A ENTRADA E A TRANSFORMA EM UM CONJUNTO DE OPERAÇÕES

import re

class tableOperations:
    tab = []

    def __init__(self):
        pass
    
    def addOperation(self, operation):
        self.tab.append(operation)
        
    
tableOperations = tableOperations()

class Operation:
    def __init__(self, operation):
        pattern = re.compile('C[1-9]')
        commitOperation = re.fullmatch(pattern, operation)
        
        self.operationType = operation[0]
        self.transactionId = operation[1]
        self.dbObject = None
        
        if commitOperation is None:
            self.dbObject = operation[3:6]
            
    
def getOperations(transaction):
    # transaction.replace(' ','')
    pattern = re.compile('[RWU][1-9]\(DB[1-9]\)|[RWU][1-9]\(AR[1-9]\)|[RWU][1-9]\(TB[1-9]\)|[RWU][1-9]\(PG[1-9]\)|[RWU][1-9]\(RW[1-9]\)|C[1-9]')
    operationsList = re.findall(pattern, transaction.replace(' ',''))
    return operationsList

def operationsTable(transaction):
    transaction = transaction.upper()
    operations = getOperations(transaction)
    for i in range(0, len(operations)):
        operation = operations[i]
        operation = Operation(operation)
        operation = [operation.transactionId, operation.dbObject, operation.operationType]
        tableOperations.addOperation(operation)
    print(tableOperations.tab)
    return tableOperations.tab

# def parserFinalSchedule(finalSchedule):
#     string = None
#     for i in range(0, len(finalSchedule)):
#         string = string+str()