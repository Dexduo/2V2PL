import networkx as nx
from lookForSysLock import *

class tableSysLock:
    initialSchedule = []
    finalSchedule = []
    table = []
    waitList = []
    graph = nx.DiGraph()
    
    def __init__(self, initialSchedule):
        self.initialSchedule = initialSchedule
        self.genSchedule()
    
    def genSchedule(self):
        for i in range(0, len(self.initialSchedule)):

            self.graph.add_node(self.initialSchedule[i][0])

            if(self.initialSchedule[i][2] == "W"):
                result = receiveWrite(self.table, self.waitList, self.initialSchedule[i], self.finalSchedule, self.graph) #se achar converte update em WL, senão coloca mais uma linha de WL
                if(result == False):
                    print("Deadlock")
            
            if(self.initialSchedule[i][2] == "R"):
                result = receiveRead(self.table, self.waitList, self.initialSchedule[i], self.finalSchedule, self.graph) #se achar converte update em WL, senão coloca mais uma linha de WL
                if(result == False):
                    print("Deadlock")

            if(self.initialSchedule[i][2] == "C"):
                result = receiveCommit(self.table, self.waitList, self.initialSchedule[i], self.finalSchedule, self.graph) #se achar uma escrita, adiciona uma linha de CL
                if(result == False):
                    print("Deadlock")

            if(self.initialSchedule[i][2] == "U"):
                receiveUpdate(self.table, self.waitList, self.initialSchedule[i], self.finalSchedule, self.graph)