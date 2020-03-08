# import networkx as nx
# import matplotlib.pyplot as plt
# from networkx.drawing.nx_agraph import graphviz_layout
from graphviz import Graph

dot = Graph(comment="The Roundtable", format="png")


dot.node('A', 'King Arthur', style="filled", fillcolor="#373737")
dot.node('B', 'Sir Bedevere the Wise', shape="square")
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')


print(dot.source)

dot.render('round-table.gv')
# g = nx.OrderedGraph()
# edgelist = [(1, 2), (2, 3), (1, 4), (3, 4), (1, 5)]

# g.add_edges_from(edgelist)

# nx.draw(g)
# plt.show()

# G = nx.Graph()

# G.add_node("ROOT")

# for i in range(5):
#     G.add_node("Child_%i" % i)
#     G.add_node("Grandchild_%i" % i)
#     G.add_node("Greatgrandchild_%i" % i)

#     G.add_edge("ROOT", "Child_%i" % i)
#     G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
#     G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

# plt.title("draw_networkx")
# nx.draw_networkx(G)

# plt.show()

# G = nx.DiGraph()

# G.add_node("ROOT")

# for i in range(5):
#     G.add_node("Child_%i" % i)
#     G.add_node("Grandchild_%i" % i)
#     G.add_node("Greatgrandchild_%i" % i)

#     G.add_edge("ROOT", "Child_%i" % i)
#     G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
#     G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

# # write dot file to use with graphviz
# # run "dot -Tpng test.dot >test.png"
# nx.nx_agraph.write_dot(G, 'test.dot')

# # same layout using matplotlib with no labels
# plt.title('draw_networkx')
# pos = graphviz_layout(G, prog='neato')
# nx.draw(G, pos, with_labels=False, arrows=False)
# plt.show()
