import graph as g

print("Grafik yang di inisialisasi:")
grafik = g.create_graph([(0, 5), (0, 4), (0, 2), (1, 5), (1, 4), (2, 4), (2, 3), (4, 5)])

print("derajat dari vertex 0:")
g.get_degree(grafik, 0)

print("dfs dengan stack(start node=5):")
g.dfs_traversal(grafik, 5)

print("dfs dengan library(start node=5):")
g.dfs_new(grafik, 5)

print("bfs dengan queue(start node=2):")
g.bfs_traversal(grafik, 2)

print("bfs dengan library(start node=2):")
g.bfs_new(grafik, 2)

print("mencari path terpendek dari vertex 3 ke 5:")
g.find_shortest_path(grafik, 3, 5)

g.visualize_graph(grafik)
