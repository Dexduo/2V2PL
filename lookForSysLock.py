import networkx as nx
from redoOperation import *

def receiveWrite(table, waitList, currentOperation, finalSchedule, graph):
    newLine = []

    for i in reversed(table):
        if((i[2] == "WL" or i[2] == "CL") and (i[0] != currentOperation[0]) and (i[1] == currentOperation[1])):
            newLine.append(currentOperation[0])
            newLine.append(currentOperation[1])
            newLine.append(currentOperation[2]+'L')
            newLine.append('3')
            table.append(newLine)
            waitList.append(currentOperation)
            graph.add_node(str(i[0]))
            graph.add_node(currentOperation[0])
            graph.add_edge(str(i[0]), currentOperation[0])

            if(len(list(nx.simple_cycles(graph))) != 0):
                # print("Deadlock")
                return False
            else:
                return True
    
    newLine.append(currentOperation[0])
    newLine.append(currentOperation[1])
    newLine.append(currentOperation[2]+'L')
    newLine.append('1')
    table.append(newLine)
    finalSchedule.append(currentOperation)


def receiveRead(table, waitList, currentOperation, finalSchedule, graph):
    newLine = []

    for i in reversed(table):
        if((i[2] == "CL") and (i[0] != currentOperation[0]) and (i[1] == currentOperation[1])):
            newLine.append(currentOperation[0])
            newLine.append(currentOperation[1])
            newLine.append(currentOperation[2]+'L')
            newLine.append('3')
            table.append(newLine)
            waitList.append(currentOperation)
            graph.add_node(str(i[0]))
            graph.add_node(currentOperation[0])
            graph.add_edge(str(i[0]), currentOperation[0])

            if(len(list(nx.simple_cycles(graph))) != 0):
                # print("Deadlock")
                return False
            else:
                return True
    
    newLine.append(currentOperation[0])
    newLine.append(currentOperation[1])
    newLine.append(currentOperation[2]+'L')
    newLine.append('1')
    table.append(newLine)
    finalSchedule.append(currentOperation)


def receiveCommit(table, waitList, currentOperation, finalSchedule, graph):
    newLine = []
    index = []
    commitWait = False

    for i in range(0, len(table)):
        if((table[i][2] == "WL") and (table[i][0] == currentOperation[0])):
            table[i][2] = "CL"
            for j in range(i-1, -1, -1):
                if((table[j][2] == "RL") and (table[j][0] != currentOperation[0]) and (table[j][1] == currentOperation[1])):
                    table[i][3] = "3"
                    graph.add_node(str(table[i][0]))
                    graph.add_node(str(table[j][0]))
                    graph.add_edge(str(table[i][0]), str(table[j][0]))
                    commitWait = True
                    break
    
    if(commitWait == True):
        waitList.append(currentOperation)
        if(len(list(nx.simple_cycles(graph))) != 0):
            # print("Deadlock")
            return False
        else:
            return True
    else:
        finishOperations = True
        for i in range(0, len(table)):
            if((table[i][0] == currentOperation[0]) and (table[i][3] == '1')):
                finishOperations = False
        if(finishOperations == True):
            finalSchedule.append(currentOperation)
            graph.remove_node(currentOperation[0])
            for i in range(0, len(table)):
                if((table[i][0] == currentOperation[0])):
                    del table[i]
            redoOperation(table, waitList, currentOperation, finalSchedule, graph)
            #A redoOperation vai pegar e tentar fazer as operações que estão na lista de espera