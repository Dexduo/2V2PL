from objects import *

# INSTRUÇÕES
# -> Os objetos estarão em uma lista arrayObjects."tipo" onde tipo está entre os valores: dbs, ars, tbs, pgs, rws
# -> A quantidade de objetos na estrutura pode ser consultada no objeto numberObjects."tipo" onde tipo está entre os valores: dbNumber, arNumber, tbNumber = 0, pgNumber = 0, rwNumber = 0
# -> Para iniciar um novo objeto basta passar o construtor "tipo"() onde tipo é um database, area, table, page, row
# -> A cada objeto pode ser adicionado um pai ou vários filhos
# -> A função showObjects exibe a lista de todos os objetos de cada tipo



# database()
# table()
# area()
# area()
# area()

for i in range(0, 1):
    database()
    for j in range(0, 2):
        newArea = area()
        newArea.father = arrayObjects.dbs[i]
        arrayObjects.dbs[i].children.append(newArea)

print(arrayObjects.dbs[0].children[0].name)

# print(numberObjects.dbNumber)
# print(numberObjects.arNumber)
# print(arrayObjects.dbs[0].name)
# print(arrayObjects.dbs[0])
showObjects()