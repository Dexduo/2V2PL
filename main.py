from objects import *
from parser import *
from dbStructure import *

# INSTRUÇÕES
# -> Os objetos estarão em uma lista arrayObjects."tipo" onde tipo está entre os valores: dbs, ars, tbs, pgs, rws
# -> A quantidade de objetos na estrutura pode ser consultada no objeto numberObjects."tipo" onde tipo está entre os valores: dbNumber, arNumber, tbNumber = 0, pgNumber = 0, rwNumber = 0
# -> Para iniciar um novo objeto basta passar o construtor "tipo"() onde tipo é um database, area, table, page, row
# -> A cada objeto pode ser adicionado um pai ou vários filhos
# -> A função showObjects exibe a lista de todos os objetos de cada tipo

genStructure() #gerar a estrutura do banco de dados     

showObjects() #exibe os objetos do banco de dados


# Exemplo de transação
trans1 = 'T2=  r1(AR1  )r1(TB2) w1(PG3) u4(RW2) w6(DB3) c4  '


print('\n')
print('-------------------------------------------------------------------------')
print('Parser')
print('-------------------------------------------------------------------------')
print('\n')


print('lista de operações da transação : ' + str(getOperations(trans1)))

primeiraOperacao = getOperations(trans1)[0]
print('primeira operação : ' + primeiraOperacao)

ultimaOperacao = getOperations(trans1)[5]
print('última operação : ' + ultimaOperacao)

print('\n')
print('-------------------------------------------------------------------------')
print('Transformando a string que representa a operação em um objeto Operation')
print('-------------------------------------------------------------------------')
print('\n')
op0 = Operation(primeiraOperacao)
op5 = Operation(ultimaOperacao)
print(f'operarionType : {op0.operationType}\n trasactionId : {op0.transactionId}\n dbObject : {op0.dbObject}')
print(f'operarionType : {op5.operationType}\n trasactionId : {op5.transactionId}\n dbObject : {op5.dbObject}')