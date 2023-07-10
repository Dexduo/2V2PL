# import networkx as nx

# graph = nx.DiGraph()

# graph.add_node('1')
# graph.add_node('2')
# graph.add_edge('1', '2')
# graph.add_edge('2', '1')

# graph.add_node('1')
# graph.remove_node('1')

# print(list(nx.simple_cycles(graph)))


# # graph.add_node('1')
# if(len(cycle) == 0):
#     print("Massa!")

# print(graph)
# def iterate():
#     iterate = True
#     for i in range(1, 11):
#         print(i)
#         if(i==5):
#             iterate = False
#             return

# iterate()

# for j in range(10-1, -1, -1):
#     print(j)

# table = [
#     [1], [2], [3], [1]
# ]
# for i in range(0, len(table)-1):
#     if(table[i][0] == 1):
#         del table[i]

# print(table)´

table = [
    [1], [1], [1]
]
# 5, 2, 1
elementsToDelete = []

for i in range(0, len(table)):
    if(table[i][0] == 2):
        del table[i]
    if(i==len(table)-1):
        break

print(table)