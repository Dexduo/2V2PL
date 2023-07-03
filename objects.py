class numberObjects:
    dbNumber = 0
    arNumber = 0
    tbNumber = 0
    pgNumber = 0
    rwNumber = 0

class arrayObjects:
    dbs = []
    ars = []
    tbs = []
    pgs = []
    rws = []
    dbsNames = []
    arsNames = []
    tbsNames = []
    pgsNames = []
    rwsNames = []

numberObjects = numberObjects()

arrayObjects = arrayObjects()

def showObjects():
    print(arrayObjects.dbsNames)
    print(arrayObjects.arsNames)
    print(arrayObjects.tbsNames)
    print(arrayObjects.pgsNames)
    print(arrayObjects.rwsNames)

class database:
    typelock = ""
    children = []

    def __init__(self):
        self.name = "DB"+str(numberObjects.dbNumber + 1)
        numberObjects.dbNumber += 1
        arrayObjects.dbs.append(self)
        arrayObjects.dbsNames.append(self.name)

class area:
    typelock = ""
    children = []
    father = None

    def __init__(self):
        self.name = "AR"+str(numberObjects.arNumber + 1)
        numberObjects.arNumber += 1
        arrayObjects.ars.append(self)
        arrayObjects.arsNames.append(self.name)

class table:
    typelock = ""
    children = []
    father = None

    def __init__(self):
        self.name = "TB"+str(numberObjects.tbNumber + 1)
        numberObjects.tbNumber += 1
        arrayObjects.tbs.append(self)
        arrayObjects.tbsNames.append(self.name)

class page:
    typelock = ""
    children = []
    father = None

    def __init__(self):
        self.name = "PG"+str(numberObjects.pgNumber + 1)
        numberObjects.pgNumber += 1
        arrayObjects.pgs.append(self)
        arrayObjects.pgsNames.append(self.name)

class row:
    typelock = ""
    children = []
    father = None

    def __init__(self):
        self.name = "RW"+str(numberObjects.rwNumber + 1)
        numberObjects.rwNumber += 1
        arrayObjects.rws.append(self)
        arrayObjects.rwsNames.append(self.name)