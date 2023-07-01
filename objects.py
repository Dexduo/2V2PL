dbNumber = 1
arNumber = 1
tbNumber = 1
pgNumber = 1
rwNumber = 1

dbs = []
ars = []
tbs = []
pgs = []
rws = []

class database:
    typelock = ""
    children = []

    def __init__(self, number):
        self.name = "DB"+str(number)

    # def children(self, number):


class area:
    typelock = ""
    children = []
    father = None

    def __init__(self, number, father):
        self.name = "AR"+str(number)
        self.father = father
        arNumber += 1

class table:
    typelock = ""
    children = []
    father = None

    def __init__(self, number, father):
        self.name = "TB"+str(number)
        self.father = father
        tbNumber += 1

class page:
    typelock = ""
    children = []
    father = None

    def __init__(self, number, father):
        self.name = "PG"+str(number)
        self.father = father
        pgNumber += 1

class row:
    typelock = ""
    children = []
    father = None

    def __init__(self, number, father):
        self.name = "RW"+str(number)
        self.father = father
        rwNumber += 1