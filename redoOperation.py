from lookForSysLock import *

def redoOperation(table, waitList, currentOperation, finalSchedule, graph):
    grant = True

    for i in range(0, len(waitList)):
        if i[2] == 'R':
            for j in range(i, -1, -1):
                if((i[2] == "CL") and (i[0] != table[j][0]) and (i[1] == table[j][1])):
                    grant = False
            if(grant == True):
                i[3] = '1'
            del waitList[i]

        if i[2] == 'W':
            for j in range(i, -1, -1):
                if((i[2] == "WL" or i[2] == "CL" ) and (i[0] != table[j][0]) and (i[1] == table[j][1])):
                    grant = False
            if(grant == True):
                i[3] = '1'
            del waitList[i]

        if i[2] == 'C':
            for j in range(i, -1, -1):
                if((i[0] != table[j][0]) and (i[1] == table[j][1])):
                    grant = False
            if(grant == True):
                i[3] = '1'
            del waitList[i]