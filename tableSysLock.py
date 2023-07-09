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

    # tableSysLock = tableSysLock()
    def genSchedule(self):
        for i in range(0, len(self.initialSchedule)):
            newLine = []
            newLine.append(self.initialSchedule[i][0])
            newLine.append(self.initialSchedule[i][1])
            newLine.append(self.initialSchedule[i][0]+'L')

            if(self.initialSchedule[i][2] == "W"):
                result = receiveWrite(tableSysLock.table, self.waitList, self.initialSchedule[i], self.finalSchedule, self.graph) #se achar converte update em WL, senão coloca mais uma linha de WL
                if(result == False):
                    print("Deadlock")
            
            if(self.initialSchedule[i][2] == "R"):
                result = receiveRead(self.table, self.waitList, self.initialSchedule[i], self.finalSchedule, self.graph) #se achar converte update em WL, senão coloca mais uma linha de WL
                if(result == False):
                    print("Deadlock")

            if(self.initialSchedule[i][2] == "C"):
                receiveCommit(self.table, self.waitList, self.initialSchedule[i], self.finalSchedule, self.graph) #se achar uma escrita, adiciona uma linha de CL
                print("commit")
                # olharSeTodasDaTransacaoEstaoConcedidas(tableSysLock.table, tableSysLock.initialSchedule[i]) #se todas as operacoes desta transacao foram concedidas

            if(self.initialSchedule[i][2] == "U"):
                # procurarOcorrenciaDeOutraTransacaoSobreOObjeto()
                result = receiveUpdate(self.table, self.waitList, self.initialSchedule[i], self.finalSchedule, self.graph) #se achar converte update em WL, senão coloca mais uma linha de WL
                if(result == False):
                    print("Deadlock")