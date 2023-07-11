from lookForSysLock import *

def redoOperation(table, waitList, finalSchedule, graph):
    grant = True

    for i in range(len(waitList)-1, -1, -1):
        grant = True
        if waitList[i][2] == 'R':
            
            for j in range(i-1, -1, -1):
                if((table[j][2] == "CL" or table[j][2] == "UL") and (table[i][0] != table[j][0]) and (table[i][1] == table[j][1])):
                    grant = False
            if(grant == True):
                table[i][3] = '1'
                finalSchedule.append(waitList[i])
                del waitList[i]

        elif waitList[i][2] == 'W':
            for j in range(i-1, -1, -1):
                if((table[j][2] == "WL" or table[j][2] == "CL" ) and (table[i][0] != table[j][0]) and (table[i][1] == table[j][1])):
                    grant = False
            if(grant == True):
                table[i][3] = '1'
                finalSchedule.append(waitList[i])
                del waitList[i]

        elif waitList[i][2] == 'C':
            for k in range(0, len(table)):
                grant = True
                # print(table[k])
                if((table[k][2] == "CL") and (table[k][3] == "3")):
                    for j in range(k-1, -1, -1):
                        if((table[j][2] == "RL") and (table[j][0] != table[k][0]) and (table[j][1] == table[k][1])):
                            # print("Deu errado")
                            grant = False
                            break
                    if(grant == True):
                        table[k][3] = '1'
            
            finishOperations = True
            for l in range(0, len(table)):
                if((table[l][0] == waitList[i][0]) and (table[l][3] == '3')):
                    finishOperations = False
            if(finishOperations == True):
                finalSchedule.append(waitList[i])
                graph.remove_node(waitList[i][0])
                for l in range(len(table)-1, -1, -1):
                    if(table[l][0] == waitList[i][0]):
                        del table[l]
                del waitList[i]
                redoOperation(table, waitList, finalSchedule, graph)