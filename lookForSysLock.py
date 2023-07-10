import networkx as nx
from redoOperation import *

GRANTED_STATUS_CODE = '1'
WAITING_STATUS_CODE = '3'

def receiveWrite(table, waitList, currentOperation, finalSchedule, graph):
    newLine = []

    for i in reversed(table):
        if((i[2] == "WL" or i[2] == "CL" or i[2] == "UL") and (i[0] != currentOperation[0]) and (i[1] == currentOperation[1]) and (i[3] == GRANTED_STATUS_CODE)):
            print(f'trasaction Id: {i[0]}, db object: {i[1]}, operation type: {i[2]}, status code: {i[3]}')
            newLine.append(currentOperation[0])
            newLine.append(currentOperation[1])
            newLine.append(currentOperation[2]+'L')
            newLine.append(WAITING_STATUS_CODE)
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
        # ------------------------
        if((i[2] == "UL") and (i[0] == currentOperation[0]) and (i[1] == currentOperation[1]) and (i[3] == GRANTED_STATUS_CODE)):
            print(f'trasaction Id: {i[0]}, db object: {i[1]}, operation type: {i[2]}, status code: {i[3]}')
            print('entreii aqui')
            print(f'i : {i}')
            i[2] = "WL"
            # newLine.append(currentOperation[0])
            # newLine.append(currentOperation[1])
            # newLine.append(currentOperation[2]+'L')
            # newLine.append(GRANTED_STATUS_CODE)
            finalSchedule.append(currentOperation)

            if(len(list(nx.simple_cycles(graph))) != 0):
                print("Deadlock")
                return False
            else:
                return True
        # ------------------------

    newLine.append(currentOperation[0])
    newLine.append(currentOperation[1])
    newLine.append(currentOperation[2]+'L')
    newLine.append(GRANTED_STATUS_CODE)
    table.append(newLine)
    finalSchedule.append(currentOperation)


def receiveRead(table, waitList, currentOperation, finalSchedule, graph):
    newLine = []

    for i in reversed(table):
        if((i[2] == "CL") and (i[0] != currentOperation[0]) and (i[1] == currentOperation[1]) and (i[3] == GRANTED_STATUS_CODE)):
            newLine.append(currentOperation[0])
            newLine.append(currentOperation[1])
            newLine.append(currentOperation[2]+'L')
            newLine.append(WAITING_STATUS_CODE)
            table.append(newLine)
            waitList.append(currentOperation)
            graph.add_node(str(i[0]))
            graph.add_node(currentOperation[0])
            graph.add_edge(str(i[0]), currentOperation[0])

            if(len(list(nx.simple_cycles(graph))) != 0):
                print("Deadlock")
                return False
            else:
                return True

    newLine.append(currentOperation[0])
    newLine.append(currentOperation[1])
    newLine.append(currentOperation[2]+'L')
    newLine.append(GRANTED_STATUS_CODE)
    table.append(newLine)
    finalSchedule.append(currentOperation)


def receiveCommit(table, waitList, currentOperation, finalSchedule, graph):
    newLine = []
    index = []
    commitWait = False

    for i in range(0, len(table)):
        #converte WL em CL e olha se pode conceder
        if((table[i][2] == "WL") and (table[i][0] == currentOperation[0])):
            # for j in range(i-1, -1, -1):
            for j in range(0, len(table)):
                if((table[j][2] == "RL") and (table[j][0] != currentOperation[0]) and (table[j][1] == table[i][1])):
                    table[i][3] = WAITING_STATUS_CODE
                    graph.add_node(str(table[i][0]))
                    graph.add_node(str(table[j][0]))
                    graph.add_edge(str(table[i][0]), str(table[j][0]))
                    commitWait = True
                    break
                    
    if commitWait == False:
        table[i][2] = "CL"

    if(commitWait == True):
        waitList.append(currentOperation)
        if(len(list(nx.simple_cycles(graph))) != 0):
            print("Deadlock")
            return False
        else:
            return True
    else:
        finishOperations = True
        for i in range(0, len(table)):
            if((table[i][0] == currentOperation[0]) and (table[i][3] == WAITING_STATUS_CODE)):
                finishOperations = False
        if(finishOperations == True):
            finalSchedule.append(currentOperation)
            graph.remove_node(currentOperation[0])
            for i in range(len(table)-1, -1, -1):
                if(table[i][0] == currentOperation[0]):
                    del table[i]
                # print("Tamanho da syslock: "+ str(len(table)))
            # print("Commit da transação "+str(currentOperation[0]))
            redoOperation(table, waitList, finalSchedule, graph)
            #A redoOperation vai pegar e tentar fazer as operações que estão na lista de espera

def receiveUpdate(table, waitList, currentOperation, finalSchedule, graph):
    newLine = []
    for i in reversed(table):
        if((i[2] == "WL" or i[2] == "CL" or i[2] == "UL") and (i[0] != currentOperation[0]) and (i[1] == currentOperation[1]) and (i[3] == GRANTED_STATUS_CODE)):
            newLine.append(currentOperation[0])
            newLine.append(currentOperation[1])
            newLine.append(currentOperation[2]+'L')
            newLine.append(WAITING_STATUS_CODE)
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
    newLine.append(GRANTED_STATUS_CODE)
    table.append(newLine)
    finalSchedule.append(currentOperation)