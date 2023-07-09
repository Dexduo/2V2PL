import networkx as nx

GRANTED_STATUS_CODE = '1'
WAITING_STATUS_CODE = '3'

def receiveWrite(table, waitList, currentOperation, finalSchedule, graph):
    newLine = []

    for i in reversed(table):
        if((i[2] == "WL" or i[2] == "CL" or i[2] == "UL") and (i[0] != currentOperation[0]) and (i[1] == currentOperation[1])):
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
        if((i[2] == "UL") and (i[0] == currentOperation[0]) and (i[1] == currentOperation[1] and i[3] == GRANTED_STATUS_CODE)):
            i[2] == "WL"
            newLine.append(currentOperation[0])
            newLine.append(currentOperation[1])
            newLine.append(currentOperation[2]+'L')
            newLine.append(GRANTED_STATUS_CODE)
            finalSchedule.append(currentOperation)
        
        else:
            newLine.append(currentOperation[0])
            newLine.append(currentOperation[1])
            newLine.append(currentOperation[2]+'L')
            newLine.append(WAITING_STATUS_CODE)
            table.append(newLine)
            waitList.append(currentOperation)

            if(len(list(nx.simple_cycles(graph))) != 0):
                # print("Deadlock")
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
        if((i[2] == "CL") and (i[0] != currentOperation[0]) and (i[1] == currentOperation[1])):
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


def receiveCommit(table, waitList, currentOperation, finalSchedule, graph):
    newLine = []

    for i in range(0, len(table)):
        if((table[i][2] == "WL") and (table[i][0] == currentOperation[0])):
            table[j][2] = "CL"
            for j in range(i-1, -1, -1):
                if((table[j][2] == "RL") and (table[j][0] != currentOperation[0]) and (i[1] == currentOperation[1])):
                    table[j][3] = "3"

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

def receiveUpdate(table, waitList, currentOperation, finalSchedule, graph):
    newLine = []

    for i in reversed(table):
        if((i[2] == "WL" or i[2] == "CL" or i[2] == "UL" or i[2] == "RL") and (i[0] != currentOperation[0]) and (i[1] == currentOperation[1])):
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
