import networkx as nx
from lookForSysLock import *

class tableSysLock:
    initialSchedule = None
    finalSchedule = None
    table = []
    waitList = []
    graph = nx.DiGraph()
    
    def __init__(self, initialSchedule):
        self.initialSchdule = initialSchedule

tableSysLock = tableSysLock()

for i in range(0, len(tableSysLock.initialSchedule)):
    newLine = []
    newLine.append(tableSysLock.initialSchedule[i][0])
    newLine.append(tableSysLock.initialSchedule[i][1])
    newLine.append(tableSysLock.initialSchedule[i][0]+'L')

    if(tableSysLock.initialSchedule[i][2] == "W"):
        result = receiveWrite(tableSysLock.table, tableSysLock.waitList, tableSysLock.initialSchedule[i], tableSysLock.finalSchedule, tableSysLock.graph) #se achar converte update em WL, senão coloca mais uma linha de WL
        if(result == False):
            print("Deadlock")
    
    if(tableSysLock.initialSchedule[i][2] == "R"):
        result = receiveRead(tableSysLock.table, tableSysLock.waitList, tableSysLock.initialSchedule[i], tableSysLock.finalSchedule, tableSysLock.graph) #se achar converte update em WL, senão coloca mais uma linha de WL
        if(result == False):
            print("Deadlock")

    if(tableSysLock.initialSchedule[i][2] == "C"):
        receiveCommit(tableSysLock.table, tableSysLock.waitList, tableSysLock.initialSchedule[i], tableSysLock.finalSchedule, tableSysLock.graph) #se achar uma escrita, adiciona uma linha de CL
        print("commit")
        olharSeTodasDaTransacaoEstaoConcedidas(tableSysLock.table, tableSysLock.initialSchedule[i]) #se todas as operacoes desta transacao foram concedidas

    if(tableSysLock.initialSchedule[i][2] == "U"):
        procurarOcorrenciaDeOutraTransacaoSobreOObjeto()