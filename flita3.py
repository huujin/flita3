import graphviz
import networkx

def connected(graph):
    n = len(graph.nodes())
    m = len(graph.edges())
    if m >= ((n-1)*(n-2))/2:
        return True
    else:
        return False

graph_data = graphviz.Graph()
graph = networkx.Graph()
with open("list.txt", 'r') as f:
    for vertices in f:
        point = vertices.strip().split()
        if len(point) == 2:
            graph.add_edge(int(point[0]), int(point[1]))
            graph_data.edge(point[0],point[1])
        elif len(point) == 1:
            graph.add_node(int(point[0]))
            graph_data.node(point[0])



if connected(graph):
    print("Your graph is connected")
else:
    print("Your graph isn't connected")

graph_data.view()