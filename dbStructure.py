from objects import *

def genStructure():
    for i in range(0, 1):
        newDatabase = database()
        for j in range(0, 2):
            newArea = area()
            newArea.father(newDatabase)
            newDatabase.child(newArea)
            for k in range(0, 2):
                newTable = table()
                newTable.father(newArea)
                newArea.child(newTable)
                for l in range(0, 2):
                    newPage = page()
                    newPage.father(newTable)
                    newTable.child(newPage)
                    for m in range(0, 2):
                        newRow = row()
                        newRow.father(newPage)
                        newPage.child(newRow)