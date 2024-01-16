# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graph_declaration import declare_graph


def main():
    g = declare_graph(show=0, tree=1, rooted=False)
    if not g.tree:
        g.label_dfs()
    """
    for n in g.nodes:
        print(n.name, n.label)
    for key in g.adj_list:
        print(f"{key.name} : {[n.name for n in g.adj_list[key]]}")

        
    g.assign_closeness_centrality(draw=True)
    for n in g.nodes:
        print(f"{n.name} {n.closeness_cent}")
        
        
    for n in g.nodes:
        print(f"{n.name} {n.degree_cent}")    
    """
    # g.shortest_path_bfs(g.node_dict["London"], g.node_dict["Paris"], draw=True)
    # print(g.nodes)
    # print(g.adj_matrix)
    # g.check_adjacency_via_matrix(4, 7)
    # print(g.nodenames)

    # g.root_tree(g.node_dict["London"])
    # g.leaf_sum(draw=True)

    # g.tree_height()

    g.assign_degree_centrality(draw=1)
    g.find_center()
    print("All tasks completed.")


if __name__ == '__main__':
    main()
