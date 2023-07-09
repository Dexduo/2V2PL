from objects import *
from parserOperations import *
from dbStructure import *

# INSTRUÇÕES
# -> Os objetos estarão em uma lista arrayObjects."tipo" onde tipo está entre os valores: dbs, ars, tbs, pgs, rws
# -> A quantidade de objetos na estrutura pode ser consultada no objeto numberObjects."tipo" onde tipo está entre os valores: dbNumber, arNumber, tbNumber = 0, pgNumber = 0, rwNumber = 0
# -> Para iniciar um novo objeto basta passar o construtor "tipo"() onde tipo é um database, area, table, page, row
# -> A cada objeto pode ser adicionado um pai ou vários filhos
# -> A função genStructure gera a estrutura do banco de dados
# -> A função showObjects exibe a lista de todos os objetos de cada tipo
# -> A função operationsTable retorna uma tabela onde cada linha é uma operação dividido por: número da transação, objeto do banco de dados, tipo de operação

genStructure() #gerar a estrutura do banco de dados     

# showObjects() #exibe os objetos do banco de dados


# Exemplo de transação
trans1 = 'T2=  R1(AR1  )R1(TB2) W1(PG3) U4(RW2) W6(DB3) C4  '

trans1 = operationsTable(trans1)

