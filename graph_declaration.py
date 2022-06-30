from Graph import Graph
from Node import Node
from Arc import Arc


def declare_graph(show, tree=False, rooted=True):
    if not tree:
        node_dict = {
            "London": Node(name="London", x=2, y=5),
            "Paris": Node(name="Paris", x=2, y=4),
            "Madrid": Node(name="Madrid", x=1, y=1),
            "Berlin": Node(name="Berlin", x=4, y=4),
            "Rome": Node(name="Rome", x=2.8, y=2),
            "Vienna": Node(name="Vienna", x=4, y=3),
            "Istanbul": Node(name="Istanbul", x=6, y=2),
            "Stockholm": Node(name="Stockholm", x=5, y=5),
            "Belgrade": Node(name="Belgrade", x=4.8, y=2.5),
            "Athens": Node(name="Athens", x=5, y=1.8),
            "Dublin": Node(name="Dublin", x=1, y=5.5),
            "Zurich": Node(name="Zurich", x=2.5, y=3),
            "Amsterdam": Node(name="Amsterdam", x=2.5, y=4.5),
            "Crete": Node(name="Crete", x=6, y=1),
            "Syracuse": Node(name="Syracuse", x=2.8, y=.4),
            "Cagliari": Node(name="Cagliari", x=2.2, y=1),
            "Moscow": Node(name="Moscow", x=6.1, y=4.3),
            "Baku": Node(name="Baku", x=6.8, y=2.2),
            "Copenhagen": Node(name="Copenhagen", x=3.5, y=4.8),
            "Bordeaux": Node(name="Bordeaux", x=1.5, y=2.3)
        }

        nodes = [node_dict[key] for key in node_dict.keys()]
        """
        [London, Paris, Madrid, Berlin, Rome, Vienna,
             Istanbul, Stockholm, Belgrade, Dublin, Zurich,
             Crete, Syracuse, Cagliari, Moscow, Baku, Amsterdam, Athens, Copenhagen]
        """
        arcs = [
            Arc(name="a1", from_=node_dict["London"], to=node_dict["Paris"]),
            Arc(name="a2", from_=node_dict["Paris"], to=node_dict["Bordeaux"]),
            Arc(name="a2", from_=node_dict["Bordeaux"], to=node_dict["Madrid"]),
            Arc(name="a3", from_=node_dict["Paris"], to=node_dict["Berlin"]),
            Arc(name="a4", from_=node_dict["Berlin"], to=node_dict["Vienna"]),
            Arc(name="a5", from_=node_dict["Rome"], to=node_dict["Vienna"]),
            Arc(name="a6", from_=node_dict["Rome"], to=node_dict["Madrid"]),
            Arc(name="a7", from_=node_dict["Dublin"], to=node_dict["London"]),
            Arc(name="a8", from_=node_dict["Dublin"], to=node_dict["Paris"]),
            Arc(name="a9", from_=node_dict["Rome"], to=node_dict["Zurich"]),
            Arc(name="a10", from_=node_dict["Paris"], to=node_dict["Zurich"]),
            Arc(name="a11", from_=node_dict["Zurich"], to=node_dict["Berlin"]),
            Arc(name="a12", from_=node_dict["Vienna"], to=node_dict["Belgrade"]),
            Arc(name="a13", from_=node_dict["Belgrade"], to=node_dict["Istanbul"]),
            Arc(name="a14", from_=node_dict["Berlin"], to=node_dict["Stockholm"]),
            Arc(name="a15", from_=node_dict["London"], to=node_dict["Copenhagen"]),
            Arc(name="a15", from_=node_dict["Copenhagen"], to=node_dict["Stockholm"]),
            Arc(name="a15", from_=node_dict["Copenhagen"], to=node_dict["Amsterdam"]),
            Arc(name="a16", from_=node_dict["Rome"], to=node_dict["Athens"]),
            Arc(name="a19", from_=node_dict["Athens"], to=node_dict["Istanbul"]),
            Arc(name="a17", from_=node_dict["Crete"], to=node_dict["Syracuse"]),
            Arc(name="a18", from_=node_dict["Cagliari"], to=node_dict["Syracuse"]),
            Arc(name="a18", from_=node_dict["Moscow"], to=node_dict["Stockholm"]),
            Arc(name="a18", from_=node_dict["Baku"], to=node_dict["Istanbul"]),
            Arc(name="a18", from_=node_dict["Amsterdam"], to=node_dict["London"]),
            Arc(name="a18", from_=node_dict["Amsterdam"], to=node_dict["Paris"]),
        ]

        g = Graph(nodes, arcs)
        if show:
            g.draw_graph()
        g.set_dist()

        return g

    elif tree and rooted:
        node_dict = {
            "London": Node(name="London", x=2, y=5),
            "Paris": Node(name="Paris", x=2, y=4),
            "Madrid": Node(name="Madrid", x=1, y=1),
            "Berlin": Node(name="Berlin", x=4, y=4),
            "Rome": Node(name="Rome", x=2.8, y=2),
            "Vienna": Node(name="Vienna", x=4, y=3, source=True),
            "Istanbul": Node(name="Istanbul", x=6, y=2),
            "Stockholm": Node(name="Stockholm", x=5, y=5),
            "Belgrade": Node(name="Belgrade", x=4.8, y=2.5),
            "Athens": Node(name="Athens", x=5, y=1.8),
            "Dublin": Node(name="Dublin", x=1, y=5.5),
            "Zurich": Node(name="Zurich", x=2.5, y=3),
            "Amsterdam": Node(name="Amsterdam", x=2.5, y=4.5),
            "Moscow": Node(name="Moscow", x=6.1, y=4.3),
            "Baku": Node(name="Baku", x=6.8, y=2.2),
            "Copenhagen": Node(name="Copenhagen", x=3.5, y=4.8),
            "Bordeaux": Node(name="Bordeaux", x=1.5, y=2.3)
        }

        nodes = [node_dict[key] for key in node_dict.keys()]

        arcs = [
            Arc(name="a1", from_=node_dict["Paris"], to=node_dict["London"], type_="directed"),
            Arc(name="a2", from_=node_dict["Madrid"], to=node_dict["Bordeaux"], type_="directed"),
            Arc(name="a3", from_=node_dict["Berlin"], to=node_dict["Paris"], type_="directed"),
            Arc(name="a4", from_=node_dict["Vienna"], to=node_dict["Berlin"], type_="directed"),
            Arc(name="a5", from_=node_dict["Vienna"], to=node_dict["Rome"], type_="directed"),
            Arc(name="a6", from_=node_dict["Rome"], to=node_dict["Madrid"], type_="directed"),
            Arc(name="a8", from_=node_dict["Paris"], to=node_dict["Dublin"], type_="directed"),
            Arc(name="a11", from_=node_dict["Berlin"], to=node_dict["Zurich"], type_="directed"),
            Arc(name="a12", from_=node_dict["Vienna"], to=node_dict["Belgrade"], type_="directed"),
            Arc(name="a13", from_=node_dict["Belgrade"], to=node_dict["Istanbul"], type_="directed"),
            Arc(name="a14", from_=node_dict["Berlin"], to=node_dict["Stockholm"], type_="directed"),
            Arc(name="a15", from_=node_dict["Amsterdam"], to=node_dict["Copenhagen"], type_="directed"),
            Arc(name="a19", from_=node_dict["Istanbul"], to=node_dict["Athens"], type_="directed"),
            Arc(name="a18", from_=node_dict["Stockholm"], to=node_dict["Moscow"], type_="directed"),
            Arc(name="a18", from_=node_dict["Istanbul"], to=node_dict["Baku"], type_="directed"),
            Arc(name="a18", from_=node_dict["Paris"], to=node_dict["Amsterdam"], type_="directed"),
        ]

        g = Graph(nodes, arcs,tree=True)
        if show:
            g.draw_graph()
        g.set_dist()
        g.detect_source_node()

        return g

    elif tree and not rooted:
        node_dict = {
            "London": Node(name="London", x=2, y=5),
            "Paris": Node(name="Paris", x=2, y=4),
            "Madrid": Node(name="Madrid", x=1, y=1),
            "Berlin": Node(name="Berlin", x=4, y=4),
            "Rome": Node(name="Rome", x=2.8, y=2),
            "Vienna": Node(name="Vienna", x=4, y=3),
            "Istanbul": Node(name="Istanbul", x=6, y=2),
            "Stockholm": Node(name="Stockholm", x=5, y=5),
            "Belgrade": Node(name="Belgrade", x=4.8, y=2.5),
            "Athens": Node(name="Athens", x=5, y=1.8),
            "Dublin": Node(name="Dublin", x=1, y=5.5),
            "Zurich": Node(name="Zurich", x=2.5, y=3),
            "Amsterdam": Node(name="Amsterdam", x=2.5, y=4.5),
            "Moscow": Node(name="Moscow", x=6.1, y=4.3),
            "Baku": Node(name="Baku", x=6.8, y=2.2),
            "Copenhagen": Node(name="Copenhagen", x=3.5, y=4.8),
            "Bordeaux": Node(name="Bordeaux", x=1.5, y=2.3)
            }

        nodes = [node_dict[key] for key in node_dict.keys()]

        arcs = [
            Arc(name="a1", from_=node_dict["Paris"], to=node_dict["London"] ),
            Arc(name="a2", from_=node_dict["Madrid"], to=node_dict["Bordeaux"]),
            Arc(name="a3", from_=node_dict["Berlin"], to=node_dict["Paris"]),
            Arc(name="a4", from_=node_dict["Vienna"], to=node_dict["Berlin"]),
            Arc(name="a5", from_=node_dict["Vienna"], to=node_dict["Rome"]),
            Arc(name="a6", from_=node_dict["Rome"], to=node_dict["Madrid"]),
            Arc(name="a8", from_=node_dict["Paris"], to=node_dict["Dublin"], type_="undirected"),
            Arc(name="a11", from_=node_dict["Berlin"], to=node_dict["Zurich"], type_="undirected"),
            Arc(name="a12", from_=node_dict["Vienna"], to=node_dict["Belgrade"], type_="undirected"),
            Arc(name="a13", from_=node_dict["Belgrade"], to=node_dict["Istanbul"], type_="undirected"),
            Arc(name="a14", from_=node_dict["Berlin"], to=node_dict["Stockholm"], type_="undirected"),
            Arc(name="a15", from_=node_dict["Amsterdam"], to=node_dict["Copenhagen"], type_="undirected"),
            Arc(name="a19", from_=node_dict["Istanbul"], to=node_dict["Athens"], type_="undirected"),
            Arc(name="a18", from_=node_dict["Stockholm"], to=node_dict["Moscow"], type_="undirected"),
            Arc(name="a18", from_=node_dict["Istanbul"], to=node_dict["Baku"], type_="undirected"),
            Arc(name="a18", from_=node_dict["Paris"], to=node_dict["Amsterdam"], type_="undirected"),
        ]

        g = Graph(nodes, arcs, tree=True)
        if show:
            g.draw_graph()
        g.set_dist()

        return g
