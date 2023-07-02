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

numberObjects = numberObjects()

arrayObjects = arrayObjects()

class database:
    typelock = ""
    children = []

    def __init__(self):
        self.name = "DB"+str(numberObjects.dbNumber + 1)
        numberObjects.dbNumber += 1
        arrayObjects.dbs.append(self)

class area:
    typelock = ""
    children = []
    father = None

    def __init__(self):
        self.name = "AR"+str(numberObjects.arNumber + 1)
        numberObjects.arNumber += 1

class table:
    typelock = ""
    children = []
    father = None

    def __init__(self, number, father):
        self.name = "TB"+str(numberObjects.tbNumber + 1)
        numberObjects.tbNumber += 1

class page:
    typelock = ""
    children = []
    father = None

    def __init__(self):
        self.name = "PG"+str(numberObjects.pgNumber + 1)
        numberObjects.pgNumber += 1

class row:
    typelock = ""
    children = []
    father = None

    def __init__(self):
        self.name = "RW"+str(numberObjects.rwNumber + 1)
        numberObjects.rwNumber += 1