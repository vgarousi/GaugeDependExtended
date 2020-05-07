from application.smells.abstractSmell import AbstractSmell
import networkx as nx

class UnusedCptSmell(AbstractSmell):
    def __init__(self, renderer):
        self.renderer = renderer

    def get_smell_name(self) -> str:
        return "Unused Concept"

    def get_smell_id(self) -> str:
        return "unused_cpt"

    def get_smell_description(self) -> str:
        return "Concept is not called by any scenario, make sure to check that all spec files are included in graph."


    def has_smell(self, graph) -> bool:
        in_degrees = list(graph.in_degree())
        unused_cpts = [node for node in in_degrees if (not node[0].startswith("Scenario:")) and (node[1]==0)]
        return len(unused_cpts)>0

    def update_graph(self, graph) -> None:
        in_degrees = list(graph.in_degree())
        unused_cpts = [node for node in in_degrees if (not node[0].startswith("Scenario:")) and (node[1] == 0)]
        for cpt in unused_cpts:
            graph.nodes[cpt[0]]["smell"]=True
            graph.nodes[cpt[0]]["smell_names"].append(self.get_smell_name())

    def get_smell_subgraph(self, graph) -> list:
        in_degrees = list(graph.in_degree())
        unused_cpts = [node for node in in_degrees if (not node[0].startswith("Scenario:")) and (node[1] == 0)]

        output_files = list()

        for i, test in enumerate(unused_cpts):
            node = test[0]
            smell_graph= nx.MultiDiGraph()

            smell_graph.add_edges_from(graph.out_edges(node), data=True)
            for neighbour in graph.neighbors(node):
                smell_graph.add_edges_from(graph.out_edges(neighbour, data=True))
                for other in graph.neighbors(neighbour):
                    smell_graph.add_edges_from(graph.out_edges(other, data=True))

            nx.set_node_attributes(smell_graph, False, "smell")
            nx.set_node_attributes(smell_graph, list(), "smell_names")

            self.renderer.render_graph(smell_graph, f"unused-cpt-smell-{i}.html")
            output_files.append(f"./unused-cpt-smell-{i}.html")

        return output_files
