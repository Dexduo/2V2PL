import networkx as nx

graph = nx.DiGraph()

graph.add_node('1')
graph.add_node('2')
graph.add_edge('1', '2')
graph.add_edge('2', '1')

graph.add_node('1')
graph.remove_node('1')

print(list(nx.simple_cycles(graph)))


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