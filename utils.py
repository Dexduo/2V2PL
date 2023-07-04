import re
class Operation:
    def __init__(self, operation):
        pattern = re.compile('c[1-9]')
        commitOperation = re.fullmatch(pattern, operation)
        
        self.operationType = operation[0]
        self.transactionId = operation[1]
        self.dbObject = None
        
        if commitOperation is None:
            self.dbObject = operation[3:6]
            
    
def getOperations(transaction):
    # transaction.replace(' ','')
    pattern = re.compile('[rwu][1-9]\(DB[1-9]\)|[rwu][1-9]\(AR[1-9]\)|[rwu][1-9]\(TB[1-9]\)|[rwu][1-9]\(PG[1-9]\)|[rwu][1-9]\(RW[1-9]\)|c[1-9]')
    operationsList = re.findall(pattern, transaction.replace(' ',''))
    return operationsList